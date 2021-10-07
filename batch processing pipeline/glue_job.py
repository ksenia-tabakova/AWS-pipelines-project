import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "glue-transactionsdb", table_name = "mybulkimport", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "glue-transactionsdb", table_name = "mybulkimport", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("invoiceno", "string", "invoiceno", "string"), ("stockcode", "string", "stockcode", "string"), ("description", "string", "description", "string"), ("quantity", "long", "quantity", "int"), ("invoicedate", "string", "invoicedate", "string"), ("unitprice", "double", "unitprice", "double"), ("customerid", "long", "customerid", "int"), ("country", "string", "country", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("invoiceno", "string", "invoiceno", "string"), ("stockcode", "string", "stockcode", "string"), ("description", "string", "description", "string"), ("quantity", "long", "quantity", "int"), ("invoicedate", "string", "invoicedate", "string"), ("unitprice", "double", "unitprice", "double"), ("customerid", "long", "customerid", "int"), ("country", "string", "country", "string")], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["country", "quantity", "customerid", "description", "invoiceno", "unitprice", "invoicedate", "stockcode"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["country", "quantity", "customerid", "description", "invoiceno", "unitprice", "invoicedate", "stockcode"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "glue-transactionsdb", table_name = "dev_public_bulkimport", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "glue-transactionsdb", table_name = "dev_public_bulkimport", transformation_ctx = "resolvechoice3")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice4"]
## @return: resolvechoice4
## @inputs: [frame = resolvechoice3]
resolvechoice4 = ResolveChoice.apply(frame = resolvechoice3, choice = "make_cols", transformation_ctx = "resolvechoice4")
## @type: DataSink
## @args: [database = "glue-transactionsdb", table_name = "dev_public_bulkimport", redshift_tmp_dir = TempDir, transformation_ctx = "datasink5"]
## @return: datasink5
## @inputs: [frame = resolvechoice4]
datasink5 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice4, database = "glue-transactionsdb", table_name = "dev_public_bulkimport", redshift_tmp_dir = args["TempDir"], transformation_ctx = "datasink5")
job.commit()