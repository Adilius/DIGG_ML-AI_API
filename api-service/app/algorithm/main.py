import requests
import json
import time
import pandas as pd
from .Analyze_Dataset import Get_A_List_Of_ML_Analysis, Get_Correlation_Classifier
from .ML_Algorithms import Decision_Tree_Classifier as dtc
from .ML_Algorithms import Random_Forest_Classifier as rfc
from .evaluation_methods import evaluate, getInstanceAmount, getAttributeAmount, getAttributes, getValueAmount, getEmptyValueAmount, getNumericValueAmount, getOutlierAmount, getDuplicateAmount, getMixedTypeAmount, clearGlobals

def evaluate_dataset(dataset: dict):

    time.sleep(5)
    df = evaluate(dataset)

    response = {
        'Instances': getInstanceAmount(df),
        'Attributes': getAttributeAmount(df),
        'Attribute names': getAttributes(df),
        'Values': getValueAmount(df),
        #'Decision Tree Classifier': Get_A_List_Of_ML_Analysis(dataset, dtc.get_DTC_statistical_analysis),
        #'Correlation Classifier' : Get_Correlation_Classifier(dataset)
    }

    if getEmptyValueAmount(df) > 0:
        response.update({'Empty values': getEmptyValueAmount(df)})
    if getNumericValueAmount() > 0:
        response.update({'Numeric values': getNumericValueAmount()})
    if getOutlierAmount() > 0:
        response.update({'Outliers': getOutlierAmount()})
    if getDuplicateAmount(df) > 0:
        response.update({'Duplicate instances': getDuplicateAmount(df)})
    if getMixedTypeAmount(df) > 0:
        response.update({'Mixed datatypes': getMixedTypeAmount(df)})

    clearGlobals()
    return response

#For direct testing (remove the '.' "from .evaluation_methods import ...")
# def main():
#     #Example API-links:
#     #No outliers: https://haninge.entryscape.net/rowstore/dataset/fb39ab31-dd4b-4414-bc5f-5af01b62a1fa/json?_limit=500
#     #Has outliers: https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=500

#     #apiLink = input("Paste link to API: ")
#     apiLink = "https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=500"

#     result = requests.get(apiLink)

#     if result.status_code == 200:
#         data = result.json()
#         #f = open('api-service/app/algorithm/test.json')
#         #data = json.load(f)
#         response = evaluate_dataset(data)
#         print(response)
#     else:
#         print("ERROR! Status code", result.status_code)

# if __name__ == '__main__':
#     main()