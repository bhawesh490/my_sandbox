from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import from_json

# set shuffle partitions to 5
conf = (
    SparkConf()
    .setAppName("streaming application")
    .setMaster("local[*]")
    .set("spark.sql.shuffle.partitions", "3")
    .set("spark.streaming.stopGracefullyOnShutdown", "true")
)
# streaming stop gracefully on shutdown means that if we stop the streaming application it will stop gracefully
spark = SparkSession.builder.config(conf=conf).getOrCreate()
# set logger to error level only
spark.sparkContext.setLogLevel("ERROR")

# 1 read from the stream socket
ordersdf = (
    spark.readStream.format("socket")
    .option("host", "localhost")
    .option("port", "12345")
    .load()
)
# lets define our schema
print(ordersdf.printSchema())
# Note:We can run the spark streaming application at this point also to get the schema of the data
# comment out the below code
# you will notice that you get something called as value in schema
order_schema = StructType(
    [
        StructField("order_id", IntegerType(), True),
        StructField("order_date", StringType(), True),
        StructField("order_customer_id", IntegerType(), True),
        StructField("order_status", StringType(), True),
        StructField("amount", IntegerType(), True),
    ]
)


# 2 process all the orders that are completed
valuedf = ordersdf.select(from_json("value", order_schema).alias("value"))
print(valuedf.printSchema())
value_refinded = valuedf.select("value.*")
print(value_refinded.printSchema())
# ordersdf.createOrReplaceTempView("orders")
# completed_orders = spark.sql(
#     "select count(*) from orders where order_status='COMPLETE'"
# )
agg_window_df = (
    value_refinded.groupBy(F.window("order_date", "15 minute"))
    .agg(sum("amount"))
    .alias("total_amount")
)

agg_window_df = agg_window_df.select("window.start", "window.end", "total_amount")
print(agg_window_df.printSchema())

# 2 write it back to the sink
orders_query = (
    agg_window_df.writeStream.format("console")
    .outputMode("update")
    .option("checkpointLocation", "checkpoint-location")
    .trigger(processingTime="15 seconds")
    .start()
)

orders_query.awaitTermination()
