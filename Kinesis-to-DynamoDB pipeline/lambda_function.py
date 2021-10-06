import json
import base64
import boto3

from datetime import datetime

def lambda_handler(event, context):

    client = boto3.client('dynamodb')  #initalize client for DynamoDB

    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        t_record = base64.b64decode(record['kinesis']['data'])

        # decode the bytes into a string
        str_record = str(t_record,'utf-8')
        print('str_record ', str_record)
        #transform the json string into a dictionary
        dict_record = json.loads(str_record)

        # create Customer Row in DynamoDB
        ############################

        customer_key = dict()
        print('dict_record ', dict_record)
        customer_key.update({'CustomerID': {"N": str(dict_record['CustomerID'])}})


        customer_attributes = dict() 
        customer_attributes.update({str(dict_record['InvoiceNo']): {'Value':{"S":'InvoiceNo'},"Action":"PUT"}})

        response = client.update_item(TableName='Customers', Key = customer_key, AttributeUpdates = customer_attributes)

        # Create Inventory Row
        #############################

        inventory_key = dict()
        inventory_key.update({'InvoiceNo': {"N": str(dict_record['InvoiceNo'])}})

        #create export dictionary
        invoice_attributes = dict()

        #remove Invoice and Stock code from the record
        stock_dict = dict(dict_record)
        stock_dict.pop('InvoiceNo',None)
        stock_dict.pop('StockCode',None)

        #turn the dict into a json
        stock_json = json.dumps(stock_dict)

        #create a record (column) for the InvoiceNo
        #add the stock json to the column with the name of the stock number
        invoice_attributes.update({str(dict_record['StockCode']): {'Value':{"S":stock_json},"Action":"PUT"}})

        #put data to Invoices table on DynamoDB
        response = client.update_item(TableName='Invoices', Key = inventory_key, AttributeUpdates = invoice_attributes)


    return 'Successfully processed {} records.'.format(len(event['Records']))
