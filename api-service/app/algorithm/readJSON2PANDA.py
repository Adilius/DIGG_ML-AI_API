
#Project created: 2021-09-13
#Developer: Björn Norén

# Information: This application reads a JSON-file and returns all the datatypes within the JSON-file

import json
import requests
import pandas as pd

# returns JSON object as 
# a dictionary
def check_if_dict_has_keyword_named_results(dict_dataset):
    if type(dict_dataset) == dict:
        for k in dict_dataset.keys(): #check for the keys
            s = str(k) #convert content to string
            if s == "results":
                dict_dataset = look_for_dicts(dict_dataset)
    return dict_dataset

def look_for_dicts(data):
    whereresults= ""
    next = 0
    if type(data) == dict:
        for k in data.keys(): #check for the keys
            s = str(k) #convert content to string
            print(type(data[s])) #check if it is a string the data
            if s == "next":
                next = 1
            if type(data[s]) == list: #check if its a list wich means it is the "data" to analice
        #         df= pd.DataFrame() #define general dataframe
        #         firstIterance = 1
                if s == "results":
                    whereresults = s
    superez= pd.DataFrame.from_dict(data[s])
    counter = 0
    while next==1:
        foundnext=0
        response = requests.get(data["next"]) #get if url correct
        # if response is valid 
        data = {}
        if (response.status_code == 200):
             data = response.json() #we conver data to json type(dict)
        else:
            next=0
            print("next labels contains a invalid link...")
        for labels in data.keys():
            s = str(labels) #convert content to string
            if foundnext == 0:
                if s == "next":
                        next = 1
                        foundnext = 1
                else:
                        next = 0
            if type(data[s]) == list:
                if s == "results":
                    tempDF=pd.DataFrame.from_dict(data[s])
                    #print(tempDF)
        datas=[superez, tempDF]
        superez = pd.concat(datas,ignore_index=True)
        counter= counter + 1
        print(counter)
        print(superez)
        #merge dataframes tempDF with superez
    
    #print(superez)
    return superez
###################################################################
##def look_for_dicts(data):  V.1.0#################################
################################################################### 
        #         print(".-.-.-.-.-.-.-.-.-.-.-.----------------------------------------------.-.-.-.-.-.-.-.-.-")
        #         print(superez)
        #         for item in data[s]: #for every item on the list:

        #            tempList = []  #list for the columns of the dict
        #            tempList2 = []  #list for the columns of the dict
        #            print(type(item))  #print type of item(should be a dict)
        #            if firstIterance == 1:
        #                if type(item) == dict: #if its a dict: check if we are in results
        #                      if s == "results":
        #                         for info in item.keys(): #we read every item on the dicts with data
        #                             print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"+ str(info))
        #                             tempList.append(str(info))
        #                             print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"+ item[str(info)])
        #                             try:
        #                                tempList2.append(float(item[str(info)]))
        #                             except:
        #                                    tempList2.append(item[str(info)])
        #                print("this is templist--------------------------") 
        #                print(tempList)
        #                df = pd.DataFrame(columns=tempList)
        #                print(df)
        #                print("this is templis2--------------------------") 
        #                print(tempList2)
        #                print("-----------------------------------------------------------------------") 

        #                df = pd.concat([df,pd.DataFrame(tempList2)])
        #                firstIterance=0
        #                print(df)

        #            else:
        #                if type(item) == dict: #if its a dict: check if we are in results
        #                      if s == "results":
        #                          for info in item.keys(): #we read every item on the dicts with data      
        #                           try:
        #                               tempList2.append(float(item[str(info)]))
        #                           except:
        #                                 tempList2.append(item[str(info)])
        #                print("this is templis2--------------------------") 
        #                print(tempList2)
        #                df = pd.concat([df,pd.DataFrame(tempList2)])
        #                print(df)
                  
        #    if type(data[s]) == dict:
        #        look_for_dicts(data[s])
        #print(df)
########################################################################################################################
########################################################################################################################



########################################################################################################################
def look_for_dicts_from_api():
    df = pd.DataFrame()
    # example api from dataportal.se : https://konsumentverket.entryscape.net/rowstore/dataset/86ce5095-1641-4390-8987-bdc3c77625a7
    url = "https://konsumentverket.entryscape.net/rowstore/dataset/86ce5095-1641-4390-8987-bdc3c77625a7"
    #url = input("enter url for API: ") #write url
    response = requests.get(url) #get if url correct

    # if response is valid 
    if (response.status_code == 200):
        data = response.json() #we conver data to json type(dict)
        if (type(data) == dict): #check if it is rlly a dict
            df = look_for_dicts(data)
        
        print("F")


#######################################################################################################################
def hello_world():
    return {"Hello":"world"}

look_for_dicts_from_api()
