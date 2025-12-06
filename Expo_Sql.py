from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("MySQL_Read") \
      .getOrCreate()  
spark.sparkContext.setLogLevel("ERROR")

data1=spark.read.csv("C:\omkar\Excel\matches 1.csv",header=True,inferSchema=True)
# data1.show()

data1.createOrReplaceTempView("omkar")
aa=spark.sql("select * from omkar")
# aa.show()

aa=spark.sql("select * from omkar where city='Pune'")
# aa.show()

aa=spark.sql("select season,count(season)as t_season from omkar group by season order by t_season desc limit 5")
# aa.show()

# spark.sql("select * from ("SELECT season,winner, count(winner)as T_winner,RANK()OVER(partition by season order by count(winner) desc as rnc from omkar group by season,winner")as kamlaja") where kamlaja < 4 ))

# spark.sql("select * from (SELECT season,winner, count(winner)as T_winner,RANK()OVER(partition by season order by count(winner) desc) as rnc from omkar group by season,winner)as kamalja where rnc <=3").show()

# spark.sql("""SELECT 
#           season,
#           winner, 
#           count(winner)as t_winner,
#           RANK()OVER(partition by season order by count(winner) desc) as rnc 
#           from omkar
#           group by season,winner""").show()

# spark.sql("""with new as (select
#           season,
#           winner, 
#           count(winner)as total_winner,
#           RANK() OVER(partition by season order by count(winner) desc) as rnc 
#           from omkar
#           group by season,winner)
#          select * from new where rnc <=3""").show()

# spark.sql("""with ashok as (select
#           season,player_of_match,
#           count(player_of_match)as total_a,
#           dense_rank() over(partition by season order by count(player_of_match) desc)as rnc
#           from omkar 
#           group by season,player_of_match)
#           select * from ashok where rnc == 1 """).show()


