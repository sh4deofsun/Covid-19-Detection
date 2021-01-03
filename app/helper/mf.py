import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from app.helper.skfuzzy_mp import view
class MF():

    cough = ctrl.Antecedent(np.arange(0, 10, 0.1), 'cough')

    cough['neg'] = fuzz.trimf(cough.universe, [0, 0, 5.95])

    cough['pos'] = fuzz.trimf(cough.universe, [3.95, 10, 10])

    fever = ctrl.Antecedent(np.arange(0, 10, 0.1), 'fever')

    fever['low'] = fuzz.trimf(fever.universe,[0,0,2.65])
    fever['medium'] = fuzz.trimf(fever.universe,[1.65,4.82,7])
    fever['high'] = fuzz.trimf(fever.universe,[5,10,10])

    breath_diff = ctrl.Antecedent(np.arange(0, 10, 0.1), 'breath_diff')

    breath_diff['low'] = fuzz.trimf(breath_diff.universe,[0,0,6.50])
    breath_diff['medium'] = fuzz.trimf(breath_diff.universe,[5.50,6.80,7.25])
    breath_diff['high'] = fuzz.trimf(breath_diff.universe,[7,10,10])

    pain = ctrl.Antecedent(np.arange(0, 10, 0.1), 'pain')

    pain['low'] = fuzz.trimf(pain.universe,[0,0,7.20])
    pain['medium'] = fuzz.trimf(pain.universe,[6.20,7.70,8.15])
    pain['high'] = fuzz.trimf(pain.universe,[7.20,10,10])

    output = ctrl.Consequent(np.arange(0, 10, 0.1), 'output')

    output['low'] = fuzz.trimf(output.universe, [0, 0, 4])
    output['medium'] = fuzz.trimf(output.universe, [2, 5, 8])
    output['high'] = fuzz.trimf(output.universe, [6, 10, 10])


    @staticmethod
    def simulation(cough,fever,breath_diff,pain,add_inp=""):
        # controller
        covid_controller = ctrl.ControlSystem(MF.get_rule())

        # simulation
        covid_simulator = ctrl.ControlSystemSimulation(covid_controller)


        MF.load_input(covid_simulator,cough,fever,breath_diff,pain)

        covid_simulator.compute()

        # output
        result = covid_simulator.output['output']
        """
            Her seferinde grafiklerin oluşturulmasına gerek yok.
            Oluşturulması gereken durumlar için config dosyası hazırlanabilir.
        """
        view(MF.output,sim=covid_simulator,name="output")
        view(MF.cough,sim=covid_simulator,name="cough")
        view(MF.fever,sim=covid_simulator,name="fever")
        view(MF.breath_diff,sim=covid_simulator,name="breath_diff")
        view(MF.pain,sim=covid_simulator,name="pain")

        return result

    """
        EĞER Öksürük VE Ateş düşük ateş düşükse = output['low']
        EĞER düşük ateş VE orta ateş orta ise = output['medium']
        EĞER düşük ateş VE yüksekse çıktı yüksek ise = output['high']
        ...
    """

    @staticmethod
    def get_rule():
        #coug neg
        rule1 = ctrl.Rule(
            (MF.cough['neg'] & MF.fever['low'] & MF.breath_diff['low'] & MF.pain['low']) |
            (MF.cough['neg'] & MF.fever['low'] & MF.breath_diff['medium'] & MF.pain['medium']) |
            (MF.cough['neg'] & MF.fever['low'] & MF.breath_diff['low'] & MF.pain['medium']) |
            (MF.cough['neg'] & MF.fever['low'] & MF.breath_diff['medium'] & MF.pain['low']) |
            (MF.cough['neg'] & MF.fever['low'] & MF.breath_diff['low'] & MF.pain['high']) |
            (MF.cough['neg'] & MF.fever['low'] & MF.pain['low']) |
            (MF.fever['low']), MF.output['low'])
        rule2 = ctrl.Rule(
            (MF.cough['neg'] & MF.fever['medium'] & MF.breath_diff['medium'] & MF.pain['medium']) |
            (MF.cough['neg'] & MF.fever['medium'] & MF.breath_diff['medium'] & MF.pain['low'] ) |
            (MF.cough['neg'] & MF.fever['medium'] & MF.breath_diff['low'] & MF.pain['medium'] ) |
            (MF.cough['neg'] & MF.fever['medium'] & MF.breath_diff['low'] & MF.pain['low'] ) |
            (MF.cough['neg'] & MF.fever['high'] & MF.breath_diff['low'] & MF.pain['low'] ) |
            (MF.breath_diff['medium'] & MF.fever['medium']), MF.output['medium'])
        rule3 = ctrl.Rule(
            (MF.cough['neg'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['high']) | 
            (MF.fever['high'] & MF.breath_diff['medium'] & MF.cough['neg'] & MF.pain['high']) |
            (MF.fever['high'] & MF.breath_diff['high'] & MF.cough['neg'] & MF.pain['medium']) |
            (MF.fever['high'] & MF.breath_diff['medium'] & MF.cough['neg'] & MF.pain['medium']) |
            (MF.fever['high'] & MF.breath_diff['low'] & MF.cough['neg'] & MF.pain['high']) |
            (MF.fever['high'] & MF.breath_diff['high'] & MF.cough['neg'] & MF.pain['low']) |
            (MF.fever['medium'] & MF.breath_diff['high'] & MF.cough['neg'] & MF.pain['high']) |
            (MF.fever['medium'] & MF.breath_diff['low'] & MF.cough['neg'] & MF.pain['high']), MF.output['high'])
        #coug pos
        rule4 = ctrl.Rule(
            (MF.cough['pos'] & MF.fever['low'] & MF.breath_diff['low'] & MF.pain['low']) |
            (MF.cough['pos'] & MF.fever['low'] & MF.breath_diff['low'] & MF.pain['medium']) |
            (MF.cough['pos'] & MF.fever['low'] & MF.breath_diff['medium'] & MF.pain['low']), MF.output['low'])
        rule5 = ctrl.Rule(
            (MF.cough['pos'] & MF.fever['medium'] & MF.breath_diff['medium'] & MF.pain['medium']) |
            (MF.cough['pos'] & MF.fever['medium'] & MF.breath_diff['low'] & MF.pain['medium']) |
            (MF.cough['pos'] & MF.fever['medium'] & MF.breath_diff['low'] & MF.pain['low']) |
            (MF.cough['pos'] & MF.fever['low'] & MF.breath_diff['high'] & MF.pain['high']) |
            (MF.cough['pos'] & MF.fever['medium'] & MF.breath_diff['medium'] & MF.pain['low']), MF.output['medium'])
        rule6 = ctrl.Rule(
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['high']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['medium'] & MF.pain['high']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['medium']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['low'] & MF.pain['high']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['low']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['low']) &  MF.pain['medium'] |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['medium']) &  MF.pain['low'] |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['low']) &  MF.pain['low'] |
            (MF.cough['pos'] & MF.fever['medium'] & MF.breath_diff['high'] & MF.pain['high']), MF.output['high'])

        return [rule1,rule2,rule3,rule4,rule5,rule6]

    @staticmethod
    def load_input(covid_simulator,cough,fever,breath_diff,pain):
        covid_simulator.input['cough'] = cough
        covid_simulator.input['fever'] = fever
        covid_simulator.input['breath_diff'] = breath_diff
        covid_simulator.input['pain'] = pain

  