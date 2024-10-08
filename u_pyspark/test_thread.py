# import threading
# from pyspark.sql import SparkSession
# from pyspark import SparkConf


# def streaming_job():
#     print(f"Running in thread: {threading.current_thread().name}")

#     # set shuffle partitions to 5
#     conf = (
#         SparkConf()
#         .setAppName("streaming application")
#         .setMaster("local[*]")
#         .set("spark.sql.shuffle.partitions", "3")
#         .set("spark.streaming.stopGracefullyOnShutdown", "true")
#         .set(
#             "spark.sql.streaming.schemaInference", "true"
#         )  # for json we have to infer the schema
#     )
#     # streaming stop gracefully on shutdown means that if we stop the streaming application it will stop gracefully
#     spark = SparkSession.builder.config(conf=conf).getOrCreate()
#     # set logger to error level only
#     spark.sparkContext.setLogLevel("ERROR")

#     # 1 read from the stream
#     ordersdf = (
#         spark.readStream.format("json")
#         .option("path", "input_files/streaming_files/")
#         .option("maxFilesPerTrigger", 1)
#         .load()
#     )

#     ordersdf.printSchema()
#     # it will process one file in first micro batch
#     # it will wait for 30 seconds and then process the next file
#     # then it will wait for 30 seconds and then process the next file
#     # 2 process all the orders that are completed
#     # print("Counting the number of orders")
#     # print(ordersdf.count())

#     ordersdf.createOrReplaceTempView("orders")
#     completed_orders = spark.sql("select * from orders where order_status='COMPLETE'")

#     def process_batch(df, epoch_id):
#         print(f"Running in thread: {threading.current_thread().name}")
#         df.show()
#         print("Counting the number of orders")
#         print(df.count())
#         df.write.format("json").mode("append").save("output_files/streaming_files/")

#     # 2 write it back to the sink
#     orders_query = (
#         completed_orders.writeStream.foreachBatch(process_batch)
#         .outputMode(
#             "append"
#         )  # does not support complete and update mode for this data source
#         .option("checkpointLocation", "checkpoint-location")
#         .trigger(processingTime="30 seconds")
#         .start()
#     )

#     orders_query.awaitTermination()
#     # means do not terminate the program until we terminate this


# # Create a thread to run the streaming job
# streaming_thread = threading.Thread(target=streaming_job, name="StreamingThread")
# streaming_thread.start()

# # Wait for the streaming thread to finish
# streaming_thread.join()

import threading, time
from pyspark.sql import SparkSession
from pyspark import SparkConf
from sys import stdin


def print_active_threads():
    print("Active threads:", [thread.name for thread in threading.enumerate()])


def streaming_job():
    print(f"Running streaming job in thread: {threading.current_thread().name}")

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
    # Check if running on driver node or worker node
    if spark.sparkContext.isLocal:
        print("Running on the driver node")
    else:
        print("Running on a worker node")

    # 1 read from the stream
    ordersdf = (
        spark.readStream.format("json")
        .option("path", "input_files/streaming_files/")
        .option("maxFilesPerTrigger", 1)
        .load()
    )

    ordersdf.printSchema()
    # it will process one file in first micro batch
    # it will wait for 30 seconds and then process the next file
    # then it will wait for 30 seconds and then process the next file
    # 2 process all the orders that are completed
    # print("Counting the number of orders")
    # print(ordersdf.count())

    ordersdf.createOrReplaceTempView("orders")
    completed_orders = spark.sql("select * from orders where order_status='COMPLETE'")

    def process_batch(df, epoch_id):
        print_active_threads()
        print(f"Running process_batch in thread: {threading.current_thread().name}")
        df.show()
        print(f"Running process_batch in thread: {threading.current_thread().name}")
        print("Counting the number of orders")
        print(df.count())
        df.write.format("json").mode("append").save("output_files/streaming_files/")

    # 2 write it back to the sink
    orders_query = (
        completed_orders.writeStream.foreachBatch(process_batch)
        .outputMode(
            "append"
        )  # does not support complete and update mode for this data source
        .trigger(processingTime="0 seconds")
        .start()
    )

    orders_query.awaitTermination()
    # means do not terminate the program until we terminate this


# Create a thread to run the streaming job
streaming_thread = threading.Thread(target=streaming_job, name="StreamingThread")
streaming_thread.start()

#  Print active threads after starting the streaming thread
print_active_threads()

# Wait for the streaming thread to finish
streaming_thread.join()

# Print active threads after joining the streaming thread
print_active_threads()
stdin.readline()
