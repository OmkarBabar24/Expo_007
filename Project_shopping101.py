from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from functools import reduce
from pyspark.sql import DataFrame
import os


# 1) Spark Session 
spark = SparkSession.builder.appName("Shopping project").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("ERROR")
 

# read the csv File 

data=spark.read.csv("E:\Data File\Project 2\drivers.csv",header=True, inferSchema=True)
data.show(10)


# df=data.withColumn("Total_Saving",col('total_price')-col('Discount'))
# df.show(5)