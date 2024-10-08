# import spark session
from pyspark.sql import SparkSession
from pyspark import SparkConf

conf = SparkConf().setAppName("First App").setMaster("local[*]")
spark = SparkSession.builder.config(conf=conf).getOrCreate()
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
df.write.format("csv").partitionBy("order_status").mode("overwrite").option(
    "header", "true"
).option("path", "output_files/14_orders").save()
# you will notice that order_status column is not there in csv file
df_read = (
    spark.read.format("csv")
    .option("delimiter", ",")
    .option("header", "true")
    .load("output_files/14_orders/order_status=COMPLETE")
)
print(
    "Schema of the read data"
)  # since we have stored the data in 5 partitions it has read in 8 partitions since partition by created 8 folders
print("No of partitions in read data...")
print(df_read.rdd.getNumPartitions())
print(df_read.printSchema())
df_read.show()
