from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define the schema
schema = StructType(
    [
        StructField("Index", StringType(), True),
        StructField("Customer_Id", StringType(), True),
        StructField("First_Name", StringType(), True),
        StructField("Last_Name", StringType(), True),
        StructField("Company", StringType(), True),
        StructField("City", StringType(), True),
        StructField("Country", StringType(), True),
        StructField("Email", StringType(), True),
        StructField("Website", StringType(), True),
    ]
)
print(schema)
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
    spark.readStream.format("csv")
    .schema(schema)
    .option("delimiter", "\t")
    .option("header", "true")
    .option(
        "path",
        "/mnt/c/Users/SESA733833/my_sandbox/u_pyspark/input_files/table2/name=bhawesh/,"
        "/mnt/c/Users/SESA733833/my_sandbox/u_pyspark/input_files/table2/name=pallavi/",
    )
    # .option("cleanSource", "archive")
    # .option("sourceArchiveDir", "input_files/archive/table2/")
    # .option("archive", "input_files/table1/archive/")
    .load()
)
# 2 process all the orders that are completed
ordersdf.createOrReplaceTempView("customers")
completed_orders = spark.sql("select * from customers limit 2")


# 2 write it back to the sink
orders_query = (
    completed_orders.writeStream.format("console")
    .outputMode(
        "append"
    )  # does not support complete and update mode for this data source
    # .option("path", "output_files/streaming_files/")
    .option("checkpointLocation", "checkpoint-location_table3")
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
