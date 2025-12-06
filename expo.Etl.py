from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import Window
from functools import reduce
from pyspark.sql import DataFrame
import os


spark = SparkSession.builder \
    .appName("transportation_pipeline") \
    .getOrCreate()
ss_dep=spark.read.csv("E:\Data File\SS_TECH Data\SE_tech Emp3.csv" ,header= True, inferSchema= True)
# ss_emp=spark.read.csv("E:\Data File\SS_TECH Data\SS_tech Emp.csv" ,header= True, inferSchema= True)



# 1)Print DataFrame schema.
# ss_dep.printSchema()

# 2)Count total number of rows.
# print("TOTAL COUNT",ss_dep.count())

#3) Count total number of columns.

# print("total_columns",ss_dep.columns)
# print(len(ss_dep.columns))

# 4)🔹 Column Operations
# SS_salary=spark.read.csv("E:\Data File\SS_TECH Data\SE_tech Emp2.csv" ,header= True, inferSchema= True)

# Show only Name and Salary columns.

# ss_dep.select('EMP_NAME','location').show()
# Rename column EmpId to Employee_ID.

# ss_dep.withColumnRenamed('EMP_NAME','NAME').show()
# Change Salary datatype to Integer.
# df=SS_salary.withColumn('Salary',col('Salary').cast("string"))
# df.show()
# df1=SS_salary.withColumn('Salary',col('Salary').cast("integer"))
# df1.printSchema()
# Add a new column Bonus = Salary * 0.10

# SS_salary.withColumn('Salary',col('Salary')+ 1200).show()
# Drop a column you don’t need.
# SS_salary.drop('Email').show()

# 🔹 Filtering Operations

# Find employees with Salary > 50000.
# SS_salary.filter('Salary > 50000').show()

# Filter employees from IT department.

# SS_salary.where("LOC == 'NEW YORK'").show()
# Find employees older than 30.

# Select employees whose name starts with 'B'.
# SS_salary.filter("FName Like 'B%'").show()
# SS_salary.filter("FName Like '%s'").show()

# Display employees who joined after 2022.
# SS_salary.filter("join_date > '2022'")
# 🔹 Aggregation & GroupBy

# Total salary department-wise.
# SS_salary.groupBy('LOC').agg(sum('Salary')).show()
# Average salary.
# SS_salary.agg(avg('Salary').alias('avg_salary')).show()
# Maximum salary.
# SS_salary.agg(max('Salary').alias('Maximum_salary')).show()
# Minimum salary.
# SS_salary.agg(min('Salary').alias('Minimum_salary')).show()
# Count employees per department.
# SS_salary.groupBy('FName').agg(count('FName')).show()
# 🔹 Sorting

# Sort salaries in descending order.
# SS_salary.orderBy(desc('Salary')).show()
# Show Top 5 highest paid employees.
# SS_salary.orderBy(desc('Salary')).limit(5).show()
# 🔹 SQL Queries

# Create Temp View.
# SS_salary.createOrReplaceTempView('Expo')
# Write SQL to fetch IT employees.
# spark.sql("select FName,LOC from expo where LOC='DALLAS'").show()
# Write SQL to calculate average salary.
# spark.sql("select avg(Salary) as AvG_SALARY From expo").show()
# 🔹 Missing Values

# Find null values in data.
# SS_salary.filter(col('EMail').isNull()).show()
# Drop rows with null salary.
# SS_salary.filter(col('Salary').na.drop()).show()

# SS_salary.na.drop().show()

# Fill missing salary with average salary.
# SS_salary.fillna({'Salary':avg("Salary")}).show()
# 🔹 Join (If second file exists)

# Join with Department table.
# aa=SS_salary.join(ss_dep,SS_salary.EmpID ==ss_dep.EmpID,"inner")
# aa.show()
# Show employee name with department.
# aa.select('FName','Dept_name').show()
# 🔹 File Writing

# Save result as Parquet.
# aa.write.option("header","true").mode("overwrite").csv("E:\Data File\SE_TECH Data\Practice ETL")
# aa.write.option("header","true").mode("overwrite").parquet("E:\Data File\SE_TECH Data\Practice ETL")
# aa.write.mode("overwrite").csv("E:\Data File\SE_TECH Data\om",header=True)
# Save output as CSVparquet

# 28/11/2025
expo_emp=spark.read.csv("E:\Data File\SS_TECH Data\EXPO_employee.csv",header=True,inferSchema=True)
# expo_emp.show(5)

# data=Window.partitionBy('department').orderBy(desc('salary'))
# a=expo_emp.withColumn('kamlaja',rank().over(data))
#a.show()
#a.where('kamlaja < 3')
# a.filter(col('kamlaja').between(5,10)).show()

# Assign a row number to each record within each department.
# data=Window.partitionBy('department').orderBy(desc('salary'))
# a=expo_emp.withColumn('rnk',row_number().over(data))
# a.filter(col('rnk').between(50,70)).show()

# Rank employees by salary inside each department.
# data=Window.partitionBy('department').orderBy(desc('salary'))
# a=expo_emp.withColumn('om',rank().over(data)).show()

# data =Window.partitionBy('department').orderBy(desc('salary'))
# aa=expo_emp.withColumn('rnk',rank().over(data))
# aa.filter('rnk <= 2').show()
# Show dense rank of employees based on salary.
# data=Window.partitionBy('department').orderBy(desc('salary'))
# aa=expo_emp.withColumn('om',dense_rank().over(data)).show()

# Divide all employees into 4 salary groups using NTILE.
# data=Window.partitionBy('department').orderBy(('salary'))
# aa=expo_emp.withColumn('om',ntile(2).over(data))
# aa.where("department== 'Finance'").show()
# Display total salary for each department without using GROUP BY.
# data=Window.partitionBy('department')
# aa=expo_emp.withColumn(col(sum('salary')).over(data)).show()

# expo_emp.withColumn("total_salary", sum("salary").over(data)) \
#         .select("department", "salary", "total_salary") \
#         .show()
# aa=expo_emp.groupBy('department').sum('salary').show()
# ✅ INTERMEDIATE QUESTIONS

# Show average salary of each department on every row.

# data=Window.partitionBy('department')
# aa=expo_emp.withColumn("om",avg('salary').over(data)).show()

# Find employees earning more than department average.
# data=Window.partitionBy('department')
# aa=expo_emp.withColumn('dept_avg',avg('salary').over(data))
# aa.filter(col('salary') > col('dept_avg')).show()

# aa=expo_emp.groupBy('department').agg(avg('salary').alias('avg_salary'))
# expo_emp.join(aa,'department','inner').filter(col('salary') > col('avg_salary')).show()

# Show highest salary in each department but return all employees.
# aa=expo_emp.groupBy('department').agg(max('salary').alias('max_salary'))
# expo_emp.join(aa,'department','inner').show()


# Calculate salary difference between each employee and the previous employee.

# data=Window.orderBy('emp_id')
# df2=expo_emp.withColumn("prives_salary", lag('salary').over(data))
# df3=df2.withColumn("diff_salary",col('salary') - col('prives_salary')).show()


# Display next employee’s salary using window function.

# data=Window.orderBy('salary')
# df=expo_emp.withColumn("Previous_salary",lead('salary',1).over(data)).show()
# df3=df.withcoloumn("Next_salary",col('salary'))


# Find first hired employee in each department.
# data=Window.partitionBy('department').orderBy("joining_date")
# df=expo_emp.withColumn('om',row_number().over(data)).filter('om == 1').show()


# Find last hired employee in each department.
# data=Window.partitionBy('department').orderBy(desc("joining_date"))
# df=expo_emp.withColumn('om',row_number().over(data)).filter('om == 1').show()
# Find cumulative salary by department.

# Show percent rank of each employee by salary.
# data=Window.partitionBy('department').orderBy(desc('salary'))
# expo_emp.withColumn('percent_col',percent_rank().over(data)).show(5)


# ✅ ADVANCED QUESTIONS

# Get top 2 highest paid employees in each department.
# data=Window.partitionBy('department').orderBy(desc('salary'))
# expo_emp.withColumn('High_emp',row_number().over(data))\
#     .filter('High_emp <= 2').show()

# Remove duplicate records using window function.
# data=Window.partitionBy('department','name','salary','dept_id','joining_date','city','gender')\
#     .orderBy('emp_id')
# expo_emp.withColumn('duplicate',row_number().over(data))\
#     .filter('duplicate = 1')\
#     .drop("duplicate").show()

# Calculate 3-row moving average of salary.
data = Window.orderBy('joining_date').rowsBetween(-2, 0)

expo_emp.withColumn("moving_avg_salary", avg("salary").over(data)).show()


# Identify salary outliers using window functions.



# Find employees with same salary within department.

# Detect gaps in employee IDs using LAG.

# ✅ SCENARIO QUESTIONS

# Show employees with salary higher than dept average.

# Rank employees across entire company.

# Show difference between department max salary and employee salary.

# Count employees per department without GROUP BY.

# Show running count of employees.