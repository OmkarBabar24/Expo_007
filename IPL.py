import numpy as np
import duckdb
import duckdb as db
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List, Tuple, Dict, Union

from fontTools.misc.psLib import suckfont

data= pd.read_csv("C:\\Users\\prati\\Downloads\\fifa data.csv")
# print(data)
# print(data.describe())
# data=data.duplicated()
# print(data.isnull().sum())
# print(data.head(25))


match= pd.read_csv("C:\\Users\\prati\\Downloads\\matches (1).csv")
# print(match)

aa=duckdb.query("select count(winner) as winners,winner from match group by winner order by winners desc").to_df()
# print(aa)
# aa = aa.dropna(subset=["winner", "winners"])
#
# # नंतर plotting करा
# plt.bar(aa["winner"], aa["winners"])
# plt.xticks(rotation=30)
# plt.show()

# a=duckdb.query("select count(result) as results,result from match group by result order by results desc")
# print(a)

b=duckdb.query("select count(player_of_match)as player,player_of_match from match group by  player_of_match order by player desc limit 5").to_df()
# print(b)
#
# plt.pie(b["player"],labels=b["player_of_match"],autopct='%1.1f%%')
# plt.show()


zz=duckdb.query("select count(toss_winner) as winner,toss_winner from match group by toss_winner order by winner desc")
# print(zz)

df1=duckdb.query("SELECT winner,COUNT(*) AS wins_after_batting_second FROM match WHERE toss_decision = 'bat' AND result = 'normal' AND winner = toss_winner GROUP BY winner ORDER BY wins_after_batting_second DESC").to_df()
print(df1)


df2=duckdb.query("select count (venue) as venues,venue from match group by venue limit 5 ")
print(df2)