import pandas as pd
air=pd.read_csv(r"C:\omkar\project\airline.csv")
print(air.columns)

count=pd.read_csv(r"C:\omkar\project\country.csv",encoding="latin1")
print(count.columns)

route=pd.read_csv(r"C:\omkar\project\routes.dat.csv")
print(route.columns)

print(count.head())
print(count.columns)

import duckdb as db


# A. Find list of Airports operating in the Country India
# a=db.query("select ANY_VALUE(country),Airportname from country where country='India' group by Airportname order by Airportname desc limit 10 ")
# print(a)
#
# # B. Find the list of Airlines having zero stops
# b=db.query("select a.Numberofstop,b.Name from airlines a,route b where a.id=b.id and Numberofstop=0 order by b.Name desc limit 15")
# print(b)
#
# # C. List of Airlines operating with code share
# c=duckdb.query("select ANY_VALUE(a.name),b.Airlinecode from route a,airlines b where a.id=b.id group by b.Airlinecode ")
# print(c)
#
# # D. Which country (or) territory having highest Airports
# d=db.query("select country,Airportname from country group by country,Airportname order by Airportname desc limit 10")
# print(d)
#
# # E. Find the list of Active Airlines in United state
# e=db.query("select name,country,Activestatus from route where country='United States' and Activestatus='Y' order by name desc limit 10")
# #print(e)