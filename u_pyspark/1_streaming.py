from pyspark.sql import SparkSession
from pyspark import SparkConf

conf = SparkConf().setAppName("streaming application").setMaster("local[*]")
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
    .start()
)

word_count_query.awaitTermination()
# means do not terminate the program until we terminate this

# open a terminal and run the following command
# nc -lk 12345
# type some text and see the output in the console
# to stop the program press ctrl+c

# Notes
# 1-200 partitions are created by default in spark after the shuffle has happened
# 2-for such small data that number is over kill
# 3-this shuffle is happending due to group by operations and after this shuffle 200 partitions are created
# 4-to handle this set conf spark.sql.shuffle.partitions=5
# 5-checkout to 2_streaming.py for these updates
