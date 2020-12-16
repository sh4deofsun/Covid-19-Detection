import os

import pandas as pd

def get_symptoms_data(data_path="app/static/data/",ignore=True,sort=False):

    file_list = os.listdir(data_path)
    
    df = read_csv(data_path+file_list.pop())
    for name in file_list:
        read_file_name = data_path + name
        data = read_csv(read_file_name)
        df.append(data, ignore_index=ignore, sort=sort)
    return df

def read_csv(name):
    dataset = pd.read_csv(name)
    symptoms = dataset[dataset.Symptoms.notnull()]
    parse_symptoms = pd.DataFrame(symptoms, columns=['Symptoms'])
    return parse_symptoms

