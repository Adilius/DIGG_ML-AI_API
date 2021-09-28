import pandas as pd
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd

#   Date      : 2021-09-24
#   Developer : Björn Norén
#   What      : The program takes in a CSV file and analyzes it through Desicion Tree Classifier. 
#             : 70% of the dataset will be used for training data and 30% is test data
#             : As it is difficult to know which column you would like to test, the program will
#             :  iterate each column as a target class and then present the correlation to
#             :  the other columns



# Läs in dataset
df = pd.read_csv("Datasets/breast_cancer.csv") 

# Print first 5 rows to the user
print(df.head())

def Analyse_Dataset(df):

    columns = []

    # Add columns to a list of columns
    for col in df.columns:
        columns.append(col)

    # Preprocess dataset so it becomes workable for ML
    le = preprocessing.LabelEncoder()
    df = df.apply(le.fit_transform)

    num = len(columns) # num the number of columns
    i = 0
    feature_cols = [] # Feature_cols are the other columns in addition to the temporary Target Class

    # Iterera varje kolumn
    while i < num:
        for val in columns:
            feature_cols.append(val)

        cur_column = columns[i] # Define the current Target Class
        feature_cols.pop(i)     # The current Target Class should not be part of feature-cols
        
        Decision_Tree_Classifier(df, columns, feature_cols, cur_column, i)

        feature_cols = []
        i += 1


def Decision_Tree_Classifier(df, columns, feature_cols, cur_column, i):

    X = df[feature_cols]
    Y = df.iloc[:, i]

    # Split dataset into training set and test set
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(max_depth = 10)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,Y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(Y_test, y_pred))


Analyse_Dataset(df)