#   Date      : 2021-09-30
#   Developer : Björn Norén
#   What      : This app reads a dataset and evaluates it by using a choosen ML_Algorithm.
#             : The app will iterate every column/label in a dataset and return the accuracy
#             : for each target based on a choosen ML_Algorithm

import pandas as pd
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import preprocessing
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd
from ML_Algorithms import Decision_Tree_Classifier as dtc
from ML_Algorithms import Random_Forest_Classifier as rfc


def Get_A_List_Of_ML_Analysis(df, ml_evaluator):

    columns = []

    # Save all columns/labels in a list
    for col in df.columns:
        columns.append(col)

    le = preprocessing.LabelEncoder()
    df = df.apply(le.fit_transform)

    num = len(columns)
    i = 0
    feature_cols = []

    list_of_accuracies = []

    while i < num:
        for val in columns:
            feature_cols.append(val)

        cur_column = columns[i]
        feature_cols.pop(i)
        
        list_of_accuracies.append(ml_evaluator(df, columns, feature_cols, cur_column, i))

        feature_cols = []

        i += 1

    return list_of_accuracies

# This function will analyse a dataset based on every column/label in the dataset
# Any of the ML-algorithms in this project should work
def Analyse_Dataset(df, ml_evaluator):

    columns = []

    # Save all columns/labels in a list
    for col in df.columns:
        columns.append(col)

    #Pre-process the data. 
    le = preprocessing.LabelEncoder()
    df = df.apply(le.fit_transform)

    num = len(columns)
    i = 0
    feature_cols = []

    # Save all columns except the target label in feature_cols
    while i < num:
        for val in columns:
            feature_cols.append(val)

        cur_column = columns[i]
        feature_cols.pop(i)
        
        # This function is one of the ML-algorithms 
        ml_evaluator(df, columns, feature_cols, cur_column, i)

        feature_cols = []

        i += 1


