from pyspark import SparkContext

sc = SparkContext("local[*]", "Second App")

sc.setLogLevel("ERROR")

initial_rdd = sc.textFile("2_file.csv")
print(initial_rdd.getNumPartitions())
# print(initial_rdd.collect())
mapped_input = initial_rdd.map(lambda x: (float(x.split(",")[10]), x.split(",")[0]))
print(mapped_input.take(5))
flat_mapped_input = mapped_input.flatMapValues(lambda x: x.split(" "))
print(flat_mapped_input.take(5))
final_mapped = flat_mapped_input.map(lambda x: (x[1].lower(), x[0]))
final_output = final_mapped.reduceByKey(lambda a, b: a + b)
print(final_output.take(5))
print(final_output.getNumPartitions())
total = final_output.sortBy(lambda x: x[1], ascending=False)  # sort by value
new_total = total.collect()
# total is a local variable in single machine
for i in new_total:
    print(i)
