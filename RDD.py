from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("MySQL_Read") \
      .getOrCreate()  
sc=spark.sparkContext

List=[10,24,25,54,65,85,24,45]
rdd=sc.parallelize(List)
# print(rdd.collect())

# aa=rdd.distinct()
# print(aa.collect())

rdd_map=rdd.map(lambda x: x+5)     # addition 
# print(rdd_map.collect())

rdd_filter=rdd.filter(lambda x:x==24)   #filter the Number
# print(rdd_filter.collect())

rdd_filter=rdd.filter(lambda x:x>24)   
# print(rdd_filter.collect())

dict_RDD =(["omkar","satara","ashok","Beed"])
dd=sc.parallelize(dict_RDD)
# rdd_flat=dd.flatMap(lambda line: line.split(" "))
# print(dd.collect())

two list add
List=[10,24,25,54,65,85,24,45]
List2=[89,54,25,47,65,64,66,48]
rdd=sc.parallelize(List)
rdd1=sc.parallelize(List2)
print(rdd.union(rdd1).collect())



DataFrame 

dict_RDD =[("omkar","satara"),("ashok","Beed")]
columns=["name","address"]
expo=spark.createDataFrame(dict_RDD,columns)
expo.show()                        
                   -- show dataframe and print RDD 


1.Parallelize 

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("RDD Example").getOrCreate()

# Get SparkContext
sc = spark.sparkContext

# Create RDD from a Python list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Show elements
print(rdd.collect())

2.external dataset 


rdd_from_file = sc.textFile("c:/documents/data.txt")

# Show first few lines
print(rdd_from_file.take(5))

3.Transformation 


rdd_numbers = sc.parallelize([1, 2, 3, 4, 5])
rdd_squared = rdd_numbers.map(lambda x: x * x)

print(rdd_squared.collect())


rdd operation

1.Transfroamtion





from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("RDD Operations Example").getOrCreate()
sc = spark.sparkContext

# Create RDD from a list
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9])

rdd_map = rdd.map(lambda x: x * 2)
print(rdd_map.collect()) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

rdd_filter = rdd.filter(lambda x: x % 2 == 0)
print(rdd_filter.collect()) # [2, 4, 6, 8]

rdd_filter = rdd.filter(lambda x: x==3)




# lines = sc.parallelize(["Hello Spark", "PySpark RDD"])

# rdd_flat = lines.map(lambda line: line.split(" "))
# print(rdd_flat.collect())                  ['Hello Spark', 'PySpark RDD']



# rdd_flat = lines.flatMap(lambda line: line.split(" "))
# print(rdd_flat.collect()) # ['Hello', 'Spark', 'PySpark', 'RDD']


# rdd_dup = sc.parallelize([1, 2, 2, 3, 3, 3])
# print(rdd_dup.distinct().collect()) # [1, 2, 3]

# rdd1 = sc.parallelize([1, 2, 3])
# rdd2 = sc.parallelize([3, 4, 5])

# print(rdd1.union(rdd2).collect()) # [1, 2, 3, 3, 4, 5]
# print(rdd1.intersection(rdd2).collect()) # [3]


# data = [("a", 1), ("b", 2), ("a", 3),("a",10)]
# rdd_kv = sc.parallelize(data)
# rdd_reduced = rdd_kv.reduceByKey(lambda a, b: a + b)
# print(rdd_reduced.collect()) # [('a', 4), ('b', 2)]


# rdd_group = rdd_kv.groupByKey().mapValues(list)
# print(rdd_group.collect()) # [('a', [1, 3]), ('b', [2])]


# rdd_sorted = sc.parallelize([('b', 2), ('a', 3), ('c', 1)]).sortByKey()
# print(rdd_sorted.collect()) # [('a', 3), ('b', 2), ('c', 1)]




# 2.Action 

# rdd=sc.parallelize([1,2,3,4,5,6])

# rdd.collect() 

# rdd.max()   --6 

# rdd.min()   --1 

# rdd.count()       -6 

# rdd.first()       --1 

# rdd.take(2)
#                   ---1 2 


# data = [("a", 1), ("b", 2), ("b", 3),("a",10)]
# rdd_kv = sc.parallelize(data)
# rdd_reduced = rdd_kv.reduceByKey(lambda a, b: a + b)
# print(rdd_reduced.collect()) # [('a', 4), ('b', 2)]


# rdd_group = rdd_kv.groupByKey().mapValues(list)
# print(rdd_group.collect()) # [('a', [1, 3]), ('b', [2])]


# rdd_sorted = sc.parallelize([('b', 2), ('a', 3), ('c', 1)]).sortByKey(ascending=True)
# print(rdd_sorted.collect()) # [('a', 3), ('b', 2), ('c', 1)]




# # 2.Action 

# rdd=sc.parallelize([1,2,3,4,5,6])

# print(rdd.collect() )

# print(rdd.max())

# print(rdd.min())

# print(rdd.count() )      

# print(rdd.first() )      

# print(rdd.take(2))




rdd=