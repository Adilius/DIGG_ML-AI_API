import pandas as pd
import json

#   Date      : 2021-09-28
#   Developer : Bj�rn Nor�n
#   What      : This program takes in a dataset and check whichs FORMAT the dataset has
#             : When the FORMAT is checked, it transforms it to a DATAFRAME and returns it
#   Note      : It's currently reads a specific .csv file for testing

#file = input("Read file: ")

def read_dataset():
    file = 'Datasets/breast_cancer.csv' 

    if file.lower().endswith('.csv'):
        file = open(file)
        df = pd.read_csv(file,)
        if len(df.columns) == 1:
            df = pd.read_csv(file, sep=";")
        return df

    if file.lower().endswith('.json'):
        data = json.load(file)
        df = pd.DataFrame.from_dict(data)
        return df