from pyspark import SparkContext, SparkConf

# Initialise Spark
conf = SparkConf().setAppName("First App").setMaster("local[*]")
# .setMaster("local[*]") means run Spark locally in my machine not in aws cluster with as many cores(cpu cores) as logical cores on your machine.
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
print(sc)
print(
    sc.defaultParallelism
)  # to check how many cores are running.Means if have a data we will have 8 partitions
