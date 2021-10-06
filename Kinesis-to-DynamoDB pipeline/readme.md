# Kinesis to DynamoDB pipeline
Two tables in DynamoDB were created with console
1. Customers - CustomerID as primary key, InvoiceNo stored in attributes
2. Invoices - InvoiceNo as primary key, invoice data stored in attributes

[Lambda function](https://github.com/ksenia-tabakova/AWS-pipelines-project/blob/main/Kinesis-to-DynamoDB%20pipeline/lambda_function.py) read data from Kinesis and writes it to DynamoSB tables.
