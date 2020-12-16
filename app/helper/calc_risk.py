def calc_additional_risks(age, polluted, hypertension, diabetes, cardiovascular, respiratory, immune):

    risk = 0

    if age <= 10: risk += 0.5
    elif age >= 80: risk += 1.5
    elif age >= 60: risk += 1
    elif age >= 50: risk += 0.5

    if polluted: risk += 1
    if hypertension: risk += 1.5
    if diabetes: risk += 1.5
    if cardiovascular: risk += 1
    if respiratory: risk += 3
    if immune: risk += 4

    if risk > 10: risk = 10

    return risk
