import math
import json
import requests

#Example API-links:
#No outliers: https://haninge.entryscape.net/rowstore/dataset/fb39ab31-dd4b-4414-bc5f-5af01b62a1fa/json?_limit=500
#Has outliers: https://catalog.sodertalje.se/rowstore/dataset/ee44b6b8-ab8c-44dc-ab0c-f7acf9a5e20d/json?_limit=500

#Global variables for keeping track outside of functions:
instanceAmount = 0 #Counts amount of instances (for instance counter)
attributeCheck = [] #To check if attribute appear more than once (if not it's part of the header)
attributeList = [] #Store every atribute name (for attribute counter)
emptyAmount = 0 #Counts amount of empty fields (for empty field counter)
numericList = [] #Stores every numeric field name and result together as string and float (for outlier counter)
numericKeyList = [] #Stores every name of numeric fields for easy access (for standard deviation calculation)
outlierAmount = 0 #Counts amount of outliers (for outlier counter)

#Returns amount of instances
def InstanceResult(data):
    return InstanceCounter(data)

#Counts amount of instances
def InstanceCounter(data):
    global instanceAmount

    for key in data.keys():
        keyName = str(key)
        if type(data[keyName]) == dict:
            InstanceCounter(data[keyName])
        elif type(data[keyName]) == list:
            for innerKey in data[keyName]:
                instanceAmount+=1
                if type(innerKey) == dict:
                    InstanceCounter(innerKey)

    return instanceAmount

#Returns amount of attributes
def AttributeResult(data):
    return AttributeCounter(data)

#Counts amount of attributes
def AttributeCounter(data):
    global attributeList

    for key in data.keys():
        keyName = str(key)
        if type(data[keyName]) == dict:
            AttributeCounter(data[keyName])
        elif type(data[keyName]) == list:
            for innerKey in data[keyName]:
                if type(innerKey) == dict:
                    AttributeCounter(innerKey)
        elif keyName in attributeCheck and keyName not in attributeList:
            attributeList.append(keyName)
        elif keyName not in attributeCheck:
                attributeCheck.append(keyName)

    return len(attributeList)

#Returns amount of empty fields
def EmptyResult(data):
    return EmptyCounter(data)

#Counts amount of empty fields
def EmptyCounter(data):
    global emptyAmount

    for key in data.keys():
        keyName = str(key)
        if type(data[keyName]) == dict:
            EmptyCounter(data[keyName])
        elif type(data[keyName]) == list:
            for innerKey in data[keyName]:
                if type(innerKey) == dict:
                    EmptyCounter(innerKey)
        elif data[keyName]=="":
                emptyAmount+=1

    return emptyAmount

#Returns amount of outliers
def OutlierResult(data):
    FloatCounter(data)
    StandardDeviationCalculator()
    return outlierAmount

#Stores every numeric field and every field with numeric values
def FloatCounter(data):
    global numericList
    global numericKeyList

    for key in data.keys():
        keyName = str(key)
        if type(data[keyName]) == dict:
            FloatCounter(data[keyName])
        elif type(data[keyName]) == list:
            for innerKey in data[keyName]:
                if type(innerKey) == dict:
                    FloatCounter(innerKey)
        else:
            try:
                floatValue = float(data[keyName].replace(',', '.'))
                numericList.append([keyName, floatValue])
                if keyName not in numericKeyList:
                    numericKeyList.append(keyName)
            except:
                pass

#Calcualtes standard deviation for every numeric field
def StandardDeviationCalculator():
    global numericList
    global numericKeyList
    squareList = []

    for keyName in numericKeyList:
        stanDev = 0
        totalValue = 0
        totalSquareValue = 0
        amount = 0
        squareList.clear()
        for value in numericList:
            if value[0] == keyName:
                totalValue+=value[1]
                amount+=1
        mean = totalValue/amount
        for value in numericList:
            if value[0] == keyName:
                square = (value[1]-mean)*(value[1]-mean)
                squareList.append(square)
        for value in squareList:
            totalSquareValue+=value
        stanDev = round(math.sqrt(totalSquareValue/amount), 2)
        OutlierCounter(keyName, mean, stanDev)

#Counts amount of outliers
def OutlierCounter(keyName, mean, stanDev):
    global numericList
    global outlierAmount

    for value in numericList:
        if value[0] == keyName:
            if value[1] > mean+(stanDev*3) or value[1] < mean-(stanDev*3):
                outlierAmount+=1

def ClearGlobals():
    global instanceAmount
    global attributeCheck
    global attributeList
    global emptyAmount
    global numericList
    global numericKeyList
    global outlierAmount

    instanceAmount = 0 
    attributeCheck.clear()
    attributeList.clear()
    emptyAmount = 0 
    numericList.clear()
    numericKeyList.clear()
    outlierAmount = 0 