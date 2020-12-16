import os

import pandas as pd

from app.helper.csv_helper import read_csv

def get_symptoms_data(data_path="app/static/data/symptoms/",ignore=True,sort=False,columns=['Symptoms']):

    file_list = os.listdir(data_path)
    
    df = read_csv(data_path+file_list.pop(),columns)
    for name in file_list:
        read_file_name = data_path + name
        data = read_csv(read_file_name,columns)
        df.append(data, ignore_index=ignore, sort=sort)
    return df


