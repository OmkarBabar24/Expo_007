import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import requests
from bs4 import BeautifulSoup
# import mysql.connector

import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", {"id": "main_table_countries_today"})
rows = table.find_all("tr")

with open('covid19_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        csvwriter.writerow(cols)

print("save file  covid19_data.csv")

#4.Loading Healthcare Data (CSV) Using Pandas
df = pd.read_csv("covid19_data.csv")
#print(df.head())  # Display first few rows

#5.Data Cleaning & Processing Using Pandas & NumPy

df.drop(columns=['New Cases/1M pop','New Deaths/1M pop'],axis=1 ,inplace=True)
print(df.columns)
#print(df.isnull().sum())

df["NewCases"]=df["NewCases"].fillna(df["NewCases"].mode()[0])
df["TotalDeaths"]=df["TotalDeaths"].fillna(df["TotalDeaths"].mode()[0])
df["NewDeaths"]=df["NewDeaths"].fillna(df["NewDeaths"].mode()[0])
df["TotalRecovered"]=df["TotalRecovered"].fillna(df["TotalRecovered"].mode()[0])
df["NewRecovered"]=df["NewRecovered"].fillna(df["NewRecovered"].mode()[0])
df["ActiveCases"]=df["ActiveCases"].fillna(df["ActiveCases"].mode()[0])
df["Serious,Critical"]=df["Serious,Critical"].fillna(df["Serious,Critical"].mode()[0])
df["Tot Cases/1M pop"]=df["Tot Cases/1M pop"].fillna(df["Tot Cases/1M pop"].mode()[0])
df["Deaths/1M pop"]=df["Deaths/1M pop"].fillna(df["Deaths/1M pop"].mode()[0])
df["TotalTests"]=df["TotalTests"].fillna(df["TotalTests"].mode()[0])
df["Tests/\n1M pop"]=df["Tests/\n1M pop"].fillna(df["Tests/\n1M pop"].mode()[0])
df["Population"]=df["Population"].fillna(df["Population"].mode()[0])
df["Continent"]=df["Continent"].fillna(df["Continent"].mode()[0])
df["1 Caseevery X ppl"]=df["1 Caseevery X ppl"].fillna(df["1 Caseevery X ppl"].mode()[0])
df["1 Deathevery X ppl"]=df["1 Deathevery X ppl"].fillna(df["1 Deathevery X ppl"].mode()[0])
df["1 Testevery X ppl"]=df["1 Testevery X ppl"].fillna(df["1 Testevery X ppl"].mode()[0])
df["Active Cases/1M pop"]=df["Active Cases/1M pop"].fillna(df["Active Cases/1M pop"].mode()[0])
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)


#7.Data Visualization (Matplotlib & Seaborn)
sb.histplot(x="TotalDeaths",data=df).set_title("Total_Death")
plt.show()
