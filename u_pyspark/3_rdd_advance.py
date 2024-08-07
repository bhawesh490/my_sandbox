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
random_list1 = random.sample(range(0, 40), 10)
rdd1 = sc.parallelize(random_list, 4)
print(rdd1.collect())  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# union() Transformation but partions will increase as rdd 1 has 4 partitions and rdd has 4 partitions
rdd2 = sc.parallelize(random_list1, 4)
print(rdd2.collect())
rdd_union = rdd1.union(rdd2)
print(rdd_union.glom().collect())

# intersection Transformation
print("# Intersection Transformation #")
rdd_intersection = rdd1.intersection(rdd2)
print(rdd_intersection.glom().collect())

# coalesce Transformation #Decrease no of partitions
rdd_intersection = rdd_intersection.coalesce(1)
print(rdd_intersection.glom().collect())

# take sample recommended instead of collect
print(rdd1.takeSample(False, 5))  # False means no replacement

# take ordered
print(rdd1.takeOrdered(5))
# Note:Before running any actions check the count if count is less than use action

# reduce Action
print(rdd1.reduce(lambda a, b: a + b))
# reduce by key Transformation remember reduce is an action.action are like print statements
rdd_with_key = sc.parallelize([(1, 2), (3, 4), (3, 6), (4, 5)], 2)
print(rdd_with_key.collect())
print(rdd_with_key.glom().collect())
rdd_reduce_by_key = rdd_with_key.reduceByKey(lambda a, b: a + b)
print(rdd_reduce_by_key.getNumPartitions())
print(rdd_reduce_by_key.collect())

# sortbykey Transformation
print("# SortByKey Transformation #")
rdd_sorted = rdd_with_key.sortByKey(ascending=False)
print(rdd_sorted.collect())

# countbykey
print(rdd_with_key.countByKey())
# groupbykey is similar to reduceby key but it will not reduce the values ,it will collect everything in driver node
# group by key is a transformation
rdd_group = rdd_with_key.groupByKey()
print(rdd_group.collect())
x = [list(i[1]) for i in rdd_group.collect()]
print(x)
