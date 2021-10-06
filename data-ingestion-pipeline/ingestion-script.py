# Load needed libraries 
import pandas as pd
import requests


#URL of the endpoint
URL = 'https://8t80y7cwrc.execute-api.us-east-1.amazonaws.com/beta/test'

data = pd.read_csv('./sample1000rows.csv', sep=',')
#data = pd.read_csv('./testsample.csv', sep=',')
for i in data.index: #For every row in the file
    try:
        #convert csv to json
        export = data.iloc[i].to_json()
        #send it to api
        response = requests.post(URL, data=export)
        print(export)
        print(response)
    except:
        print(data.loc[i])
