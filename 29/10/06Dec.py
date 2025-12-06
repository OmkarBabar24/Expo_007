from pyspark.sql import functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import dataframe
from functools import reduce
import os

spark=SparkSession.builder.appName("Practice session").getOrCreate()

data=[(101,"ram",45200,"satara"),(102,"sham",56412,"kohlapur"),(103,"radha",65984,'sangali'),(104,"seeta",334657,"wai"),(105,"geeta",87456,"karad")]
df=spark.createDataFrame(data,["id","name","salary","city"])

# df.printSchema()
# print(df.count())
# print("Total_Count",df.count())
# print("Total_Count =", df.count())
# print("columns=",df.columns)
# print('length =',len(df.columns))
# df.select("name","salary").show()
# df.withColumnRenamed("name","Name").show()

# df.withColumn("salary",col("salary")+12500).show()
# df.filter("salary > 70000").show()
# df.filter("salary < 70000").show()
# df.where("city == 'satara'").show()
# df.filter("city Like '%r'").show()
# df.filter("city Like 's%'").show()
# df.filter("name Like 'm%'").show()


# df.agg(avg('salary').alias('Avg_salary')).show()
# df.groupBy("city").agg(sum('salary').alias('total_salary')).show()
# df.agg(max('salary').alias('max_salary')).show()
# df.orderBy(desc('salary')).show()

df.filter(df.name.isnull()).show()