import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import boto3
import json

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

client = boto3.client("secretsmanager", region_name="eu-west-1")

get_secret_value_response = client.get_secret_value(SecretId="sap_hana")

secret = get_secret_value_response["SecretString"]
secret = json.loads(secret)

db_username = secret.get("db_username")
db_password = secret.get("db_password")
db_url = secret.get("db_url")
jdbc_driver_name = secret.get("driver_name")
table_name = '"INTELDS_POC"."2VS_I_ORDER"'
print(table_name)

options = {
    "driver": jdbc_driver_name,
    "url": db_url,
    "dbtable": table_name,
    "user": db_username,
    "password": db_password,
}

df = glueContext.read.format("jdbc").options(**options).load()
distinct_values = df.select("OrderCategory").distinct()
print(distinct_values.show())
print("Schema is", df.printSchema())
bounds = df.selectExpr(
    "min(OrderID) as lower_bound", "max(OrderID) as upper_bound"
).collect()[0]
print(bounds)
print("Count is")
print(df.count())
print("Number of partitions: ", df.rdd.getNumPartitions())
print(df.show(8))
df.write.format("parquet").mode("append").save("s3://bhawesh-test-101/vs_i_order/")
