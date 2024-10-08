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

rdd = sc.textFile("input_files/6_sort_basics.csv")  # Transformation
# print(rdd.getNumPartitions())
# print(rdd.take(3))
rdd1 = rdd.map(lambda x: x.split("\t"))  # Transformation
rdd2 = rdd1.map(lambda x: (x[0], float(x[2])))
# print(rdd2.take(3))
# print(rdd2.getNumPartitions())
rdd3 = rdd2.reduceByKey(lambda a, b: a + b)  # Transformation
# rdd4 = rdd3.sortBy(lambda x: x[1], ascending=False)
# print(rdd4.take(3))
rdd3.collect()
stdin.readline()  # to keep the console open workaround to see the dag
