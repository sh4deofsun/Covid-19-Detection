class Risk():

    @staticmethod
    def calc_additional_risks_score(age, polluted, hypertension, diabetes, cardiovascular, respiratory, immune):

        risk = 0

        if age <= 10: risk += 0.55
        elif age >= 80: risk += 1.55
        elif age >= 60: risk += 1.00
        elif age >= 50: risk += 0.50

        if polluted: risk += 1.0
        if hypertension: risk += 1.55
        if diabetes: risk += 1.55
        if cardiovascular: risk += 1.5
        if respiratory: risk += 3.05
        if immune: risk += 4.05

        return risk
