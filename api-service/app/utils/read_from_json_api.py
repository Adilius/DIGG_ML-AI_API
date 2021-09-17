import requests
import json

#Test
#Script for reading from different json APIs on dataportal.se
def main():

    #testAPI = 'https://opendata.umea.se/api/v2/catalog/datasets/skyddade-omraden-djur-och-vaxtskyddsomraden-sverigesweden/records'
    #testAPI = 'https://opendata.umea.se/api/v2/catalog/datasets/miljobilar-andel-av-totalt-antal-bilar-i-det-geografiska-omradet-kolada/records'
    testAPI = 'https://opendata.umea.se/api/v2/catalog/datasets/leverantorsfakturor-2017/records'

    responseAPI = requests.get(testAPI)
    #print(responseAPI.status_code)

    data = responseAPI.text
    #print(data)

    parseJson = json.loads(data)
    #print(parseJson['records'])

    result = []
    result.append(parseJson['total_count'])
    i=0

    while i < len(parseJson['records']):
        #Appends fields to list
        result.append(len(parseJson['records'][i]['links']))
        result.append(parseJson['records'][i]['record']['id'])
        result.append(parseJson['records'][i]['record']['timestamp'])
        result.append(parseJson['records'][i]['record']['size'])
        result.append(len(parseJson['records'][i]['record']['fields']))
        i+=1

    #Prints out list
    printOut(result)

def printOut(list):
    
    print('Total count: ' + str(list[0]))
    i=0
    j=1

    while i < len(list)-1:
        print('\nRecord ' + str(j) + ':')
        print('Record links: ' + str(list[i+1]))
        print('Record id: ' + str(list[i+2]))
        print('Record timestamp: ' + str(list[i+3]))
        print('Record size: ' + str(list[i+4]))
        print('Record total fields: ' + str(list[i+5]))
        i+=5
        j+=1

main()