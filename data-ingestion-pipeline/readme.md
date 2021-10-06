# TBA
### Data source and description
E-commerce data from an UK retailer (availbale on Kaggle [here](https://www.kaggle.com/carrie1/ecommerce-data)) was used for this project.
CSV data was transfromed to json string in the Client and sent to API Gateway.

Simple API Gateway that has two methods (POST AND GET) with Lambda integration was created.
1. POST: writes data to Kinesis Stream
2. GET: gets item from DynamoDB

Kinesis stream was created in the console.
Lambda function is [here](https://github.com/ksenia-tabakova/AWS-pipelines-project/blob/main/data-ingestion-pipeline/lambda_function.py)
