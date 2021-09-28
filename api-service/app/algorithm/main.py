import requests
from evaluation_methods import InstanceResult, AttributeResult, EmptyResult, OutlierResult

def evaluate_dataset(dataset: dict):

    #Anropa funktioner här fär att skapa en dictionary som returneras

    response = {
        'Number of instances': InstanceResult(dataset),
        'Number of attributes': AttributeResult(dataset),
        'Missing values': EmptyResult(dataset),
        'Outliers': OutlierResult(dataset),
    }

    # dummy_response = {
    #     'Number of instances': 30,
    #     'Number of attributes': 30,
    #     'Missing values': 37,
    #     'Data Set Characteristics': 'Multivariate',

    # }
    
    return response

#For direct testing
# def main():
#     #Example API-links:
#     #No outliers: https://haninge.entryscape.net/rowstore/dataset/fb39ab31-dd4b-4414-bc5f-5af01b62a1fa/json?_limit=500
#     #Has outliers: https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=500

#     apiLink = input("Paste link to API: ")

#     result = requests.get(apiLink)

#     if result.status_code == 200:
#         data = result.json()
#         response = evaluate_dataset(data)
#         print(response)
#     else:
#         print("ERROR! Status code", result.status_code)

# if __name__ == '__main__':
#     main()