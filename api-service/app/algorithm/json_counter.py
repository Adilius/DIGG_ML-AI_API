
#JSON Dataset downloaded from this link: https://opendata.umea.se/api/v2/catalog/datasets/skyddade-omraden-djur-och-vaxtskyddsomraden-sverigesweden/records

#Project created: 2021-09-13
#Developer: Björn Norén

#Datafile: open_data_umea.json

# Information: This application reads a JSON-file and returns all the datatypes within the JSON-file

import json
#f = open('../../Datasets/open_data_umea.json',)


# returns JSON object as 
# a dictionary
#data = json.load(f)

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

#look_for_dicts(data)

print("Lägg in JSON fil:")

def hello_world():
    return {"Hello":"world"}
