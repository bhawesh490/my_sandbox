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

# we have a small file called boring data
# we will braodcast this file to all the machines

rdd = sc.textFile("input_files/9_flatmapvalues.csv")  # Transformation
print(rdd.getNumPartitions())
print(rdd.take(3))
rdd1 = rdd.map(lambda x: x.split("\t"))
rdd2 = rdd1.map(lambda x: (float(x[10]), x[0]))
print(rdd2.take(3))
rdd3 = rdd2.flatMapValues(lambda x: x.split(" "))
print(rdd3.take(3))
rdd4 = rdd3.map(lambda x: (x[1].lower(), x[0]))
print(rdd4.take(3))
rdd5 = rdd4.reduceByKey(lambda a, b: a + b)
print(rdd5.take(3))
rdd6 = rdd5.sortBy(lambda x: x[1], False)
print(rdd6.take(3))
