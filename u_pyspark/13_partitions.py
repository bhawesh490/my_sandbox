# import spark session
from pyspark.sql import SparkSession
from pyspark import SparkConf
from sys import stdin

conf = SparkConf().setAppName("First App").setMaster("local[2]")
spark = SparkSession.builder.config(conf=conf).getOrCreate()

max_partition_bytes = spark.conf.get("spark.sql.files.maxPartitionBytes").rstrip("b")
open_cost_in_bytes = spark.conf.get("spark.sql.files.openCostInBytes").rstrip("b")

print(f"Max partition size: {int(max_partition_bytes) / (1024 * 1024)} MB")
print(f"Open cost in bytes: {int(open_cost_in_bytes) / (1024 * 1024)} MB")

# df = (
#     spark.read.format("csv")
#     .option("header", "true")
#     .option("delimiter", "\t")
#     .load("input_files/13_orders.csv")
# )
print("No of partitions are")
# print(df.rdd.getNumPartitions())
# print(spark.sparkContext.defaultParallelism)
print(spark.sparkContext.defaultMinPartitions)
# print(df.printSchema())
# df = df.repartition(5)
# df.write.format("csv").mode("append").option("header", "true").option(
#     "path", "output_files/13_orders"
# ).save()

df_read = (
    spark.read.format("csv")
    .option("delimiter", ",")
    .option("header", "true")
    .load("output_files/13_orders/")
)
print(df_read.show())
# print(
# "Schema of the read data"
# )  # since we have stored the data in 5 partitions it has read in 8 partitions since partition by created 8 folders
print("No of partitions in read data...")
print(df_read.rdd.getNumPartitions())
new_df = df_read.repartition(16)
print(new_df.rdd.getNumPartitions())
print(new_df.count())
# df_read.write.format("csv").mode("append").option("header", "true").option(
# "path", "output_files/13_orders_test"
# ).save()


# print(df_read.printSchema())
stdin.readline()  # to keep the console open workaround to see the dag
