import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import mysql.connector
# import duckdb as db
# import requests
# from bs4 import BeautifulSoup
#
# #Fetching Web Data:
# url = "https://www.worldometers.info/coronavirus/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# #Extracting Table Data:
#
# table = soup.find("table", {"id": "main_table_countries_today"})
# rows = table.find_all("tr")

# #Processing Data Directly to DataFrame:
#
# data = []
# for row in rows:
#     cols = row.find_all(['th', 'td'])
#     cols = [col.text.strip() for col in cols]
#     data.append(cols)
#
# df = pd.DataFrame(data[1:], columns=data[0])
# # print(df.columns)
# # print(df.head())
# #print(df.isnull().sum())

# Data Cleaning
#Handlig mssing values

#df.fillna(df.mean(),inplace=True)


#print(df.describe())
# 1. First check your data types
#print(df.dtypes)

# df.drop(columns=['New Cases/1M pop','New Deaths/1M pop'],axis=1 ,inplace=True)
# #print(df.columns)
# #print(df.isnull().sum())
# df = df.rename(columns={'Country,Other': 'Country'})
# df["NewCases"]=df["NewCases"].fillna(df["NewCases"].mode()[0])
# df["TotalDeaths"]=df["TotalDeaths"].fillna(df["TotalDeaths"].mode()[0])
# df["NewDeaths"]=df["NewDeaths"].fillna(df["NewDeaths"].mode()[0])
# df["TotalRecovered"]=df["TotalRecovered"].fillna(df["TotalRecovered"].mode()[0])
# df["NewRecovered"]=df["NewRecovered"].fillna(df["NewRecovered"].mode()[0])
# df["ActiveCases"]=df["ActiveCases"].fillna(df["ActiveCases"].mode()[0])
# df["Serious,Critical"]=df["Serious,Critical"].fillna(df["Serious,Critical"].mode()[0])
# #df[ "Tot Cases/1M pop"]=df[ 'Tot Cases/1M pop'].fillna(df[ 'Tot Cases/1M pop'].mode()[0])
# df["Deaths/1M pop"]=df["Deaths/1M pop"].fillna(df["Deaths/1M pop"].mode()[0])
# df["TotalTests"]=df["TotalTests"].fillna(df["TotalTests"].mode()[0])
# df["Tests/\n1M pop"]=df["Tests/\n1M pop"].fillna(df["Tests/\n1M pop"].mode()[0])
# df["Population"]=df["Population"].fillna(df["Population"].mode()[0])
# df["Continent"]=df["Continent"].fillna(df["Continent"].mode()[0])
# df["1 Caseevery X ppl"]=df["1 Caseevery X ppl"].fillna(df["1 Caseevery X ppl"].mode()[0])
# df["1 Deathevery X ppl"]=df["1 Deathevery X ppl"].fillna(df["1 Deathevery X ppl"].mode()[0])
# df["1 Testevery X ppl"]=df["1 Testevery X ppl"].fillna(df["1 Testevery X ppl"].mode()[0])
# df["Active Cases/1M pop"]=df["Active Cases/1M pop"].fillna(df["Active Cases/1M pop"].mode()[0])

# print(df.isnull().sum())
# print(df.describe())
# print(df.dtypes)


#7.Data Visualization (Matplotlib & Seaborn)
# plt.figure(figsize=(8,5))
# sns.histplot(df['ActiveCases'],bins=20,kde=True)
# plt.title("ActiveCases")
# plt.show()

# sns.histplot(x="TotalDeaths",data=df).set_title("Total_Death")
# plt.show()

# #
# sns.histplot(x="ActiveCases",data=df).set_title("Total_Death")
# plt.show()

# #
# sns.histplot(x="ActiveCases", data=df).set_title("print")
# plt.show()


# Connect to MySQL Database
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="ashok"
# )
#
# cursor=conn.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS patients (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     Country VARCHAR(100),
#     NewCases VARCHAR(100),
#     NewDeaths VARCHAR(100),
#     ActiveCases VARCHAR(100),
#     TotalRecovered VARCHAR(100),
#     TotalCases VARCHAR(100),
#     TotalDeaths VARCHAR(100)
# )
# """)

# print(df)

# #print(df.columns)
# #cursor.execute("DROP TABLE IF EXISTS patients")
# cursor.execute("DESCRIBE patients")
# print(cursor.fetchall())

# for _, row in df.iterrows():
#     cursor.execute("INSERT INTO patients (Country,NewCases, NewDeaths,  ActiveCases, TotalRecovered,TotalCases, TotalDeaths) VALUES (%s, %s, %s,%s,%s,%s, %s)",
#     (row['Country'], row['NewCases'], row['NewDeaths'], row['ActiveCases'],row['TotalRecovered'],row['TotalCases'],row['TotalDeaths']))


# conn.commit()
# conn.close()

#Fetching Data from SQL

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="ashok"
# )

cursor=conn.cursor()

# #Retrieve Data
# cursor.execute("SELECT * FROM patients")
# rows=cursor.fetchall()
# print(rows)


# a=cursor.execute("SELECT * FROM patients")
# print(a)

#Convert to DataFrame

# df_sql=pd.DataFrame(rows,columns=["ID","Country","NewCases","NewDeaths","ActiveCases","TotalRecovered","TotalCases","TotalDeaths"])
# print(df_sql)

# conn.close()
# a=cursor.execute("SELECT * FROM patients")
# print(a)

# cursor.execute("SELECT Country,Total_eaths from patients order by Total_Deaths desc limit 5")
# cursor.execute("SELECT Country,TotalDeaths from patients order by TotalDeaths limit 5")
# rows=cursor.fetchall()
# print(rows)
#
# df=pd.DataFrame(rows)
# print(df)