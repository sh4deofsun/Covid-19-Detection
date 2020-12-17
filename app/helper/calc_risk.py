import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def calc_risk_percentage(risk_score=10,density = 0):
    """
    Antecedent:
        Bulanık bir kontrol sistemi için önceki (giriş / sensör) değişken.

    Consequent:
        Bulanık bir kontrol sistemi için sonuç (çıktı / kontrol) değişkeni.
    """
    ##Risk oranı
    risk = ctrl.Antecedent(np.arange(0, 10, 0.5), 'risk')

    #Dışarda harcanan zaman
    time_spent_outside = ctrl.Consequent(np.arange(1, 15, 0.1), 'outside')


    # Kümenin öğeleri üyelik derecelerine göre eşlenir
    risk['high'] = fuzz.zmf(risk.universe, 0, 10)
    risk['low'] = fuzz.smf(risk.universe, 0, 10)

    # Kümenin öğeleri üyelik derecelerine göre eşlenir
    time_spent_outside['long'] = fuzz.zmf(time_spent_outside.universe, 1, 15)
    time_spent_outside['short'] = fuzz.smf(time_spent_outside.universe, 1,15)

    #Bulanık bir kontrol sisteminde Antecedent'ı Consequent'a bağlayan kural.
    rule1 = ctrl.Rule(risk['high'], time_spent_outside['long'])
    rule2 = ctrl.Rule(risk['low'], time_spent_outside['short'])

    # controller
    riskController = ctrl.ControlSystem([rule1, rule2])

    # simulation
    riskSimulator = ctrl.ControlSystemSimulation(riskController)

    # load the value in the simulator
    riskSimulator.input['risk'] = risk_score

    # process
    riskSimulator.compute()

    # output
    result = riskSimulator.output['outside'] * density

    return result


def calc_additional_risks_score(age, polluted, hypertension, diabetes, cardiovascular, respiratory, immune):

    risk = 1

    if age <= 10: risk += 0.5
    elif age >= 80: risk += 1.5
    elif age >= 60: risk += 1
    elif age >= 50: risk += 0.8

    if polluted: risk += 1
    if hypertension: risk += 1.4
    if diabetes: risk += 1.5
    if cardiovascular: risk += 1.7
    if respiratory: risk += 2.5
    if immune: risk += 2.5

    return risk
