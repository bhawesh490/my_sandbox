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

rdd = sc.textFile("input_files/5_word_count.txt")  # Transformation
print(rdd.getNumPartitions())
print(rdd.take(3))
rdd1 = rdd.flatMap(lambda x: x.split(" "))  # Transformation
print(rdd1.take(3))
rdd2 = rdd1.map(lambda x: (x, 1))
rdd3 = rdd2.reduceByKey(lambda a, b: a + b)
# # print(rdd3.collect()) collect is not preferred instead us saveAsTextFile
print(rdd3.take(3))
# # lets check partitions before saving
print(rdd3.getNumPartitions())
# rdd3.saveAsTextFile("output_files/4_word_count/")  # path should not exist before hand

# Note on dag
# localhost:4040
# when we are writing a code in ide  and you run the program the dag is visible only till the TimeoutError
# job is running. as soon as the job terminates or finishes the dag is not visible

# you admin will setup history server where you can see the dag
# but in our case history server is not set
# stdin.readline()  # to keep the console open workaround to see the dag
