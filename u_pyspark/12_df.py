# import spark session
from pyspark.sql import SparkSession
from pyspark import SparkConf

# initialise spark session
spark = SparkSession.builder.appName("First App").master("local[2]").getOrCreate()
# write the code here
# treat spark session as entry point to spark cluster and driver
spark.stop()

# initalise spark session using spark conf here we we will attach the name of the app and the master
# initialise spark session
conf = SparkConf().setAppName("First App").setMaster("local[2]")
spark = SparkSession.builder.config(conf=conf).getOrCreate()
