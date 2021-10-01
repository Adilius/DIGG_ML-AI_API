#   Date      : 2021-09-30
#   Developer : Björn Norén
#   What      : The program evaluates a dataset based on the ML_Algorithm Random Forest Classifier.
#   Functions : This app contains two Function. The first function prints the accuracy score for a given
#             : target label and the other function returns the score 
#             : - Random_Forest_Classifier()
#             : - get_DTC_statistical_analysis()

import pandas as pd
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split  # Import train_test_split function
from   sklearn.ensemble      import RandomForestClassifier
from sklearn import preprocessing
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd

def Random_Forest_Classifier(df, columns, feature_cols, cur_column, i):
    X = df[feature_cols]
    Y = df.iloc[:, i]

    # Split dataset into training set and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test

    # Create Decision Tree classifer object
    clf=RandomForestClassifier(n_estimators=1000)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,Y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

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


def get_RFC_statistical_analysis(df, columns, feature_cols, cur_column, i):
    X = df[feature_cols]
    Y = df.iloc[:, i]

    # Split dataset into training set and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test

    # Create Decision Tree classifer object
    clf=RandomForestClassifier(n_estimators=1000)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,Y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Return Model Accuracy, how often is the classifier correct?
    return metrics.accuracy_score(Y_test, y_pred)
