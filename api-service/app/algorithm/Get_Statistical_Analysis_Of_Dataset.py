#
#   Date      : 2021-09-30
#   Developer : Björn Norén
#   What      : This app reads a dataset and evaluates it by using a choosen ML_Algorithm.
#             : The app will print statistical properties such as Mean, Median etc. 
#             : based on choosen ML_Algorithm
#

import pandas as pd
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import preprocessing
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd
import read_dataset as rd
from ML_Algorithms import Decision_Tree_Classifier as dtc
from ML_Algorithms import Naive_Bayes as nb
from ML_Algorithms import KNN_Classifier as knn
from ML_Algorithms import Random_Forest_Classifier as rfc
import statistics

# Read in a given dataset
# - This is hard coded for the moment for making testing easier
df = rd.read_dataset()

print(df.head()) # This line of code can be here temporary 

columns = []

# Print columns
for col in df.columns:
    columns.append(col)

# This function will print out the following for a dataset based on a given ML-Algorithm
# - Mean
# - Median
# - Min
# - Max
# - Stdev
# - Variance 
def Get_Statistical_Analysis_Of_Dataset(df, columns, ml_evaluator):

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

    print("\n")
    print("Mean:     ", statistics.mean(list_of_accuracies))
    print("Median:   ", statistics.median(list_of_accuracies))
    print("Min:      ", min(list_of_accuracies))
    print("Max:      ", max(list_of_accuracies))
    print("Stdev:    ", statistics.stdev(list_of_accuracies))
    print("Variance: ", statistics.variance(list_of_accuracies))


Get_Statistical_Analysis_Of_Dataset(df, columns, dtc.get_DTC_statistical_analysis)
Get_Statistical_Analysis_Of_Dataset(df, columns, nb.get_NB_statistical_analysis)
Get_Statistical_Analysis_Of_Dataset(df, columns, knn.get_KNN_statistical_analysis)
Get_Statistical_Analysis_Of_Dataset(df, columns, rfc.get_RFC_statistical_analysis)
    