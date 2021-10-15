#   Date      : 2021-10-06
#   Developer : Björn Norén
#   What      : The program shows a heatmap showing the correlation between each column/label
# Using Skicit-learn to split data into training and testing sets

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def Correlation_Classifier(df):

    #print(df.corr(method ='pearson'))
    #heatmap = sns.heatmap(df.corr(method ='pearson'), vmin=-1, vmax=1, annot=True)
    #plt.figure(figsize=(20, 10))
    #plt.show()
    correlation_matrix = df.corr(method ='pearson').values.tolist()
    for item in correlation_matrix:
        for i in item:
            if np.isnan(i):
                return "Data is not suitable for Correlation Classification"
    return correlation_matrix
