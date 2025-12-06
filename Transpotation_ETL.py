from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType,StructField,StringType,DoubleType,IntegerType
from functools import reduce
from pyspark.sql import DataFrame
import os

# 1) Spark Session 

# Spark=SparkSession.builder \
# .appname("transpotation paipeline")\
# .getOrCreate()


spark = SparkSession.builder \
    .appName("transportation_pipeline") \
    .getOrCreate()

# 2)  define Schema
driver_schema = StructType([
    StructField("driver_id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("license_no", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("hire_date", StringType(), True),
    StructField("status", StringType(), True),
    StructField("created_at", StringType(), True),
    StructField("updated_at", StringType(), True)
])


routes_schema = StructType([
    StructField("route_id", StringType(), True),
    StructField("route_name", StringType(), True),
    StructField("start_stop", StringType(), True),
    StructField("end_stop", StringType(), True),
    StructField("expected_duration_min", DoubleType(), True),
    StructField("distance_km", DoubleType(), True)
])

trips_schema = StructType([
    StructField("trip_id", StringType(), True),
    StructField("vehicle_id", StringType(), True),
    StructField("driver_id", StringType(), True),
    StructField("route_id", StringType(), True),
    StructField("start_time", StringType(), True),   # parse to timestamp
    StructField("end_time", StringType(), True),
    StructField("start_lat", DoubleType(), True),
    StructField("start_lon", DoubleType(), True),
    StructField("end_lat", DoubleType(), True),
    StructField("end_lon", DoubleType(), True),
    StructField("distance_km", DoubleType(), True),
    StructField("fare", DoubleType(), True),
    StructField("status", StringType(), True),
    StructField("created_at", StringType(), True),
    StructField("updated_at", StringType(), True)
])

vehicles_schema = StructType([
    StructField("vehicle_id", StringType(), True),
    StructField("reg_no", StringType(), True),
    StructField("vehicle_type", StringType(), True),
    StructField("capacity", IntegerType(), True),
    StructField("purchase_date", StringType(), True),
    StructField("status", StringType(), True),
    StructField("created_at", StringType(), True),
    StructField("updated_at", StringType(), True)
])


# 3) read file 

drivers=spark.read.csv("E:\Data File\Project 2\drivers.csv",header=True, inferSchema=True)
drivers.show ( 10)
routes=spark.read.csv("E:/Data File/Project 2/routes.csv",header=True, inferSchema=True)
routes.show(10)
trips=spark.read.csv("E:/Data File/Project 2/trips.csv",header=True, inferSchema=True)
trips.show(10)
vehicles=spark.read.csv("E:/Data File/Project 2/vehicles.csv",header=True, inferSchema=True)
vehicles.show(10)


## 4) Parse timestamps and dates

trips_df=trips\
    .withColumn("start_time_ts", to.timestamp(col("start_time"),"yyyy-MM-dd HH:mm:ss"))\
    .withcolum("end_time_ts", to_timestamp(col("end_time_ts"),"yyyy-MM-dd HH:mm:ss"))\
    .withcolum("trip_date",to_date(col("start_time_ts")))


driver_df=driver.withcolumn("hire_date",to.timestamp(col(hire_date),"yyyy-MM-dd"))
vehicles_df=vehicles.withColumn("purchase_date",to.timestamp(col("purchase_date"),"yyyy-MM-dd"))


