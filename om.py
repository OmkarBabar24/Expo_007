# from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#     .appName("MySQL_Read") \
#         .config("spark.jars", r"/C:\\py_spark_installation\\hadoop\\lib\\mysql-connector-java-8.0.20.jar,C:\\py_spark_installation\\hadoop\\lib\\ojdbc8.jar")\
#      .getOrCreate()  
# spark.sparkContext.setLogLevel("ERROR")
# print("omkar")

# spark = SparkSession.builder \
#     .appName("MySQL_Read") \
#     .getOrCreate()  
# spark.sparkContext.setLogLevel("ERROR")

# model_config = spark.read.csv("C:/Users/Ashok/Desktop/data_analysis/data/model_config.csv",header=True, inferSchema=True)
# # # model_config.show(5)

# jdbc_url = "jdbc:mysql://localhost:3306/yc?useSSL=false&allowPublicKeyRetrieval=true"
# table_name = "matches"
# username = "root"
# password = "root123"

# df = spark.read.format("jdbc") \
#     .option("url", jdbc_url) \
#     .option("driver", "com.mysql.cj.jdbc.Driver") \
#     .option("dbtable", table_name) \
#     .option("user", username) \
#     .option("password", password) \
#     .load()

# df.show(5)

# jdbc_url = "jdbc:mysql://localhost/expo?serverTimezone=UTC&useSSL=false"

# table_name = "Matches"
# username = "omkar"
# password = "Admin@123"

# df = spark.read.format("jdbc") \
#     .option("url", jdbc_url) \
#     .option("driver", "com.mysql.cj.jdbc.Driver") \
#     .option("dbtable", table_name) \
#     .option("user", username) \
#     .option("password", password) \
#     .load()

# df.show(5)

# jdbc_url = "jdbc:mysql://localhost:3306/company?serverTimezone=UTC&useSSL=false"
# jdbc_url = "jdbc:mysql://localhost/expo?useSSL=false&allowPublicKeyRetrieval=true"
# table_name = "Matches"
# username = "omkar"
# password = "Admin@123"

# df = spark.read.format("jdbc") \
#     .option("url", jdbc_url) \
#     .option("driver", "com.mysql.cj.jdbc.Driver") \
#     .option("dbtable", table_name) \
#     .option("user", username) \
#     .option("password", password) \
#     .load()

# df.show(5)
# 1 csv file-

# df=spark.read.csv("C:\omkar\Excel\matches 1.csv",header=True,inferSchema=True)
# df.show()


# # With delimiter(text.csv)
# df_csv = spark.read.option("delimiter", ",").csv("C:\omkar\project file\Mobile_Sales_1.txt", header=True, inferSchema=True)
# df_csv.show()


# 2.Excel file:- 

# spark = SparkSession.builder \
#     .appName("ExcelExample") \
#     .config("spark.jars.packages", "com.crealytics:spark-excel_2.12:0.13.7") \
#     .getOrCreate()

# df_excel = spark.read.format("com.crealytics.spark.excel") \
#     .option("header", "true") \
#     .option("inferSchema", "true") \
#     .load("path/to/yourfile.xlsx")

# df_excel.show()


# 4.Json file:- 

# # Simple JSON
# df_json = spark.read.json("path/to/yourfile.json")
# df_json.show()

# # Multiline JSON
# df_json = spark.read.option("multiline", True).json("path/to/yourfile.json")
# df_json.show()


# 5.Text file:- 

# # Each line as one record
# df_text = spark.read.text("path/to/yourfile.txt")
# df_text.show(truncate=False)

# # For delimited text (e.g., tab-separated)
# df_text = spark.read.option("delimiter", "\t").csv("path/to/yourfile.txt", header=True, inferSchema=True)
# df_text.show()


# # 6.Mysql database:- 

# df = spark.read.format("jdbc") \
#     .option("url", "jdbc:mysql://localhost/new") \
#     .option("driver", "com.mysql.cj.jdbc.Driver") \
#     .option("dbtable", "Match01") \
#     .option("user", "ashok") \
#     .option("password", "Admin@123") \
#     .load()

# df.show(5)


# 7.Oracle database:- 

# df_oracle = spark.read.format("jdbc") \
#     .option("url", "jdbc:oracle:thin:@//hostname:1521/servicename") \
#     .option("driver", "oracle.jdbc.driver.OracleDriver") \
#     .option("dbtable", "your_table_name") \
#     .option("user", "your_username") \
#     .option("password", "your_password") \
#     .load()

# df_oracle.show()


# 8.Write data to external files:- 

# # Example transformation
# df=df_csv.select("id", "name") \
#     .filter(df_csv["id"] > 100) \
#     .show()

# # Save back as CSV or Parquet
# df.write.mode("overwrite").csv("output/path/csv_output")
# df.write.mode("overwrite").parquet("output/path/parquet_output")


# ***********Analysis*****************

# 1.Basic DataFrame Info:- 

# # Show first few records
# df.show(5)

# # Display all rows fully (use cautiously for large data)
# df.show(truncate=False)

# # Print DataFrame schema (column names and types)
# df.printSchema()

# # Get column names
# print("total columns",df.columns)

# # Get number of columns
# print(len(df.columns))

# # # Count total number of rows
# print(df.count())

# # Get DataFrame summary statistics
# df.describe().show()

# # Extended summary (mean, stddev, min, max, etc.)
# df.summary().show()


# 2.Schema & Data Types Validation

# # Show detailed schema as StructType
# print(df.schema)

# # Get specific column data type
# df.dtypes

# # Verify column data types
# from pyspark.sql import functions as f
# print(df.select([f.col(c).cast("string").alias(c) for c in df.columns]).printSchema())


# 3.Data Quality Checks


# from pyspark.sql import functions as F

# # Check for null values in each column
# df.select([F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns]).show()

# # Count distinct values per column
# df.select([F.countDistinct(F.col(c)).alias(c) for c in df.columns]).show()

# # Find duplicate rows
# df.groupBy(df.columns).count().filter("count > 1").show()

# # Drop duplicate rows
# df_no_dup = df.dropDuplicates()

# # Check for blank strings
# df.filter(F.col("Winner") == "").count()

# # Replace nulls with default value
# df.fillna({"city": "satara"}).show()





# 4.Exploratory Data Analysis (EDA)

# # View top N values of a column
# df.groupBy("city").count().orderBy(F.desc("count")).show(10)

# # Get distinct values of a column
# df.select("city").distinct().show()

# # Frequency count (value distribution)
# df.groupby("city").agg(F.count("*").alias("count")).show()

# # Min, Max, Mean, StdDev
# df.select(
#     F.min("numeric_col").alias("min"),
#     F.max("numeric_col").alias("max"),
#     F.mean("numeric_col").alias("mean"),
#     F.stddev("numeric_col").alias("stddev")
# ).show()

# # Correlation between numeric columns
# df.stat.corr("col1", "col2")



# 5.Filtering & Sampling


# # Filter rows
# df.filter(df["age"] > 30).show()
# df.filter((df["salary"] > 50000) & (df["gender"] == "M")).show()

# # Random sample
# df.sample(withReplacement=False, fraction=0.1).show()

# # Take first few rows as list
# df.take(5)




# 6.Column-Level Analysis


# # Add new calculated column
# df = df.withColumn("increment_value", F.col("salary") * 0.1)

# # Rename column
# df = df.withColumnRenamed("old_name", "new_name")

# # Drop columns
# df = df.drop("unwanted_col")

# # Cast data type
# df = df.withColumn("age", F.col("age").cast("int"))

# # Get summary per group
# df.groupBy("department").agg(F.avg("salary").alias("avg_salary")).show()

# #create temporary view 

# df.createOrReplaceTempView("employee")
# df1=spark.sql("select * from employee")

# df1.show() 

# 7.Save Validation Results



# # Save as CSV
# df.write.mode("overwrite").csv("output/validated_data")

# # Save as Parquet
# df.write.mode("overwrite").parquet("output/validated_data_parquet")


# ***********Optimization of technique pyspark********************

from pyspark.sql import SparkSession
spark=SparkSession.builder\
     .appName("Mysql Read")\
     .getOrCreate()
sc=spark.sparkContext

#    data frame 
# dict=[("BscI","MscI"),("BscII",'MscII'),("Bsc III","NA")]
# columns=["BSC","MSC"]
# dict_RDD =[("omkar","satara"),("ashok","Beed")]
# columns=["name","address"]
# expo=spark.createDataFrame(dict,columns)
# expo.show()

l=[10,25,32,39,45,59,72]
rdd=sc.parallelize(l)
# print(rdd.collect())  
# aa=rdd.distinct()
# print(aa.collect())

S
