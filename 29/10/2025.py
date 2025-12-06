from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Window
from functools import reduce
from pyspark.sql import dataframe
import os 

spark=SparkSession.builder\
.appName("Practice Data") \
.getOrCreate()


data=[
    (1,"omkar","Bsc"),
    (2,"ashok","MTech"),
    (3,"kamlja","Bsc"),
    (4,"chaitrali","MTech"),
    (5,"komal","Msc"),
    (6,"ankita","Msc")
     ]
df= spark.createDataFrame(data,["id","Name","Equcation"])
# df.show()


# data1=[
#     (7,"rahul","Bsc"),
#     (8,"rohini","Msc"),
#     (9,"Pranay","MTech")
# ]
# df2=spark.createDataFrame (data1,["id","Name","Equcation"])
# # df2.show()

# df.printSchema()
# print("Total_Count",df.count())
# print("Total_colunmns",df.columns)
# print("Total_lenght",len(df.columns))
# df.select("id","Name").show()  
# df.withColumnRenamed("id","Std_id").show()

# change DataType 
# data=df.withColumn('Equcation',col("Equcation").cast("integer"))
# data.show()


#  Add columns 
df3 = df.withColumn(
    "salary",
    when(df.id == 1, 20000)
   .when(df.id == 2, 25000)
   .when(df.id == 3, 30000)
   .when(df.id == 4, 35000)
   .when(df.id == 5, 40000)
   .when(df.id == 6, 45000)
)

df3.show()
# df.show()
# df.drop("contact").show()
# df.withColumn('salary',col('salary')+4200).show()
# df.filter('salary > 30000').show()
# df.where("Equcation =='Msc'").show()
# df.filter("Name Like 'o%'").show()
# df.filter("Name Like '%a'").show()


# df.agg(avg('salary').alias('avg_salary')).show()
# df.groupBy('Equcation').agg(sum('salary')).show()
# df.agg(min('salary').alias('mini_salary')).show()
# df.agg(max('salary').alias('max_salary')).show()
# df.groupBy('Name').agg(count('Name')).show()

# df.orderBy(desc('salary')).show()
# df.orderBy(desc('salary')).limit(5).show()

# df.createOrReplaceTempView('Expo')
# spark.sql("select avg(salary)as Salary from expo limit 2 ").show()
# spark.sql("select name,equcation from expo where equcation =='Bsc'").show()

# df.filter(col('name').isNull()).show()
# df.filter(col('name').na.drop()).show()

# df.fillna({'salary':avg("salary")}).show()
# Student.show()


# Student.write.option("header", "true") \
#     .mode("overwrite") \
#     .csv(r"E:\Data File\Over_Write_Data\29-11-2025_ETL")


# data=[("omkar",213,'Pune'),("rahul",1021,'Beed')]
# df=spark.createDataFrame(data["name",id,"city"]).show()


# df3.printSchema()
# print(df3.count())
# print(df3.columns)
# print(len(df3.columns))
# df3.select("id","name").show()
# df3.withColumnRenamed('id',"std_id").show()

# data=df3.withColumn('Name',col("Name").cast('integer'))
# data.show()

# df3.drop("name").show()
# df3.withColumn('incresment',col('salary')+14000).show()
# df3.filter('salary <= 35000').show()
# df3.where("Equcation =='Bsc'").show()
# df3.filter("Name like 'o%'").show()
# df3.filter("Name  like '%a'").show()

# df3.agg(avg('salary').alias('avg_salary')).show()
# df3.groupBy("salary").agg(min('salary')).show()
# df3.agg(min('salary').alias('min_salary')).show()
# df3.agg(max('salary').alias("max_salary")).show()
# df3.groupBy('Name').agg(count('name').alias('total_count')).show()

# df3.orderBy(desc('salary')).show()
# df3.createOrReplaceTempView('expo')
# spark.sql("select Avg(salary)as avg_salary from expo order by avg_salary").show()
# spark.sql("select Name, min(salary) as salary from expo group by Name order by salary desc").show()

#df3.filter((df3.salary >=35000).isnull()).show()

#df3.select('salary').show()

# df3.filter('salary > 35000').show()
# df3.fillna({"salary":avg("salary")}).show()

# from pyspark.sql.functions import avg

# avg_salary = df3.select(avg("salary")).collect()[0][0]
# df3 = df3.fillna({"salary": avg_salary})
# df3.show()

# Student.write.option("header","true")\
#     .mode("overwrite")\
#         .csv("E:\Data File\Over_Write_ Data\dec4")
df3.write.option("header", "true") \
    .mode("overwrite") \
    .csv("E:\Data File\Over_Write_ Data\dec4")
