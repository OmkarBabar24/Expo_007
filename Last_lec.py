from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Optimization').getOrCreate()
# RDD approach (not recommended)
rdd = spark.sparkContext.parallelize([(1, 'A'), (2, 'B')])
# df = rdd.toDF(['id', 'name']).show()
# DataFrame approach (recommended)
df = spark.createDataFrame([(1, 'A'), (2, 'B')], ['id', 'name'])
# df.show()


# 2. Cache and Persist
# Cache frequently used DataFrames to avoid recomputation.
# df = spark.read.parquet(r"E:\Data File\weather.parquet",header=True,inferSchema=True).show() # Triggers caching
# df = spark.read.parquet('data.parquet')
# df.cache()
# df.count() # Triggers caching


# 3. Optimize Joins
# Use broadcast joins when one dataset is small.
# from pyspark.sql.functions import broadcast large_df = spark.read.parquet('large_dataset.parquet')
# small_df = spark.read.parquet('small_lookup.parquet') joined_df =
# large_df.join(broadcast(small_df), 'id') joined_df.show()
# from pyspark.sql.functions import broadcast
# large_df = spark.read.parquet('large_dataset.parquet')
# small_df = spark.read.parquet('small_lookup.parquet')
# joined_df = large_df.join(broadcast(small_df), 'id')
# joined_df.show()


# 4. Repartition and Coalesce
# Balance partitions for efficient parallelism.
# Increase partitions df = df.repartition(10) # Reduce partitions (narrow transformation) df =
# df.coalesce(2)
# # Increase partitions
# df = df.repartition(10)
# # Reduce partitions (narrow transformation)
# df = df.coalesce(2)


# 5. Predicate Pushdown
# Read only required data from source files.
# df = spark.read.parquet('data.parquet').filter("age > 30")
# df = spark.read.parquet('data.parquet').filter("age > 30")



# 6. Use Efficient File Formats
# Prefer columnar formats like Parquet or ORC.
# df.write.mode('overwrite').parquet('optimized_data.parquet')


# df.write.partitionBy("region").mode("overwrite").parquet("output/sales_data")
# df_repart = df.repartition(4)



# 7. Avoid UDFs When Possible
# Use built-in functions for better performance.
# from pyspark.sql.functions import col, upper # Avoid this from pyspark.sql.functions import udf from
# pyspark.sql.types import StringType to_upper = udf(lambda s: s.upper(), StringType()) df =
# df.withColumn('name', to_upper(col('name'))) # Use built-in df = df.withColumn('name',
# upper(col('name')))
# from pyspark.sql.functions import col, upper
# # Avoid this
# from pyspark.sql.functions import udf
# from pyspark.sql.types import StringType
# to_upper = udf(lambda s: s.upper(), StringType())
# df = df.withColumn('name', to_upper(col('name')))
# # Use built-in
# df = df.withColumn('name', upper(col('name')))




# 8. Tune Spark Configuration
# Adjust Spark parameters for better performance.
# spark.conf.set("spark.sql.shuffle.partitions", 100) spark.conf.set("spark.executor.memory", "4g")




# 9. Optimize Shuffles
# Minimize wide transformations and use aggregations wisely.
# # Avoid groupByKey result = df.groupBy('category').count() # Better: use reduceByKey or
# aggregateByKey in RDDs if needed
# # Avoid groupByKey
# result = df.groupBy('category').count()
# # Better: use reduceByKey or aggregateByKey in RDDs if needed




# 10. Broadcast Variables
# Share small static data across executors efficiently.
# lookup = {'A': 1, 'B': 2} broadcastVar = spark.sparkContext.broadcast(lookup) df =
# df.rdd.map(lambda x: (x[0], broadcastVar.value.get(x[1], 0))).toDF(['id', 'mapped_value'])
# lookup = {'A': 1, 'B': 2}
# broadcastVar = spark.sparkContext.broadcast(lookup)
# df = df.rdd.map(lambda x: (x[0], broadcastVar.value.get(x[1], 0))).toDF(['id', 'mapped_value'])




# 11. Column Pruning
# Select only necessary columns.
# df = df.select('id', 'name')
# df = df.select('id', 'name')





# 12. Handle Data Skew
# Use salting or broadcast joins for skewed keys.
# from pyspark.sql.functions import rand, concat_ws df = df.withColumn("skewed_key",
# concat_ws("_", col("key"), (rand()*10).cast("int"))) df.show()
# from pyspark.sql.functions import rand, concat_ws
# df = df.withColumn("skewed_key", concat_ws("_", col("key"), (rand()*10).cast("int")))
# df.show()




# 13. Monitor and Debug
# Use Spark UI to monitor jobs and identify bottlenecks.
# Access Spark UI via web browser (default: localhost:4040)
# Access Spark UI via web browser (default: localhost:4040)



# Partitioning and Bucketing in PySpark


# 1. Partitioning in PySpark
# Partitioning is a way to divide data across multiple nodes or files for parallel processing. It improves
# performance by ensuring data locality and balanced workload across executors.


# Types of Partitioning:
# 1. **Repartitioning** – Increases or changes the number of partitions (wide transformation).
# 2. **Coalesce** – Reduces the number of partitions without a full shuffle (narrow transformation).
# 3. **Custom Partitioning** – You can partition data based on specific columns when writing files.
# Example: Repartition and Coalesce


# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("PartitioningExample").getOrCreate()
# df = spark.read.csv("data.csv", header=True, inferSchema=True)


# # Repartition data into 10 partitions
# df_repart = df.repartition(10)
# # Reduce partitions to 2 using coalesce (faster, narrow transformation)
# df_coalesce = df_repart.coalesce(2)
# print("Number of partitions:", df_coalesce.rdd.getNumPartitions())
# Partitioning While Writing Data
# You can write partitioned data to disk based on one or more columns. This makes queries faster
# when filtering on partitioned columns.
# # Write data partitioned by 'country' column
# df.write.mode("overwrite").partitionBy("country").parquet("output/partitioned_data")
# # Read data (only 'India' partition will be read)
# df_india = spark.read.parquet("output/partitioned_data/country=India")




# 2. Bucketing in PySpark
# Bucketing is used to divide data into a fixed number of buckets based on the hash of a column. It
# helps improve join and aggregation performance by ensuring data with the same key goes into the
# same bucket.
# Bucketing Example:
# # Save bucketed table (works with Hive or Spark SQL tables)
# df.write.bucketBy(8, "customer_id").sortBy("customer_id").saveAsTable("bucketed_customers")
# # Example query on bucketed data
# bucketed_df = spark.sql("SELECT * FROM bucketed_customers WHERE customer_id = 101")
# bucketed_df.show()
# When to Use Partitioning and Bucketing
# - **Use partitioning** when data is queried frequently by a column (like country, date, etc.).
# - **Use bucketing** for optimizing large joins and aggregations when both datasets are bucketed on
# the same key.
# - Combine both for best performance in analytical workloads.
# Key Differences Between Partitioning and Bucketing
# | Feature | Partitioning | Bucketing | |----------|---------------|-----------| | Data division | Based on column
# values | Based on hash of column values | | Number of partitions | Dynamic | Fixed number of
# buckets | | Storage structure | Creates separate folders | Stored in single folder with multiple files | |
# Best for | Filtering queries | Joins and aggregations |