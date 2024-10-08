# import spark session
from pyspark.sql import SparkSession
from pyspark import SparkConf

conf = SparkConf().setAppName("First App").setMaster("local[*]")
spark = SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()
df = (
    spark.read.format("csv")
    .option("delimiter", "\t")
    .option("header", "true")
    .load("input_files/13_orders.csv")
)

print("No of partitions are")
print(df.rdd.getNumPartitions())
print(spark.sparkContext.defaultParallelism)
print(spark.sparkContext.defaultMinPartitions)
print(df.printSchema())
df = df.repartition(5)
spark.sql("CREATE DATABASE IF NOT EXISTS retail_db")
df.write.format("csv").mode("overwrite").saveAsTable("retail_db.orders_table")
print(spark.catalog.listTables("retail_db"))
# you will notice that it has created a folder named has spark-warehouse and inside that it has created a folder named orders_table
# by default it has saved it in default database
