import math

#Global variables for keeping track outside of functions:
instanceList = [] #Stores every instance (for getInstanceAmount and duplicateCount)
dataList = [] #Stores every value together with key and type (for mixedTypeCount and getEmptyValueAmount)
attributeCheck = [] #To check if attribute appear more than once, if not it's probably part of the header (for attributeAdd)
attributeList = [] #Store every atribute that appear more than once in attributeCheck (for attributeAdd and getAttributeAmount)
numericList = [] #Stores every key with a numeric value together with the value (for floatConverter, stanDevCalc, outlierCount and getOutlierAmount)
numericKeyList = [] #Stores key with a numeric value (for floatConverter and stanDevCalc)
outlierAmount = 0 #Counts amount of outliers (for outlierCount and getOutlierAmount)

#Evaluate function
def evaluate(data):
    jsonCounter(data)
    stanDevCalc()

#Goes through the entire json dataset and adds neccesary information to global variables
def jsonCounter(data):
    global instanceList
    global dataList

    for key in data.keys():
        keyName = str(key)
        value = data[keyName]
        valueType = type(value)
        if valueType == dict:
            instanceList.append(value)
            jsonCounter(value)
        elif valueType == list:
            for innerValue in value:
                if type(innerValue) == dict:
                    instanceList.append(innerValue)
                    jsonCounter(innerValue)
        else:
            attributeAdd(keyName)
            floatConvert(value, keyName)
            dataList.append([keyName, valueType, value])

#Adds attributes to attributeList if they appear more than once
def attributeAdd(attribute):
    global attributeList
    global attributeCheck

    if attribute in attributeCheck and attribute not in attributeList:
        attributeList.append(attribute)
    elif attribute not in attributeCheck:
        attributeCheck.append(attribute)

#Converts numeric values to float type if possible
def floatConvert(value, keyName):
    global numericList
    global numericKeyList

    try:
        floatValue = float(value.replace(',', '.'))
        numericList.append([keyName, floatValue])
        if keyName not in numericKeyList:
            numericKeyList.append(keyName)
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

#Counts amount of duplicates
def duplicateCount():
    global instanceList
    duplicates = 0

    for instance in instanceList:
        duplicateCheck = 0
        for instanceCheck in reversed(instanceList):
            if instance == instanceCheck:
                duplicateCheck+=1
        if duplicateCheck > 1:
            duplicates+=1
        instanceList.remove(instanceCheck)
    
    return duplicates

#Counts amount of mixed datatypes
def mixedTypeCount():
    global dataList
    global attributeList
    mixedDataTypeAmount = 0

    for attribute in attributeList:
        mixedTypeCheck = False
        for value in dataList:
            if attribute == value[0]:
                for valueCheck in reversed(dataList):
                    if attribute == valueCheck[0]:
                        if value[1] != valueCheck[1]:
                            mixedTypeCheck = True
                        dataList.remove(valueCheck)
        if mixedTypeCheck == True:
            mixedDataTypeAmount+=1

    return mixedDataTypeAmount

#Returns amount of instances
def getInstanceAmount():
    global instanceList
    return len(instanceList)

#Returns amount of attributes
def getAttributeAmount():
    global attributeList
    return len(attributeList)

#Returs string containing all attributes
def getAttributes():
    global attributeList
    attributeString = '[ '

    for attribute in attributeList:
        attributeString += attribute + ', '
    
    attributeString = attributeString[:-2] + ' ]'
    return attributeString

#Returns amount of empty fields
def getEmptyValueAmount():
    emptyAmount = 0
    for value in dataList:
        if value[2] == "":
            emptyAmount+=1
    return emptyAmount

#Returns amount of outliers
def getOutlierAmount():
    global outlierAmount
    global numericList

    outlierAmountString = str(outlierAmount) + '/' + str(len(numericList))
    return outlierAmountString

#Returns amount of duplicates
def getDuplicateAmount():
    return duplicateCount()

#Returns amount of attributes with mixed datatypes
def getMixedTypeAmount():
    return mixedTypeCount()

#Clear global values
def clearGlobals():
    global instanceList
    global attributeCheck
    global attributeList
    global numericList
    global numericKeyList
    global outlierAmount
    global dataList

    instanceList.clear()
    attributeCheck.clear()
    attributeList.clear()
    numericList.clear()
    numericKeyList.clear()
    outlierAmount = 0 
    dataList.clear()