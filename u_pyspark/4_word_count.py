# The basic unit which holds the data in spark in rdd
from pyspark import SparkContext, SparkConf
from sys import stdin

# Initialise Spark
conf = SparkConf().setAppName("First App").setMaster("local[*]")
# .setMaster("local[*]") means run Spark locally with as many worker threads as logical cores on your machine.
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
# print(sc)
print(
    sc.defaultParallelism
)  # to check how many cores are running.Means if have a data we will have 8 partitions
# sc is the entry point of spark cluster
# There are 2 ways to create rdd
# 1-Parallelising an existing collection in driver program
# 2-Referencing a dataset in an external storage system like hdfs, hbase, shared file system

rdd = sc.textFile("input_files/4_word_count.txt", minPartitions=8)  # Transformation
print(rdd.collect())  # Action Job0
# print(rdd.getNumPartitions())  # Action
print(rdd.glom().collect())  # Action
rdd1 = rdd.flatMap(lambda x: x.split(" "))  # Transformation
rdd2 = rdd1.map(lambda x: (x, 1))
rdd3 = rdd2.reduceByKey(lambda a, b: a + b)
# print(rdd3.collect()) collect is not preferred instead us saveAsTextFile
# lets check partitions before saving
print(rdd3.getNumPartitions())
rdd3.saveAsTextFile("output_files/4_word_count/")  # path should not exist before hand


# stdin.readline()  # to keep the console open
