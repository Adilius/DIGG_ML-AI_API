import pandas as pd
import requests
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
        check = 0
        if type(data) == dict:
            for k in data.keys(): #check for the keys
               s = str(k) #convert content to string
               print(type(data[s])) #check if it is a string the data
               if type(data[s]) == list: #check if its a list wich means it is the "data" to analice
                  if data[s]== "results":
                     check = 1
        if check ==1:
            return 1
        else:
            print("NO DATA FOUND LABELED AS 'RESULTS' PLEASE CHECK AGAIN/FIX THE ISSUE")
            return 0