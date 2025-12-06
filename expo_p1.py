from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("MySql_Read")\
       .getOrCreate()
# sc=spark.Sparkcontext

df=spark.read.csv("E:\Data File\Addidas.csv",header=True,inferSchema=True)
df.show()

from pyspark.sql.functions import regexp_replace, col


df = df.withColumn("Total Sales", regexp_replace(col("Total Sales"), ",", "").cast("double")) \
       .withColumn("operating profit", regexp_replace(col("operating profit"), ",", "").cast("double")) \
       .withColumn("price per unit", regexp_replace(col("price per unit"), ",", "").cast("double")) \
       .withColumn("units sold", regexp_replace(col("units sold"), ",", "").cast("double"))




total_rows = df.count()
distinct_rows = df.distinct().count()

print("Total rows:", total_rows)
print("Distinct rows:", distinct_rows)
print("Duplicate rows:", total_rows - distinct_rows)

from pyspark.sql.functions import col

df = df.filter(col("Total Sales").rlike("^[0-9.]+$"))  # फक्त अंक असलेले values ठेवा
df = df.withColumn("Total_Sales", col("Total Sales").cast("double"))



df.createOrReplaceTempView("ashok")

spark.sql("describe ashok").show()

# spark.sql("select sum('Total Sales') as total_sales,sum('operating profit) total_profit,avg(price per unit) av_price_per_unit,sum(units sold) total_unit_sold from ashok").show()
# df.printSchema()
spark.sql("""
    SELECT 
        SUM('Total Sales') AS total_sales,
        SUM('operating profit') AS total_profit,
        AVG('price per unit') AS av_price_per_unit,
        SUM('units sold') AS total_unit_sold
    FROM ashok
""").show()