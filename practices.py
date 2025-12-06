from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("MySQL_Read") \
      .getOrCreate()  
sc=spark.sparkContext


data1=[1,2,3,6,4,5,8,7,70]
Rdd=sc.parallelize(data1)
# print(Rdd.collect())   
# Rdd = sc.textFile.save("E:\Study Notwes\Expo.txt") 
# print(Rdd.collect()) 
# Rdd.saveAsTextFile("E:\Study Notwes\Expo.txt")

# Rdd.saveAsTextFile("E:\Study Notwes\kamalja.txt")


# Operations that return a new RDD (lazy evaluated).
# Example: map(), filter(), flatMap(), distinct(), union().
# rdd2 = Rdd.map(lambda x: x * 2)
# print(rdd2.collect())

# rdd2=Rdd.filter(lambda x: x>25)
# print(rdd2.collect())
label = sc.parallelize(["Data Engineer", "Expo"])
rdd2=label.map(lambda line : line.split(" "))
print(rdd2.collect())