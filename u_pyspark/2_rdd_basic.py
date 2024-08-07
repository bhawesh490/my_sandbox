from pyspark import SparkContext, SparkConf
import random
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

# There are 2 ways to create rdd
# 1-Parallelising an existing collection in driver program
# 2-Referencing a dataset in an external storage system like hdfs, hbase, shared file system

random_list = random.sample(range(0, 40), 10)
print(random_list)
rdd1 = sc.parallelize(random_list)
print(rdd1.getNumPartitions())  # takes default no of partitions as 8
rdd2 = sc.parallelize(random_list, 4)
print(rdd2.getNumPartitions())  # takes 4 partitions
print(
    rdd2.collect()
)  # this will print the list of elements in the rdd at the driver program

# Data Distribution in partitions
print(rdd2.glom().collect())
print(rdd2.glom().take(2))
# in case of glue job having 4 workers and 4 cores(vcpus) each we will have 12 partitions by default
# 1 worker reserved for driver program
# count
print(rdd2.count())
print(rdd2.first())
print(rdd2.top(3))
# avoid using actions as much as possible because it will bring the data to the driver program
# distinct(Transformation)
rdd3 = rdd1.distinct()
print(rdd3.collect())

# Map(Transformations)  In Transformation partition are same
rdd4 = rdd2.map(lambda x: x * 2)
print(rdd4.collect())
print(rdd4.glom().collect())  # partition are same 4

# filter(Transformation) In Transformation partition are same
print("# Filter Transformation #")
rdd5 = rdd2.filter(lambda x: x % 2 == 0)
print(
    rdd5.collect()
)  # spark will remve empty partition using garbage collection technique
print(rdd5.glom().collect())
# Flatmap(Transformation) In Transformation partition are same
# Its Exactly a map its going to collect all values into one single list
print("# FlatMap Transformation #")
rdd6 = rdd2.flatMap(lambda x: [x + 2, x + 4])
print(rdd6.collect())
print(rdd6.glom().collect())
# reduce(Action)
print("# Reduce Action #")
sumation = rdd2.reduce(lambda a, b: a + b)
print(sumation)
# Descriptive Analytics
print("# Descriptive Analytics #")
print(rdd2.max(), rdd2.min(), rdd2.mean(), rdd2.stdev(), rdd2.variance())
# mapPartitions(Transformation) In Transformation partition are same
# here we do transformation against each partition

print("# MapPartitions Transformation #")


def sum_func(partitions):
    _sum = 0
    for item in partitions:
        _sum += item
    yield _sum


print(rdd2.mapPartitions(sum_func).collect())
stdin.readline()  # to keep the console open
