# import pandas
# import numpy as np
# import matplotlib.pyplot as plt
# import openpyxl
# import duckdb
# df1=pandas.read_csv(r"C:C:\omkar\Book1.xlsx")
#
# # print(df1)
# # # A. Find the number of movies released between 1950 and 1960.
# # d=duckdb.query("select  Moviename,ANY_VALUE(Yearofrelease) as t from df1 where Yearofrelease>=1950 and Yearofrelease<=1960 group by Moviename order by Moviename limit 5").df()
# # print(d)
# # a=d["Moviename"].to_numpy()
# # b=d["t"].to_numpy()
# # x=np.array(a)
# # y=np.array(b)
# # font1={"family":"serif","color":"red","size":10}
# # font2={"family":"serif","color":"blue","size":10}
# # plt.xlabel("Moviename",font1,loc="right")
# # plt.ylabel("Yearofrelease",font1,loc="top")
# # plt.subplot(2,1,2)
# # plt.title('first graph')
# # plt.bar(x,y)
# #
# #
# # # # B. Find the number of movies having rating more than 4.
# # # e=duckdb.query("select
# def add(a, b):
#     return a + b
# result = add(5, 3)
# print(result)


# def add(a,b):
#     return a+b
# print(add(5,3))
# print(add(25,41))

# def multiply(a,b):
#      return a*b
# result=multiply(4,5)
# print(result)

# def greet(name,age):
#     print(f"hello {name},you are {age} year old")
# greet(name="omkar",age="25")
# print(greet)

#
# def greet(name="omkar"):
#     print("hello",name)
# greet(name="rani")
# my_list = ["apple", "banana", "cherry"]
# def display_item(items):
#     for item in items:
#      print(item)
# display_item(my_list)



# l = ["apple", "banana", "cherry"]
# def test(food):
#     for i in food:
#         print(i)
# (test(l))


# def sarva_add(*args):
#     total=0
#     for num in args:
#         total +=num
#     print(total)
# aa=sarva_add(10,20,30)

def aa(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
aa(name="ashok",age=25)

