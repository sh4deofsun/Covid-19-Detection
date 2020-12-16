import pandas as pd

def read_csv(name,columns):
    dataset = pd.read_csv(name)
    copy_col = columns[:]
    data = clear_data_set(copy_col,dataset)
    data_symptoms = pd.DataFrame(data, columns=columns)
    return data_symptoms

def clear_data_set(columns,dataset):
    check = "dataset.{}.notnull()"
    data = dataset[eval(check.format(columns.pop()))]
    for name in columns:
        check = check.format(name)
        data = data[eval(check)]
    return data
