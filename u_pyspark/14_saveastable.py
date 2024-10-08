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

df.write.format("csv").mode("overwrite").saveAsTable("orders_table")
# you will notice that it has created a folder named has spark-warehouse and inside that it has created a folder named orders_table
# by default it has saved it in default database
