import json
import boto3

def lambda_handler(event, context):

    print("MyEvent:")
    print(event)
    try:
        method = event['requestContext']['httpMethod']
    except KeyError:
        method = event['context']['http-method']

        
    if method == "GET":  #This will query DynamoDB Invoices table by InvoiceNo
        dynamo_client = boto3.client('dynamodb')  #client for DynamoDB
        im_InvoiceNo = event['params']['querystring']['InvoiceNo']
        print(im_InvoiceNo)
        response = dynamo_client.get_item(TableName = 'Invoices', Key = {'InvoiceNo':{'N': im_InvoiceNo}})
        print(response['Item'])

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
           }

    elif method == "POST":  #This will wrtie data to Kinesis stream

        incoming_record = event['body']
        recordstring = json.dumps(p_record)

        client = boto3.client('kinesis')  #initate Kinesis client
        response = client.put_record(  #Send data to Kinesis Stream
            StreamName='APIData',
            Data= incoming_record,
            PartitionKey='string'
        )

        return {
            'statusCode': 200,
            'body': json.dumps(incoming_record)
        }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
