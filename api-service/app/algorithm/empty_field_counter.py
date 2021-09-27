import requests
import json

#Global vars if sets resultcounter > 500 (WIP)
counter = 1
fieldCounter = 0
emptyFieldCounter = 0

#Prints every column name
def arrayPrinter(array):
    for i in array:
        print(i)
    
#Prints which fields are empty and percentage of empty fields
def emptyCheck(result, columnNames):
    global counter
    global fieldCounter
    global emptyFieldCounter

    for i in result:
        for j in columnNames:
            fieldCounter+=1
            if not i[j]:
                print("Empty field at result", counter, 'at column "' + j + '"')
                emptyFieldCounter+=1
        counter+=1
    percentage = round((emptyFieldCounter / fieldCounter) * 100)
    print("\nTotal amount of empty fields:", str(emptyFieldCounter) + '/' + str(fieldCounter), '(' + str(percentage) + '%)\n')

#Main
def main():
    apiLink = "https://haninge.entryscape.net/rowstore/dataset/fb39ab31-dd4b-4414-bc5f-5af01b62a1fa/json?_limit=500"
    
    responseAPI = requests.get(apiLink)
    data = responseAPI.text
    parseJson = json.loads(data)
    result = parseJson['results']

    columnNames = []

    for k in result[0].keys():
        columnNames.append(k)

    #arrayPrinter(columnNames)
    emptyCheck(result, columnNames)

main()