from pyspark.sql import SparkSession
from pyspark import SparkConf

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

# 1 read from the stream
linesdf = (
    spark.readStream.format("socket")
    .option("host", "localhost")
    .option("port", "12345")
    .load()
)
# process
linesdf.printSchema()
words_df = linesdf.selectExpr("explode(split(value,' ')) as word")

count_df = words_df.groupBy("word").count()
# difference b/w select and select expr is that select expr is used to write sql queries
# select is used to select columns

# 2 write it back to the sink
word_count_query = (
    count_df.writeStream.format("console")
    .outputMode("complete")
    .option("checkpointLocation", "checkpoint-location")
    .trigger(processingTime="30 seconds")
    .start()
)

word_count_query.awaitTermination()
# means do not terminate the program until we terminate this

# open a terminal and run the following command
# nc -lk 12345
# type some text and see the output in the console
# to stop the program press ctrl+c
