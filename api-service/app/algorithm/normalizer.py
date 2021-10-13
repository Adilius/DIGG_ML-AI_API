import pandas as pd
from sklearn import preprocessing
import requests
import json
from evaluation_methods import evaluate, getNumericList, getNumericKeyList, clearGlobals

def jsonNormalize():
    names = getNumericKeyList()
    numericList = getNumericList()

    for name in names:
        tempArray = []
        for value in numericList:
            if value[0] == name:
                tempArray.append(value[1])
        
        normalizedArray = preprocessing.normalize([tempArray])
        print(name, "normalized:", normalizedArray)

def main():
    #Example API-links:
    #No outliers: https://haninge.entryscape.net/rowstore/dataset/fb39ab31-dd4b-4414-bc5f-5af01b62a1fa/json?_limit=500
    #Has outliers: https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=500

    #data = pd.read_json("https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=10")

    #apiLink = input("Paste link to API: ")
    apiLink = "https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=5"

    result = requests.get(apiLink)

    if result.status_code == 200:
        data = result.json()
        #f = open('api-service/app/algorithm/test.json')
        #data = json.load(data)
        evaluate(data)
        jsonNormalize()
        clearGlobals()

    else:
        print("ERROR! Status code", result.status_code)

if __name__ == '__main__':
    main()