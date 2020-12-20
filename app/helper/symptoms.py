import os

import pandas as pd

from app.helper.csv_helper import read_csv

def get_symptoms_data(data_path="app/static/data/symptoms/",ignore=True,sort=False,columns=['Symptoms']):

    file_list = os.listdir(data_path)
    
    df = read_csv(data_path+file_list.pop(),columns)
    for name in file_list:
        read_file_name = data_path + name
        data = read_csv(read_file_name,columns)
        df = df.append(data, ignore_index=ignore, sort=sort)
    return df

def get_data_count(data,keyword_list,col_name):

    count = 0
    result = {}

    for keyword in keyword_list:
        for k in keyword_list[keyword]:
            count += len(data[data[col_name].str.contains(k)].axes[0])
        
        result[keyword] = count
        count = 0

    return result


