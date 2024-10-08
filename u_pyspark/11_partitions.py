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

print(" Minium partitions to maintain", sc.defaultMinPartitions)
# sc is the entry point of spark cluster
# There are 2 ways to create rdd
# 1-Parallelising an existing collection in driver program
# 2-Referencing a dataset in an external storage system like hdfs, hbase, shared file system

# we have a small file called boring data
# we will braodcast this file to all the machines

rdd = sc.textFile("input_files/bigLog.txt")  # Transformation
print(rdd.getNumPartitions())
# You will notice there will be 11 partitions becuase if the file is getting read from local the block size is 32 mb
# and the file size is 350 mb so 350/32 = 11 partitions
# 11 partition would mean 11 tasks will be created and 11 threads will be created
rdd2 = sc.textFile("input_files/9_flatmapvalues.csv")  # Transformation
# since default min partition is 2 so it will maintain miminum 2 partitions
print(rdd2.getNumPartitions())
print(sc.defaultMinPartitions)
