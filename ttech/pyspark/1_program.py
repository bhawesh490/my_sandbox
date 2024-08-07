from pyspark import SparkContext
from sys import stdin

sc = SparkContext("local[*]", "First App")
# Local[*] means run Spark locally with as many worker threads as logical cores on your machine.
sc.setLogLevel("ERROR")

input = sc.textFile("file1.csv")
print(input.getNumPartitions())
words = input.flatMap(lambda x: x.split())
words_count = words.map(lambda x: (x, 1))
final_count = words_count.reduceByKey(lambda a, b: a + b)
final_count.saveAsTextFile("output")

results = final_count.collect()


# results will be a local variable now in single machine
for result in results:
    print(result)

stdin.readline()  # to keep the console open
