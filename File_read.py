from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("MySQL_Read") \
      .getOrCreate()  
sc=spark.sparkContext

# CSV File 
data=spark.read.csv("E:\Data File\Match_Data.csv",header=True,inferSchema=True)
# data.show(12)

# Text File
Data_text= spark.read.option("delimiter", ",").csv("C:\omkar\project file\Mobile_Sales_1.txt", header=True, inferSchema=True)
# Data_text.show(10)

# parquet file
para_file=spark.read.parquet("E:\Data File\house-price.parquet",header=True,inferschema=True)
# para_file.show(10)

# ORC File 
orc_file=spark.read.orc("E:\Data File\part-00005-5df36169-249c-4e9f-9d3f-8c02a0aa303f-c000.snappy.orc")
# orc_file.show(15)

# JSON file

J_file=spark.read.option("multiline",True).json("E:\Data File\house-price-parquet.json")
# J_file.show(10)

# crc file