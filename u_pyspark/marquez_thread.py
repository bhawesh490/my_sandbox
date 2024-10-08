from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import col
from concurrent.futures import ThreadPoolExecutor
import random
import string


def generate_random_name(length=8):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_spark_session(app, namespace):
    conf = (
        SparkConf()
        .setAppName(app)
        .setMaster("local[2]")
        .set("spark.jars.packages", "io.openlineage:openlineage-spark:1.8.0")
        .set("spark.openlineage.transport.url", "http://localhost:3000")
        .set("spark.openlineage.transport.type", "http")
        .set("spark.openlineage.namespace", namespace)
    )
    return SparkSession.builder.config(conf=conf).getOrCreate()


def process_data(file_path, output_path):
    random_name = generate_random_name()

    spark = create_spark_session(
        random_name, random_name
    )  # Create a new Spark session for each thread
    try:
        df = (
            spark.read.format("csv")
            .option("header", "true")
            .option("delimiter", "\t")
            .load(file_path)
        )
        print("DataFrame columns:", df.columns)
        df_transformed = df.withColumn("new_company", col("Company"))
        df_transformed.write.format("csv").mode("overwrite").save(output_path)
        print(f"Processed and saved: {output_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    finally:
        spark.stop()  # Ensure the Spark session is stopped


# Define file paths and output paths
file_paths = ["input_files/table1/name=hello_v1/", "input_files/table1/name=bhawesh/"]
output_paths = ["output_files/joined_table/df1/", "output_files/joined_table/df2/"]

# Use ThreadPoolExecutor to run tasks in parallel
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(process_data, file_paths, output_paths)
