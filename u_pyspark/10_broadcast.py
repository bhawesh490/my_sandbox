from pyspark import SparkContext, SparkConf
from sys import stdin

# Initialise Spark
conf = SparkConf().setAppName("First App").setMaster("local[*]")
# .setMaster("local[*]") means run Spark locally with as many worker
# threads as logical cores on your machine.
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
# print(sc)
print(f"Default Partition is : {sc.defaultParallelism}")  # to check how many cores


def load_boarding_words():
    boring_words = set(line.strip() for line in open("input_files/10_broadcast.txt"))
    return boring_words


print(load_boarding_words())
name_set = sc.broadcast(load_boarding_words())
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
rdd5 = rdd4.filter(lambda x: x[0] not in name_set.value)
print(rdd5.take(3))
