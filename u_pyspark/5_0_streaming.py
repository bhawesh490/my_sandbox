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
    df.show()
    print("Counting the number of orders")
    print(df.count())
    df.write.format("json").mode("append").save("output_files/streaming_files/")


# 2 write it back to the sink
orders_query = (
    completed_orders.writeStream.foreachBatch(process_batch)
    .outputMode(
        "append"
    )  # does not support complete and update mode for this data source
    .option("checkpointLocation", "checkpoint-location")
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
# checkpoint file-->sources-->batch wise you can see that files that are read
# here it keeps a track of what all it has read
# over the times the number of files in the directory will keep on increasing.lets say
# we get a new file every two minutes
# if we have a lot of files in the folder then it will keep on becoming difficult or
# time consuming ,becuase spark keep a track what all files it has processed
# so if new files keep on coming and older files grow this tracking mechanism can become
# difficult and time consuming
# that is why it is recommended to cleanup older files as and when required
# we should not accumulate too many old files rather do the cleanup frequently
# options available
# clean source and sourceArchiveDir are often used together
# cleansource takes 2 values archive and delete

# it will delete the files that are processed
# .options("cleanSource", "delete")
# but it will take some time not feasible becuase job will only complete when you process
# and delete the file
# .options("cleanSource", "archive")
# .option("sourceArchiveDir", "Name of archive dir where files will be moved")
# remember going with any of the above will increase the processing time
# if our expected time to process is very quick we should avoid using these options
# in such cases we can have our own batch job schdueled to cleanup the files

# if our older processed files are not removed from the folder that it will adversily affect the performance
