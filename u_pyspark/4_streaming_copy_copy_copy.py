from pyspark.sql import SparkSession
from pyspark import SparkConf

# set shuffle partitions to 5
conf = (
    SparkConf()
    .setAppName("streaming application")
    .setMaster("local[*]")
    .set("spark.sql.shuffle.partitions", "3")
    .set("spark.streaming.stopGracefullyOnShutdown", "true")
    .set(
        "spark.sql.streaming.schemaInference", "true"
    )  # for json we have to infer the schema
)
# streaming stop gracefully on shutdown means that if we stop the streaming application it will stop gracefully
spark = SparkSession.builder.config(conf=conf).getOrCreate()
# set logger to error level only
spark.sparkContext.setLogLevel("ERROR")

# 1 read from the stream
ordersdf = (
    spark.readStream.format("json")
    .option("path", "input_files/table1/name=pallavi/")
    .load()
)
# 2 process all the orders that are completed
ordersdf.createOrReplaceTempView("orders")
completed_orders = spark.sql("select * from orders where order_status='COMPLETE'")


# 2 write it back to the sink
orders_query = (
    completed_orders.writeStream.format("json")
    .outputMode(
        "append"
    )  # does not support complete and update mode for this data source
    .option("path", "output_files/streaming_files/")
    .option("checkpointLocation", "checkpoint-location_table1")
    .trigger(processingTime="30 seconds")
    .start()
)

orders_query.awaitTermination()
# means do not terminate the program until we terminate this

# open a terminal and run the following command
# nc -lk 12345
# type some text and see the output in the console
# to stop the program press ctrl+c

# we have other options also
# 1-in read stream we have options like maxFilesPerTrigger
# go to next file to see it
