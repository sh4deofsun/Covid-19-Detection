from pyit2fls import IT2FS, trapezoid_mf, tri_mf, IT2FS_Gaussian_UncertMean, \
    IT2FS_plot, IT2FLS, min_t_norm, max_s_norm, TR_plot, crisp

import skfuzzy as fuzz

from numpy import linspace

class MF():

    severity = linspace(0.0, 10.0, 100)

    cough_neg = IT2FS(severity, trapezoid_mf, [0., 0.001, 3, 7, 1.0],
                      tri_mf, [0, 0.001, 2, 0.5])
    cough_pos = IT2FS(severity, trapezoid_mf, [5, 8, 9.999, 10, 1.0],
                      tri_mf, [8.5, 9.999, 10, 0.5])

    fever_low = IT2FS_Gaussian_UncertMean(severity, [0, 2.65, 1, 1.0])
    fever_mod = IT2FS_Gaussian_UncertMean(severity, [5, 2.65, 1, 1.0])
    fever_high = IT2FS_Gaussian_UncertMean(severity, [10, 2.65, 1, 1.0])

    breath_diff_low = IT2FS_Gaussian_UncertMean(severity, [0, 1.75, 1, 1.0])
    breath_diff_mod = IT2FS_Gaussian_UncertMean(severity, [5, 2.5, 1, 1.0])
    breath_diff_extr = IT2FS_Gaussian_UncertMean(severity, [10, 1.75, 1, 1.0])

    add_low = IT2FS_Gaussian_UncertMean(severity, [0, 5, 2, 1.0])
    add_high = IT2FS_Gaussian_UncertMean(severity, [10, 5, 2, 1.0])

    risk_low = IT2FS_Gaussian_UncertMean(severity, [0, 3, 1, 1.0])
    risk_high = IT2FS_Gaussian_UncertMean(severity, [6.5, 2, 1, 1.0])
    risk_veryhigh = IT2FS_Gaussian_UncertMean(severity, [10.7, 1, 1, 1.0])
    
    @staticmethod
    def add_rule(myIT2FLS):
        myIT2FLS.add_rule([("cough", MF.cough_neg), ("fever", MF.fever_low), ("breath", MF.breath_diff_low), ("add", MF.add_low)],
                      [("risk", MF.risk_low)])
        myIT2FLS.add_rule([("cough", MF.cough_pos), ("fever", MF.fever_mod), ("breath", MF.breath_diff_low), ("add", MF.add_low)],
                        [("risk", MF.risk_low)])
        myIT2FLS.add_rule([("cough", MF.cough_neg), ("fever", MF.fever_high), ("breath", MF.breath_diff_low), ("add", MF.add_low)],
                        [("risk", MF.risk_low)])
        myIT2FLS.add_rule([("cough", MF.cough_neg), ("fever", MF.fever_high), ("breath", MF.breath_diff_low), ("add", MF.add_high)],
                        [("risk", MF.risk_low)])
        myIT2FLS.add_rule([("cough", MF.cough_neg), ("fever", MF.fever_low), ("breath", MF.breath_diff_extr), ("add", MF.add_low)],
                        [("risk", MF.risk_high)])
        myIT2FLS.add_rule([("cough", MF.cough_neg), ("fever", MF.fever_high), ("breath", MF.breath_diff_mod), ("add", MF.add_low)],
                        [("risk", MF.risk_high)])
        myIT2FLS.add_rule([("cough", MF.cough_pos), ("fever", MF.fever_mod), ("breath", MF.breath_diff_mod), ("add", MF.add_high)],
                        [("risk", MF.risk_veryhigh)])
        myIT2FLS.add_rule([("cough", MF.cough_pos), ("fever", MF.fever_low), ("breath", MF.breath_diff_extr), ("add", MF.add_high)],
                        [("risk", MF.risk_veryhigh)])
        myIT2FLS.add_rule([("cough", MF.cough_pos), ("fever", MF.fever_mod), ("breath", MF.breath_diff_mod), ("add", MF.add_high)],
                        [("risk", MF.risk_veryhigh)])
        myIT2FLS.add_rule([("cough", MF.cough_pos), ("fever", MF.fever_high), ("breath", MF.breath_diff_extr), ("add", MF.add_high)],
                        [("risk", MF.risk_veryhigh)])
    @staticmethod
    def add_input_veriable(myIT2FLS):
        myIT2FLS.add_input_variable("cough")
        myIT2FLS.add_input_variable("fever")
        myIT2FLS.add_input_variable("breath")
        myIT2FLS.add_input_variable("add")
        myIT2FLS.add_output_variable("risk")

    @staticmethod
    def evaluate(myIT2FLS,cough_inp,fever_inp,breath_inp,add_inp,):

        it2out, tr = myIT2FLS.evaluate({"cough": cough_inp, "fever": fever_inp, "breath": breath_inp, "add": add_inp},
                                min_t_norm, max_s_norm, MF.severity,
                                method="Centroid", algorithm="EKM")
        it2out["risk"].plot(title="Type-2 output MF converted to Type-1")
        TR_plot(MF.severity, tr["risk"])

        return int((crisp(tr["risk"])) * 10)

    @staticmethod
    def plot_cough_mf():
        IT2FS_plot(MF.cough_neg, MF.cough_pos,
                   title="Cough",
                   legends=["Negative", "Positive"],
                   )
    @staticmethod
    def plot_fever_mf():
        IT2FS_plot(MF.fever_low, MF.fever_mod, MF.fever_high,
                   title="Fever",
                   legends=["Low", "Moderate", "High"],
                   )
    @staticmethod
    def plot_additional_mf():
        IT2FS_plot(MF.add_low, MF.add_high,
                   title="Additional Risks",
                   legends=["Low", "High"],
                   )
    @staticmethod
    def plot_breathdiff_mf():
        IT2FS_plot(MF.breath_diff_low, MF.breath_diff_mod, MF.breath_diff_extr,
                   title="Breathing Difficulty",
                   legends=["Low", "Moderate", "High"],
                   )
    @staticmethod
    def plot_risk_mf():
        IT2FS_plot(MF.risk_low, MF.risk_high, MF.risk_veryhigh,
                   title="Overall Risk",
                   legends=["Unlikely", "Likely", "Extremely Likely"],
                   )
