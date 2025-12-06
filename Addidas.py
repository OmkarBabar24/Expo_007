# from pyspark.sql import SparkSession
# from pyspark.sql.functions import regexp_replace, col

# spark = SparkSession.builder.appName("adidas project").getOrCreate()

# df = spark.read.csv(r"E:\Data File\Addidas.csv", header=True, inferSchema=True)

# df.show(5)

# df = df.withColumn("Total Sales", regexp_replace(col("Total Sales"), ",", "").cast("double")) \
#        .withColumn("operating profit", regexp_replace(col("operating profit"), ",", "").cast("double")) \
#        .withColumn("price per unit", regexp_replace(col("price per unit"), ",", "").cast("double")) \
#        .withColumn("units sold", regexp_replace(col("units sold"), ",", "").cast("double"))




# total_rows = df.count()
# distinct_rows = df.distinct().count()

# print("Total rows:", total_rows)
# print("Distinct rows:", distinct_rows)
# print("Duplicate rows:", total_rows - distinct_rows)

# df.createOrReplaceTempView("ashok")

# spark.sql("select * from ashok").show()

# spark.sql("select sum(Total Sales) as total_sales,sum(operating profit) total_profit,avg(price per unit) av_price_per_unit,sum(units sold) total_unit_sold from ashok").show()

# spark.sql("""
#     SELECT 
#         SUM(Total Sales) AS total_sales,
#         SUM(operating profit) AS total_profit,
#         AVG(price per unit) AS av_price_per_unit,
#         SUM(units sold) AS total_unit_sold
#     FROM ashok
# """).show()


from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

spark = SparkSession.builder.appName("adidas project").getOrCreate()

df = spark.read.csv(r"E:\Data File\Addidas.csv", header=True, inferSchema=True)

#df.show(5)

df = df.withColumn("Total Sales", regexp_replace(col("Total Sales"), ",", "").cast("double")) \
       .withColumn("operating profit", regexp_replace(col("operating profit"), ",", "").cast("double")) \
       .withColumn("price per unit", regexp_replace(col("price per unit"), ",", "").cast("double")) \
       .withColumn("units sold", regexp_replace(col("units sold"), ",", "").cast("double"))




total_rows = df.count()
distinct_rows = df.distinct().count()

print("Total rows:", total_rows)
print("Distinct rows:", distinct_rows)
print("Duplicate rows:", total_rows - distinct_rows)

df.createOrReplaceTempView("ashok")

spark.sql("select * from ashok").show()

# spark.sql("select sum(`Total Sales`) as total_sales,sum(`operating profit`) total_profit,avg(`price per unit`) av_price_per_unit,sum(`units sold`) total_unit_sold from ashok").show()



# Total sales by month
spark.sql(""" SELECT Date_Format(to_Date(`Invoice Date`,'M/d/yyyy'),'MMMM')as Date ,
           Sum(`Total Sales`)
          from ashok
           group by 1 
          """).show()



# Total sales by state
spark.sql("""SELECT City,
          sum(`Total Sales`)
          from ashok
          group by 1
          """).show()




# total sales by region
spark.sql("""SELECT Region,
          sum(`Total Sales`)
          from ashok
          group by 1
          """).show()
# Total sales by product
spark.sql("""SELECT Product,
          sum(`Total Sales`)
          from ashok
          group by 1
          """).show()

# Total sales by retailer
spark.sql("""SELECT Retailer,
          sum(`Total Sales`)
          from ashok
          group by 1
          """).show()
# Units Sold by Product Category
spark.sql("select `Product`,sum(`units sold`) from ashok group by Product").show()


# Top Performing Cities by Profit

spark.sql("""SELECT `City`,
          sum(`operating profit`)
          from ashok
          group by 1
          order by 2 desc
          """).show()

