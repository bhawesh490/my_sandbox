from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import from_json, col, get_json_object, input_file_name, lit

# Configure Spark with OpenLineage
# "io.openlineage:openlineage-spark_2.12.18:1.9.1"
# "io.openlineage:openlineage-spark:1.8.0"
conf = (
    SparkConf()
    .setAppName("test-bhawesh-0")
    .setMaster("local[2]")
    .set("spark.jars.packages", "io.openlineage:openlineage-spark:1.8.0")
    .set("spark.extraListeners", "io.openlineage.spark.agent.OpenLineageSparkListener")
    .set("spark.openlineage.transport.url", "http://localhost:3000")
    .set("spark.openlineage.transport.type", "http")
    .set("spark.openlineage.namespace", "bhawesh-3")
    # .set("spark.openlineage.parentJobNamespace", "bhawesh-2")
    # .set("spark.openlineage.parentJobName", "bhawesh-2")
    # .set("spark.openlineage.parentRunId", "bhawesh-2")
)
spark = SparkSession.builder.config(conf=conf).getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
# Read multiple datasets
df1 = (
    spark.read.format("csv")
    .option("header", "true")
    .option("delimiter", "\t")
    .load("input_files/table1/name=hello_v1/")
)

print(df1.columns)
df1_transformed = df1.withColumn("new_company", col("Company"))
df1.show()
# df2.show()
df1.printSchema()
df1_transformed = df1.withColumn("new_company_hello", col("Company"))
df1_transformed.show()

# conf = (
#     SparkConf()
#     .setAppName("test-bhawesh-2")
#     .setMaster("local[2]")
#     .set("spark.jars.packages", "io.openlineage:openlineage-spark:1.8.0")
#     .set("spark.extraListeners", "io.openlineage.spark.agent.OpenLineageSparkListener")
#     .set("spark.openlineage.transport.url", "http://localhost:3000")
#     .set("spark.openlineage.transport.type", "http")
#     .set("spark.openlineage.namespace", "bhawesh_2")
#     .set("spark.openlineage.parentJobNamespace", "bhawesh_2")
#     .set("spark.openlineage.parentJobName", "bhawesh_2")
#     .set("spark.openlineage.parentRunId", "bhawesh_2")
# )

# spark = SparkSession.builder.config(conf=conf).getOrCreate()

spark.conf.set("spark.openlineage.namespace", "bhawesh-2")
spark.conf.set("spark.openlineage.parentJobNamespace", "bhawesh-2")
spark.conf.set("spark.openlineage.parentJobName", "bhawesh-2")
spark.conf.set("spark.openlineage.parentRunId", "bhawesh-2")


df2 = (
    spark.read.format("csv")
    .option("header", "true")
    .option("delimiter", "\t")
    .load("input_files/table1/name=bhawesh/")
)


print(df2.columns)
# Perform transformations
df2_transformed = df2.withColumn("new_company", col("Company"))

df2_transformed.show()

# # Join datasets
# joined_df = df1_transformed.union(df2_transformed)
# # joined_df = df1_transformed.join(df2_transformed, on="Index", how="inner")

# # Write the results to different outputs
# df1_transformed.write.format("csv").mode("overwrite").save(
#     "output_files/table1_transformed/"
# )
# df2_transformed.write.format("csv").mode("overwrite").save(
#     "output_files/table2_transformed/"
# )
# joined_df.write.format("csv").mode("overwrite").save("output_files/joined_table/")

# # Show schemas and sample data
# df1.printSchema()
df2.show()

#
# df2.show(3)
# joined_df.printSchema()
# joined_df.show(3)

df2.write.format("csv").mode("overwrite").save("output_files/joined_table/df2/")

df1.write.format("csv").mode("overwrite").save("output_files/joined_table/df1/")

spark.stop()
