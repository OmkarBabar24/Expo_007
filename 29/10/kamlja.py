from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Window
from functools import reduce
from pyspark.sql import DataFrame
import os


spark = SparkSession.builder.appName("transportation_pipeline").getOrCreate()
data=spark.read.csv("E:\Data File\Match_Data.csv",header=True,inferSchema=True)
#data.show()
# data.printSchema()
df=data.withColumn("date",to_date("Date",'m/d/yyyy')) # yyyy\mm\dd

# df.printSchema()

# df.show()

# dff=df.withColumns({'omkar':col('season')+100,'ashok':col('season')*2})

# dff.show()

# df1=df.withColumnsRenamed({'city':'new_city','date':'new_date'})

# df1.show()

# data.agg(
#     max('win_by_runs').alias('max_number'),
#     min("win_by_runs").alias('min_runs'),
#     count('win_by_runs').alias('count_runs'),
#     avg('win_by_runs').alias('avg_runs')
# ).show()

# aa=df.withColumn('date_1',year('date','yyyy'))
# aa.show()
# aa1=df.withColumn('data_1',year('date'))
# aa1.show()

aa1=df.withColumn('data_1',date_format('date','EEEE'))
aa1.show()