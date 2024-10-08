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

# our intention in to count the number of blank lines in the file
rdd = sc.textFile("input_files/8_accumulators.txt")  # Transformation
print(rdd.getNumPartitions())
print(rdd.collect())
my_accumulator = sc.accumulator(0)  # long type accumulator


def g(x):
    if x == "":
        my_accumulator.add(1)


rdd.foreach(
    g
)  # for each is available for rdds in pyspark as they are distributed but if it would have been a list it was not available
# for each is a functionality of pyspark not python
print(my_accumulator.value)
