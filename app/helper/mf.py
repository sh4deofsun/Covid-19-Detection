from pyit2fls import IT2FS, trapezoid_mf, tri_mf, IT2FS_Gaussian_UncertMean, \
    IT2FS_plot, IT2FLS, min_t_norm, max_s_norm, TR_plot, crisp

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from numpy import linspace

class MF():

    severity = linspace(0.0, 10.0, 100)

    cough = ctrl.Antecedent(np.arange(0, 10, 0.1), 'cough')

    cough['neg'] = fuzz.trimf(cough.universe, [0, 0, 5.95])

    cough['pos'] = fuzz.trimf(cough.universe, [5.95, 10, 10])

    fever = ctrl.Antecedent(np.arange(0, 10, 0.1), 'fever')

    fever['low'] = fuzz.trimf(fever.universe,[0,0,2.65])
    fever['medium'] = fuzz.trimf(fever.universe,[2.65,5,7])
    fever['high'] = fuzz.trimf(fever.universe,[5,10,10])


    output = ctrl.Consequent(np.arange(0, 10, 0.1), 'output')

    output['low'] = fuzz.trimf(output.universe, [0, 0, 4])
    output['medium'] = fuzz.trimf(output.universe, [4, 7, 10])
    output['high'] = fuzz.trimf(output.universe, [7, 10, 10])


    @staticmethod
    def simulation(cough,fever,breath_inp="",add_inp=""):
        # controller
        covid_controller = ctrl.ControlSystem(MF.get_rule())

        # simulation
        covid_simulator = ctrl.ControlSystemSimulation(covid_controller)


        MF.load_input(covid_simulator,cough,fever)

        covid_simulator.compute()

        # output
        result = covid_simulator.output['output']

        return result

    """
        Öksürük ve Ateş düşük veya ateş düşükse = output['low']
        Öksürük düşük ateş orta veya ateş orta ise = output['medium']
        Öksürük düşük ateş yüksekse çıktı yüksek olacaktır.


        Hizmet iyiyse veya yemek kalitesi iyiyse, BU DURUMDA bahşiş yüksek olacaktır.
        Servis ortalama ise, BU DURUMDA bahşiş orta olacaktır.
        EĞER hizmet zayıftı ve gıda kalitesi kötüyse, BU DURUMDA bahşiş düşük olacaktır.
    """

    @staticmethod
    def get_rule():
        #coug neg
        rule1 = ctrl.Rule((MF.cough['neg'] & MF.fever['low']) | MF.fever['low'], MF.output['low'])
        rule2 = ctrl.Rule((MF.cough['neg'] & MF.fever['medium']) | MF.fever['medium'], MF.output['medium'])
        rule3 = ctrl.Rule((MF.cough['neg'] & MF.fever['high']) | MF.fever['high'], MF.output['high'])
        #coug pos
        rule4 = ctrl.Rule(MF.cough['pos'] & MF.fever['low'], MF.output['low'])
        rule5 = ctrl.Rule(MF.cough['pos'] & MF.fever['medium'], MF.output['medium'])
        rule6 = ctrl.Rule(MF.cough['pos'] & MF.fever['high'], MF.output['high'])

        return [rule1,rule2,rule3,rule4,rule5,rule6]

    @staticmethod
    def load_input(covid_simulator,cough,fever):
        print(cough,fever)
        covid_simulator.input['cough'] = cough
        covid_simulator.input['fever'] = fever

  