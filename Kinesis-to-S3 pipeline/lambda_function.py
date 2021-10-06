from __future__ import print_function

import base64
import json
import boto3
from datetime import datetime

#make s3 client
s3_client = boto3.client("s3")

#convert datetime to string
dateTimeObj = datetime.now()

#format the string
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H%M%S")


def lambda_handler(event, context):

    #list for the records
    kinesisRecords = []  
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("Decoded payload: " + payload)
        kinesisRecords.append(payload)
        
    #make a string out of list
    record_string = '\n'.join(kinesisRecords)
    
    #generate name for the file with the timestamp
    mykey = 'output-' + timestampStr + '.txt'
    
    #put the file into S3 bucket
    response = s3_client.put_object(Body=record_string, Bucket="myingestionbucket", Key = mykey)
    return 'Successfully processed {} records.'.format(len(event['Records']))
