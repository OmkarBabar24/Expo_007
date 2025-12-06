from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("MySQL_Read") \
      .getOrCreate()  
sc=spark.sparkContext
from pyspark.sql import functions as f
from pyspark.sql.functions import col,count,when,isnull,when

ETL=spark.read.csv("C:\omkar\project\PIZZA Project\pizza_sales.csv",header=True,inferSchema=True)
# ETL.show()

# print(ETL.columns)
# print(ETL.count())
# print(len(ETL.columns))
# print(ETL.printSchema)

# IS NULL
# ETL.select([count(when(isnull(c),c)).alias(c) for c in ETL.columns]).show()
# duplicate
# aa=ETL.distinct().count()-ETL.count()
# print(aa)

# filter 

# ETL.filter(f.col("order_id")<7).show()
# ETL.filter(f.col("pizza_size")=='M').show()
# ETL.filter((f.col("order_id")<7) & (f.col("pizza_size")=='M')).show()
# ETL.filter((f.col("order_id")<7) | (f.col("pizza_size")=='M')).show()

#  regular Expression

# ETL.filter(f.col("pizza_name_id").endswith("n_m")).show()
# ETL.filter(f.col("pizza_name_id").startswith("bbq")).show()
# ETL.filter(f.col("pizza_name_id").contains("ckn")).show()
# ETL.select([f.col(c).cast("string").alias(c) for c in ETL.columns]).show()
# print(ETL.printSchema)
# df=ETL.withColumn("pizza_id",f.col("pizza_id").cast("bigint"))
# print(df)

# add column    ----withcolume use for particular column

df=ETL.withColumn("omkar",f.col("unit_price")+ f.col("total_price"))
# df.show()

df.select("omkar","pizza_id","total_price").show()

# save csv file   --overwrite ,append,ignore,error

# csv file
# df.write.mode("overwrite").csv("E:/file/kamalja")      

df.coalesce(1).write.mode("overwrite").csv("E:/file/kamalja1") 