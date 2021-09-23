import requests
import json

#Global variables for keeping track outside of functions
counter = 0
fieldCounter = 0
emptyFieldCounter = 0
    
#Prints which fields fields are empty and where they are
def emptyCheck(data, s):
    global counter
    global emptyFieldCounter

    if data[s]=="":
        print('Empty field "' + s + '" at result', counter)
        emptyFieldCounter+=1

#Prints total amount and percentage of empty fields
def emptyResult():
    global fieldCounter
    global emptyFieldCounter

    percentage = round((emptyFieldCounter / fieldCounter) * 100)
    print("\nTotal amount of empty fields:", str(emptyFieldCounter) + '/' + str(fieldCounter), '(' + str(percentage) + '%)\n')

#Reads every single attribute from json and runs them through emptyCheck unless they are lists or dicts
def jsonReader(data):
    global counter
    global fieldCounter
    global emptyFieldCounter

    for k in data.keys():
        s=str(k)
        if(type(data[s])==dict):
            jsonReader(data[s])
        elif(type(data[s])==list):
            for i in data[s]:
                counter+=1
                if(type(i)==dict):
                    jsonReader(i)
        else:
            #print("Column:", s, "| Type:", type(data[s]), "| Value:", data[s])
            fieldCounter+=1
            emptyCheck(data, s)
            
#Main
def main():
    #Example API-links:
    #https://haninge.entryscape.net/rowstore/dataset/fb39ab31-dd4b-4414-bc5f-5af01b62a1fa/json?_limit=500
    #https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=500

    apiLink = input("Paste link to API: ")

    response = requests.get(apiLink)

    if(response.status_code==200):
        data = response.json()
        jsonReader(data)
        emptyResult()
    else:
        print("ERROR! Status code", response.status_code)

if __name__ == '__main__':
    main()