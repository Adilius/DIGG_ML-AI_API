import requests
import math
import pandas as pd

#Global variables for keeping track outside of functions:
numericList = [] #Stores every key with a numeric value together with the value (for floatConverter, stanDevCalc, outlierCount and getOutlierAmount)
numericKeyList = [] #Stores key with a numeric value (for floatConverter and stanDevCalc)
outlierAmount = 0 #Counts amount of outliers (for outlierCount and getOutlierAmount)
jsonFull = [] 

#Evaluate function
def evaluate(jsonData):
    jsonFiltering(jsonData)
    floatConverter()
    stanDevCalc()
    df = pd.DataFrame(jsonFull)
    return df

#Checks if json has next, and/or result attributes, if not, take the entire json
def jsonFiltering(jsonData):
    global jsonFull
    hasNext = False
    hasResults = False
    newJson = ""

    for key in jsonData.keys():
        if key == "next":
            nextLink = jsonData[key]
            hasNext = True
        if key == "results":
            hasResults = True
    if hasNext == True:
        addToDict(jsonData["results"])
        newJson = jsonFiltering(linkToJSON(nextLink))
        return
    elif hasResults == True:
        addToDict(jsonData["results"])
    else:
        addToDict(jsonData)
    if newJson != "":
        jsonFiltering(newJson)

#Appends json to jsonFull
def addToDict(results):
    global jsonFull

    for value in results:
        jsonFull.append(value)

#Converts recieved link to json data
def linkToJSON(link):
    result = requests.get(link)
    data = result.json()
    return data

#Converts numeric values to float type if possible
def floatConverter():
    global numericList
    global numericKeyList
    global jsonFull

    for instance in jsonFull:
        for val in instance:
            try:
                floatValue = instance[val]
                floatValue = floatValue.replace(',', '.')
                floatValue = floatValue.replace(' ', '')
                floatValue = round(float(floatValue), 2)
                numericList.append([val, floatValue])
                if val not in numericKeyList:
                    numericKeyList.append(val)
            except:
                pass

#Calcualtes standard deviation for every key with numeric values
def stanDevCalc():
    global numericList
    global numericKeyList

    for keyName in numericKeyList:
        stanDev = 0
        totalValue = 0
        totalSquareValue = 0
        amount = 0
        squareList = []
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
        outlierCount(keyName, mean, stanDev)

#Counts amount of outliers
def outlierCount(keyName, mean, stanDev):
    global numericList
    global outlierAmount

    for value in numericList:
        if value[0] == keyName:
            if value[1] > mean+(stanDev*3) or value[1] < mean-(stanDev*3):
                outlierAmount+=1

#Counts amount of attributes with mixed data types
def mixedTypeCount(df):
    global jsonFull

    jsonTemp = jsonFull
    mixedTypeAmount = 0

    for att in df.columns:
        mixedTypeCheck = False
        for inst in jsonTemp:
            for instCheck in reversed(jsonTemp):
                if type(inst[att]) != type(instCheck[att]):
                    mixedTypeCheck = True
                jsonTemp.remove(instCheck)
        if mixedTypeCheck == True:
            mixedTypeAmount+=1

    return mixedTypeAmount

#Returns amount of numeric values
def getNumericListLength():
    return len(numericList)

#Returns amount of outliers
def getOutliers():
    return outlierAmount

#Clear global values
def clearGlobals():
    global numericList
    global numericKeyList
    global outlierAmount
    global jsonFull

    numericList.clear()
    numericKeyList.clear()
    outlierAmount = 0 
    jsonFull.clear()