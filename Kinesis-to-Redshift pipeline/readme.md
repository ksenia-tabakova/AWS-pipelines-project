## Redshift
1. Redshift database were configred in console
2. Table was creted using query (code [here](https://github.com/ksenia-tabakova/AWS-pipelines-project/blob/main/Kinesis-to-Redshift%20pipeline/create_table_query.txt))
3. VPC routing for firehose set up
4. Amazon Kinesis data Firehose configured and connected to the Redshift database in the console
6. Connected to Redshift through the temporary S3 bucket. [jsonpaths.json](https://github.com/ksenia-tabakova/AWS-pipelines-project/blob/main/Kinesis-to-Redshift%20pipeline/jsonpaths.json) file was placed beforehand in the bucket - it tells Firehose what is the structure of the records coming in.
