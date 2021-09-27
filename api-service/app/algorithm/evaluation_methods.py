import requests
import math
import json

#Global variables for keeping track outside of functions:
resultCount = 0 #Counts total amount of results (only for showing where something occurs (only works for empty fields atm))
numericCounter = 0 #Counts total amount of numeric fields (for outlier result)
fieldCounter = 0 #Counts total amount of fields (for empty field result) 
emptyFieldCounter = 0 #Counts total amount of empty fields (for empty field detection and result)
floatArray = [] #Stores every numeric field name and result together as string and float (for outlier detection)
fieldArray = [] #Stores every name of numeric fields for easy access (for standard deviation calculation)
outlierAmount = 0 #Counts amount of outliers (for outlier detection and result)

#Reads every single attribute from json and runs them through emptyCheck unless they are lists or dicts
def jsonReader(data):
    global resultCount
    global numericCounter
    global fieldCounter
    global floatArray
    global fieldArray

    for k in data.keys():
        s=str(k)
        if(type(data[s])==dict):
            jsonReader(data[s])
        elif(type(data[s])==list):
            for i in data[s]:
                resultCount+=1
                if(type(i)==dict):
                    jsonReader(i)
        else:
            #print("Column:", s, "| Type:", type(data[s]), "| Value:", data[s])
            fieldCounter+=1
            emptyCheck(data, s)
            try:
                tempFloat = float(data[s].replace(',', '.'))
                #print("Field:", s, "| Value:", temp)
                numericCounter+=1
                floatArray.append([s, tempFloat])
                if(s not in fieldArray):
                    fieldArray.append(s)
            except:
                pass

#Prints which fields fields are empty and where they are
def emptyCheck(data, s):
    global resultCount
    global emptyFieldCounter

    if data[s]=="":
        #print('Empty field "' + s + '" at result', resultCount)
        emptyFieldCounter+=1

#Prints total amount and percentage of empty fields
def emptyResult():
    global fieldCounter
    global emptyFieldCounter

    percentage = round((emptyFieldCounter / fieldCounter) * 100, 2)
    print("\nTotal amount of empty fields:", str(emptyFieldCounter) + '/' + str(fieldCounter), '(' + str(percentage) + '%)\n')

#Calcualtes standard deviation for every numeric field
def standardDeviationCalculator():
    global floatArray
    global fieldArray
    tempArray = []

    for f in fieldArray:
        stanDev = 0
        temp = 0
        counter = 0
        tempArray.clear()
        for i in floatArray:
            if(i[0]==f):
                temp+=i[1]
                counter+=1
        mean = temp/counter
        for i in floatArray:
            if(i[0]==f):
                tempArray.append((i[1]-mean)*(i[1]-mean))
        for i in tempArray:
            stanDev+=i
        stanDev=round(math.sqrt(stanDev/counter), 2)
        #print('"' + f + '"', 'standard deviation:', stanDev)
        outlierDetector(f, mean, stanDev)

#Checks for outliers
def outlierDetector(field, mean, stanDev):
    global floatArray
    global outlierAmount

    for i in floatArray:
        if(i[0]==field):
            if(i[1]>mean+(stanDev*3) or i[1]<mean-(stanDev*3)):
                #print('Outlier detected: Field "' + field + '" Value:', i[1])
                #print('Should be between', mean-(stanDev*3), '-', mean+(stanDev*3))
                outlierAmount+=1

#Prints total amount and percentage of outliers, and evaluates if there's an unusual amount of them
def outlierResult():
    global numericCounter
    percentage = round((outlierAmount / numericCounter) * 100, 2)
    print('Outliers:', str(outlierAmount) + '/' + str(numericCounter), '(' + str(percentage) + '%)')
    if percentage > 0.3:
        print("More outliers than normal (should be max 0.3%)")
    else:
        print("Normal amount of outliers")  

#Main
def main():
    #Example API-links:
    #No outliers: https://haninge.entryscape.net/rowstore/dataset/fb39ab31-dd4b-4414-bc5f-5af01b62a1fa/json?_limit=500
    #Has outliers: https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=500

    apiLink = input("Paste link to API: ")

    response = requests.get(apiLink)

    if(response.status_code==200):
        data = response.json()
        jsonReader(data)
        emptyResult()
        standardDeviationCalculator()
        outlierResult()
    else:
        print("ERROR! Status code", response.status_code)

if __name__ == '__main__':
    main()