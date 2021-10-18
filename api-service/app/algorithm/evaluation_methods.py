from .jsonToDataframe import getNumericListLength, getOutliers, mixedTypeCount

#Returns amount of instances
def getInstanceAmount(df):
    return len(df)

#Returns amount of attributes
def getAttributeAmount(df):
    return len(df.columns)

#Returs string containing all attributes
def getAttributes(df):
    attributes = []
    for col in df:
        attributes.append(col)

    return attributes

#Returns amount of values
def getValueAmount(df):
    return int(df.size)

#Returns amount of empty fields
def getEmptyValueAmount(df):
    emptyList = (df == "").sum()
    misVal = 0
    for value in emptyList:
        misVal+=value

    return misVal

#Returns amount of numeric values
def getNumericValueAmount():
    return getNumericListLength()

#Returns amount of outliers
def getOutlierAmount():
    return getOutliers()

#Returns amount of duplicates
def getDuplicateAmount(df):
    return len(df)-len(df.drop_duplicates())

#Returns amount of attributes with mixed datatypes
def getMixedTypeAmount(df):
    return mixedTypeCount(df)
