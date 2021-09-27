
#Project created: 2021-09-13
#Developer: Björn Norén

# Information: This application reads a JSON-file and returns all the datatypes within the JSON-file

import json
import requests

# returns JSON object as 
# a dictionary

def look_for_dicts(data):    
    if type(data) == dict:
        for k in data.keys():
            s = str(k)
            print(type(data[s]))
            if type(data[s]) == list:
                for i in data[s]:
                    print(type(i))
                    if type(i) == dict:
                        look_for_dicts(i)
            if type(data[s]) == dict:
                look_for_dicts(data[s])

def look_for_dicts_from_api():

    # example api from dataportal.se : https://konsumentverket.entryscape.net/rowstore/dataset/86ce5095-1641-4390-8987-bdc3c77625a7
    url = input("enter url for API: ")
    response = requests.get(url)

    # if response is valid 
    if (response.status_code == 200):
        data = response.json()
        if (type(data) == dict):
            look_for_dicts(data)

def hello_world():
    return {"Hello":"world"}

#look_for_dicts_from_api()
