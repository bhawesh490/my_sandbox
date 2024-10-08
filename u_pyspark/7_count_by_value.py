# The basic unit which holds the data in spark in rdd
from pyspark import SparkContext, SparkConf
from sys import stdin

# Initialise Spark
conf = SparkConf().setAppName("First App").setMaster("local[*]")
# .setMaster("local[*]") means run Spark locally with as many worker
# threads as logical cores on your machine.
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
# print(sc)
print(
    f"Default Partition is : {sc.defaultParallelism}"
)  # to check how many cores are running.Means if have a data we will have 8 partitions
# sc is the entry point of spark cluster
# There are 2 ways to create rdd
# 1-Parallelising an existing collection in driver program
# 2-Referencing a dataset in an external storage system like hdfs, hbase, shared file system

# user_id movie_id rating_given timestamp
# how many times movies were rated 5 Star
# how many times movies were rated 4 Star
# how many times movies were rated 3 Star
# how many times movies were rated 2 Star
# how many times movies were rated 1 Star


rdd = sc.textFile("input_files/7_count_by_values.txt")  # Transformation
print(rdd.getNumPartitions())
print(rdd.take(3))
rdd1 = rdd.map(lambda x: x.split("\t"))  # Transformation
print(rdd1.take(3))
rdd2 = rdd1.map(lambda x: (x[2], 1))
print(rdd2.take(3))
rdd3 = rdd2.reduceByKey(lambda a, b: a + b)  # Transformation
print(rdd3.glom().collect())
print(rdd3.collect())
#############################################################
# we can use count by value also in above case
# countbyvalue is an action so it will be a local variable not a rdd
print(rdd2.countByValue())
