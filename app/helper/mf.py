import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from app.helper.skfuzzy_mp import view
class MF():

    cough = ctrl.Antecedent(np.arange(0, 10, 0.1), 'cough')

    cough['neg'] = fuzz.trimf(cough.universe, [0, 0, 5.95])

    cough['pos'] = fuzz.trimf(cough.universe, [5.95, 10, 10])

    fever = ctrl.Antecedent(np.arange(0, 10, 0.1), 'fever')

    fever['low'] = fuzz.trimf(fever.universe,[0,0,2.65])
    fever['medium'] = fuzz.trimf(fever.universe,[2.65,5,7])
    fever['high'] = fuzz.trimf(fever.universe,[5,10,10])

    breath_diff = ctrl.Antecedent(np.arange(0, 10, 0.1), 'breath_diff')

    breath_diff['low'] = fuzz.trimf(fever.universe,[0,0,7])
    breath_diff['medium'] = fuzz.trimf(fever.universe,[7,8,9])
    breath_diff['high'] = fuzz.trimf(fever.universe,[9,10,10])

    pain = ctrl.Antecedent(np.arange(0, 10, 0.1), 'pain')

    pain['low'] = fuzz.trimf(fever.universe,[0,0,7.20])
    pain['medium'] = fuzz.trimf(fever.universe,[7.20,8,8.20])
    pain['high'] = fuzz.trimf(fever.universe,[8.20,10,10])

    output = ctrl.Consequent(np.arange(0, 10, 0.1), 'output')

    output['low'] = fuzz.trimf(output.universe, [0, 0, 4])
    output['medium'] = fuzz.trimf(output.universe, [4, 7, 10])
    output['high'] = fuzz.trimf(output.universe, [7, 10, 10])


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
        view(MF.output,sim=covid_simulator,name="output")

        return result

    """
        IF Öksürük AND Ateş düşük THEN ateş düşükse = output['low']
        IF düşük ateş AND orta THEN ateş orta ise = output['medium']
        IF düşük ateş ANDyüksekse çıktı yüksek ise = output['high']
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
            (MF.breath_diff['medium'] & MF.fever['medium']), MF.output['medium'])
        rule3 = ctrl.Rule(
            (MF.cough['neg'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['high']) | 
            (MF.fever['high'] & MF.breath_diff['medium'] & MF.cough['neg'] & MF.pain['high']) |
            (MF.fever['high'] & MF.breath_diff['high'] & MF.cough['neg'] & MF.pain['medium']) |
            (MF.fever['high'] & MF.breath_diff['medium'] & MF.cough['neg'] & MF.pain['medium']) |
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
            (MF.cough['pos'] & MF.fever['medium'] & MF.breath_diff['medium'] & MF.pain['low']), MF.output['medium'])
        rule6 = ctrl.Rule(
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['high']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['medium'] & MF.pain['high']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['medium']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['low'] & MF.pain['high']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['high'] & MF.pain['low']) |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['low']) &  MF.pain['medium'] |
            (MF.cough['pos'] & MF.fever['high'] & MF.breath_diff['medium']) &  MF.pain['low'] |
            (MF.cough['pos'] & MF.fever['medium'] & MF.breath_diff['high'] & MF.pain['high']), MF.output['high'])

        return [rule1,rule2,rule3,rule4,rule5,rule6]

    @staticmethod
    def load_input(covid_simulator,cough,fever,breath_diff,pain):
        covid_simulator.input['cough'] = cough
        covid_simulator.input['fever'] = fever
        covid_simulator.input['breath_diff'] = breath_diff
        covid_simulator.input['pain'] = pain

  