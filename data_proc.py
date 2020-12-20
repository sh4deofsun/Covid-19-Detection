import pandas as pd
import matplotlib.pyplot as plt

from app.helper.symptoms import get_symptoms_data,get_data_count

symptoms_list = {
    "cough" : ["cough"],
    "fever" : ["fever"],
    "pain" : ["sore","myalgias","ache"],
    "breath" : ["breath","pneumo","phary","gasp"],
}

def get_statistics(data,total_count):
    result = {}

    for d in data:
        result[d] = {
            "Positive": data[d]*100/total_count,
            "Negative": (total_count - data[d])*100/total_count
        }
    
    return result

def show_data(symp_count,symp_statistics,total_count):

    for name in symp_statistics:
        plt.bar(["Positive", "Negative"], [symp_count[name], total_count - symp_count[name]], width=.6)
        plt.legend()
        plt.xlabel(name.capitalize())
        plt.ylabel('Number of Reports')
        plt.title(f'Reported {name.capitalize()} as Symptom')
        plt.show()
        print(f"{name.capitalize()} - Positive:", symp_statistics[name]['Positive'] , "%,",
            "Negative", symp_statistics[name]['Negative'] , "%")

all_symptoms = get_symptoms_data()

total_count = len(all_symptoms.axes[0])

symp_count = symptoms_count_list = get_data_count(all_symptoms,symptoms_list,"Symptoms")

symp_statistics = get_statistics(symp_count,total_count)

show_data(symp_count,symp_statistics,total_count)
