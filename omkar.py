from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import window
from functools import reduce 
from pyspark.sql import DataFrame
import os 

spark=SparkSession.builder.appName("Practice session").getOrCreate()
data=spark.read.csv("E:\Data File\Match_Data.csv",header=True,inferSchema=True)
# data.show(10)

# data.createTempView('expo')
# aa=spark.sql("select winner,count(winner)as total_winner from  expo group by winner order by total_winner desc limit 2")
# aa.show()

data.groupBy("winner").agg(count("winner").alias("total_winner")).orderBy(desc("total_winner"))\
    where("")