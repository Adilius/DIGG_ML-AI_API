from .Analyze_Dataset import Get_A_List_Of_ML_Analysis, Get_Correlation_Classifier
from .ML_Algorithms import Decision_Tree_Classifier as dtc
from .jsonToDataframe import evaluate, clearGlobals
from .evaluation_methods import getInstanceAmount, getAttributeAmount, getAttributes, getValueAmount, getEmptyValueAmount, getNumericValueAmount, getOutlierAmount, getDuplicateAmount, getMixedTypeAmount
import time

def evaluate_dataset(dataset: dict):

    start = time.time()
    df = evaluate(dataset)

    response = {
        'Header' : df.head().to_dict(),
        'Instances': getInstanceAmount(df),
        'Attributes': getAttributeAmount(df),
        'Attribute names': getAttributes(df),
        'Values': getValueAmount(df),
        'Decision Tree Classifier': Get_A_List_Of_ML_Analysis(df, dtc.get_DTC_statistical_analysis),
        'Correlation Classifier' : Get_Correlation_Classifier(df)
    }

    if getEmptyValueAmount(df) > 0:
        response.update({'Empty values': getEmptyValueAmount(df)})
    if getNumericValueAmount() > 0:
        response.update({'Numeric values': getNumericValueAmount()})
    if getOutlierAmount() > 0:
        response.update({'Outliers': getOutlierAmount()})
    if getDuplicateAmount(df) > 0:
        response.update({'Duplicate instances': getDuplicateAmount(df)})
    if getMixedTypeAmount(df) > 0:
        response.update({'Mixed datatypes': getMixedTypeAmount(df)})

    end = time.time()
    response.update({'Time measurements': end - start})

    clearGlobals()

    return response
