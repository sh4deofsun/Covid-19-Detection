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

    output = ctrl.Consequent(np.arange(0, 10, 0.1), 'output')

    output['low'] = fuzz.trimf(output.universe, [0, 0, 4])
    output['medium'] = fuzz.trimf(output.universe, [4, 7, 10])
    output['high'] = fuzz.trimf(output.universe, [7, 10, 10])


    @staticmethod
    def simulation(cough,fever_inp="",breath_inp="",add_inp=""):
        # controller
        covid_controller = ctrl.ControlSystem(MF.get_rule())

        # simulation
        covid_simulator = ctrl.ControlSystemSimulation(covid_controller)


        MF.load_input(covid_simulator,cough)

        covid_simulator.compute()

        # output
        result = covid_simulator.output['output']

        return result

    @staticmethod
    def get_rule():
        rule1 = ctrl.Rule(MF.cough['neg'], MF.output['medium'])
        rule2 = ctrl.Rule(MF.cough['pos'], MF.output['high'])

        return [rule1,rule2]

    @staticmethod
    def load_input(covid_simulator,cough):
        covid_simulator.input['cough'] = cough

  