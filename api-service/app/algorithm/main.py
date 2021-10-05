import requests
import json
import time
from .evaluation_methods import evaluate, getInstanceAmount, getAttributeAmount, getAttributes, getEmptyValueAmount, getOutlierAmount, getDuplicateAmount, getMixedTypeAmount, clearGlobals

def evaluate_dataset(dataset: dict):

    #Anropa funktioner här fär att skapa en dictionary som returneras

    time.sleep(5)

    evaluate(dataset)

    response = {
        'Number of instances': getInstanceAmount(),
        'Number of attributes': getAttributeAmount(),
        'Attributes': getAttributes(),
        'Missing values': getEmptyValueAmount(),
        'Outliers': getOutlierAmount(),
        'Duplicate instances': getDuplicateAmount(),
        'Attributes with mixed datatypes': getMixedTypeAmount()
    }

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
#         #data = result.json()
#         f = open('api-service/app/algorithm/test.json')
#         data = json.load(f)
#         response = evaluate_dataset(data)
#         print(response)
#     else:
#         print("ERROR! Status code", result.status_code)

# if __name__ == '__main__':
#     main()