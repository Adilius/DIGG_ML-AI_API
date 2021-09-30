#   Date      : 2021-09-30
#   Developer : Björn Norén
#   What      : The program evaluates a dataset based on the ML_Algorithm KNN Classifier.
#   Functions : This app contains two Function. The first function prints the accuracy score for a given
#             : target label and the other function returns the score 
#             : - KNN_Classifier()
#             : - get_KNN_statistical_analysis()

import pandas as pd
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split  # Import train_test_split function
from   sklearn.preprocessing import StandardScaler
from   sklearn.neighbors     import KNeighborsClassifier
from   sklearn.metrics       import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd

def KNN_Classifier(df, columns, feature_cols, cur_column, i):

    X = df[feature_cols]
    Y = df.iloc[:, i]

    ## Split dataset into training set and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test

    #########################################
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    classifier = KNeighborsClassifier(n_neighbors=len(columns))
    classifier.fit(X_train, Y_train)
    y_pred = classifier.predict(X_test)

    print("Lable: ", cur_column, end = '')

    j = 0
    num = len(cur_column)
    num = 30 - num
    if (num > 0):
        while j < 30 - len(cur_column):
           print(" ", end = '')
           j = j + 1

    # Model Accuracy, how often is the classifier correct?
    print(" Accuracy: ", metrics.accuracy_score(Y_test, y_pred))

    #print(confusion_matrix(Y_test, y_pred))
    #print(classification_report(Y_test, y_pred))
    #########################################


def get_KNN_statistical_analysis(df, columns, feature_cols, cur_column, i):
    X = df[feature_cols]
    Y = df.iloc[:, i]

    # Split dataset into training set and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test

    #########################################
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    classifier = KNeighborsClassifier(n_neighbors=len(columns))
    classifier.fit(X_train, Y_train)
    y_pred = classifier.predict(X_test)

    # print(confusion_matrix(Y_test, y_pred))
    # print(classification_report(Y_test, y_pred))
    #########################################

    # Return Model Accuracy, how often is the classifier correct?
    return metrics.accuracy_score(Y_test, y_pred)
