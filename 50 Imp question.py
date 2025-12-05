# 1.Write a python program to convert temperature from Fahrenheit to Celsius degrees.
# f=int(input("Enter value"))
# c=(f-32)*5/9
# print(c)
#
##2.write a python program that reads a number in inches and converts it to meters.
# i=int(input("enter value="))
# m=0.024*i
# print(m)

# #3.write a python program to convert minutes into years and days.
# # min=int(input("enter minutes="))
# # day=min/1440
# # print(day)
# #
# # year=min/(1440*365)
# # print(year)
#
# #4. Problem statement -
# # Enter username-
# # Enter password -
# # If username is swap and password is 1234
# # Then login successfully otherwise failed
#
#
# # username=input("enter username=")
# # password=int(input("enter password="))
# # if username=="swap" and password ==1234:
# #         print("login successfully")
# # else:
# #         print("login failed")
#
# #5.Write a Python program to count the number of even and odd numbers in a series of numbers.
#
# # def even_num():
# #      even_count=[]
# #      odd_count=[]
# #      for i in range(25):
# #              if i%2==0:
# #                      even_count.append(i)
# #              else:
# #                      odd_count.append((i))
# #      return f"The even no. is {len(even_count)},The odd no. is {len(odd_count)}"
# # print(even_num())
#
# # 6.Write a Python program to get the Fibonacci series between 0 and 50.
def fibo(n):
     a,b=0,1
     while a<=n:
         print(a,end=" ")
         a,b=b,a+b
     print()
fibo(50)

# # 7.Write a Python program that checks whether a specified value is contained within a group of values.
# # l=[2,4,8,9,11,14.15]
# # b=int(input("enter input"))
# # if b in l:
# #     print("number in list")
# # else:
# #     print("not in b")
#
#
# # 8.Write a Python program that will accept the base and height of a triangle and compute its area.
# # b=int(input("enter the base value"))
# # h=int(input("enter the height value"))
# # A=(b*h)/2
# # print(A)
#
#
# # 9.Write down function to find out whether given no is even and odd?
#
# # def check_even_odd(number):
# #     if number % 2 == 0:
# #         return "Even"
# #     else:
# #         return "Odd"
# # print(check_even_odd(15))
#
#
#
# # 10.Write down function to swap two values?
#
# # def swap_no(a,b):
# #     return b,a
# # print(swap_no(10,20))
#
# ##number divisible by 3, 5 or 7
# # n = int(input("enter number"))
# #
# # if n%3 == 0:
# #     print("divisible by 3")
# # elif n%5 == 0:
# #     print("divisible by 5")
# # elif n%7 == 0:
# #     print("divisible by 7")
# # else:
# #     print("not divisible by 3, 5 or 7")
#
# #construct pattern
# # n = int(input("enter number"))
# # i =1
# # while i<=n:
# #     j=1
# #     while j<=i:
# #         print("*",end="")
# #         j=j+1
# #     print()
# #     i=i+1
#
# #reverse string in python
# # word = input("enter the word")
# # reversed_word = word[::-1]
# # print(reversed_word)
#
# #calculate area of circle
# # r = int(input("enter radius"))
# # area = 3.14*r*r
# # print("area of circle is",area)
#
# #user's first name and last name and print in reverse order
# # fname = input("enter first name")
# # lname = input("enter last name")
# # print(lname,fname)
#
# #16.Write a Python program that accepts a sequence of comma-separated numbers
# # from the user and generates a list and a tuple of those numbers.
#
# # l=[]
# # while True:
# #     a=int(input("Enter the number"))
# #     if a==-1:
# #         break
# #     l.append(a)
# # b=tuple(l)
# #
# # print(l,type(l))
# # print(b,type(b))
#
# #17.Write a Python program that accepts a filename from the user and prints the extension of the file.
# # filename = input("Enter the filename: ")
# # extension = filename.split(".")[-1]\
# #     if "." in filename \
# #     else "No extension found"
# # print(f"The file extension is: {extension}")
#
# # #18.Write a Python program to display the first and last colors from the following list.
# # color_list = ["Red","Green","White" ,"Black"]
# # print(color_list[0],color_list[3])
#
# # 19.Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# # # Sample Output : The examination will start from : 11 / 12 / 2014
# # exam_st_date = (11, 12, 2014)
# # a=exam_st_date[0]
# # b=exam_st_date[1]
# # c=exam_st_date[2]
# # print(a,"/",b,"/",c)
#
# #20.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# # n=int(input("enter the value"))
# # print(n+n*n+n*n*n)
# #16
# # List = []
# # while True:
# #     s = input("enter something")
# #     if s == "-1" :
# #         break
# #     else :
# #         List.append(s)
# #
# # Tuple = tuple(List)
# # print(List, type(List))
# # print(Tuple, type(Tuple))
#
# #17
# # filename = input("enter filename")
# # count = 0
# # for i in filename:
# #     if i == ".":
# #         break
# #     count = count +1
# # print(filename[count:])
#
#
# #18
# # color_list = ["Red","Green","White" ,"Black"]
# # print(color_list[0],color_list[3])
#
# #19
# # exam_st_date = (11, 12, 2014)
# # day = exam_st_date[0]
# # month = exam_st_date[1]
# # year = exam_st_date[2]
# # print(day,"/",month,"/",year)
#
# #20
# # n = int(input("enter number"))
# # result = n + n*n + n**3
# # print(result)
#
# #21.Write a Python program that prints the calendar for a given month and year.
#            # Note : Use 'calendar' module.
# # import calendar
# # years=int(input("enter the years"))
# # months=int(input("enter the months"))
# # print(calendar.month(years,months))
#
# # 22.Write a Python program to calculate the number of days between two dates.
# # Sample dates : (2014, 7, 2), (2014, 7, 11)
# # Expected output : 9 days
#
# # from datetime import date
# # date1=date(2014,7,2)
# # date2=date(2014,7,11)
# # print(date2-date1)
#
# #23.Write a Python program to get the volume of a sphere with radius six.
#
# # radius = 6
# # volume=(4/3)3.14(radius**3)
# # print("volume of Sphere having radius 6 =",volume)
#
# # 24.Write a Python program to calculate the difference
# # between a given number and 17. If the number
# # is greater than 17, return twice the absolute difference.
#
# # def difference(n):
# #     if n<=17:
# #         return 17-n
# #     else:
# #         return(n-17)*2
# # print(difference(25))
#
# #25.Write a Python program to test whether a number is within 100 of 1000 or 2000.
#
#
# # 26.Write a Python program to sum three given integers. However,
# # if two values are equal, the sum will be zero.
# # a=10
# # b=10
# # c=30
# # if a==b or b==c or c==a:
# #     print(0)
# # else:
# #     print(a+b+c)
#
# # #27.Write a Python function to multiply all the numbers in a list.
# # a=1
# # list=[1,4,6,8]
# # for i in list:
# #     a*=i
# # print(a)
#
# # 28.Write a Python program to reverse a string.
# #
# # Sample String: "1234abcd"
# # Expected Output: "dcba4321”
# # str = input("enter something")
# # i = len(str)-1
# # newstring = ""
# # while i>=0:
# #     newstring = newstring + str[i]
# #     i=i-1
# # str = newstring
# #
# # print(str)
#
# #29.Write a Python function to check whether a number falls within a given range
# # def in_range(num, start, end):
# #     return start <= num <= end
# #     True
# # print(in_range(1, 1, 10))
#
# #30.Write a Python function to find the maximum of three numbers
# # a = 50
# # b = 20
# # c = 30
# # if a>=b and a>=c :
# #     print(a,"is greatest")
# # elif b>=a and b>=c:
# #     print(b,"is greatest")
# # else:
# #     print(c,"is greatest")
#
# # a = int(input("enter first number"))
# # b = int(input("enter second number"))
# # c = a+b
# # if c>=15 and c<=20:
# #     print(20)
# # else:
# #     print(c)
#
# #32
# # a = input("Enter something")
# # # try :
# # #     int(a)
# # #     print(a,"is number")
# # #
# # # except ValueError:
# # #     print("not a number")
#
# # 33
# # day = int(input("enter day"))
# # month = input("enter month")
# #
# # if (month == "dec" and day >= 21) or month in ["jan", "feb"] or (month == "mar" and day < 20):
# #     season = "Winter"
# # elif (month == "mar" and day >= 20) or month in ["apr", "may"] or (month == "jun" and day < 21):
# #     season = "Spring"
# # elif (month == "jun" and day >= 21) or month in ["jul", "aug"] or (month == "sep" and day < 22):
# #     season = "Summer"
# # elif (month == "sep" and day >= 22) or month in ["oct", "nov"] or (month == "dec" and day < 21):
# #     season = "Autumn"
# # else:
# #     season = "Invalid input"
# #
# # print("Season:",season)
#
# #34
# # a = int(input("enter first number"))
# # b = int(input("enter second number"))
# # c = int(input("enter third number"))
# # median= 0
# # if a>=b and a>=c:
# #     if b>=c:
# #         median = b
# #     else:
# #         median = c
# # elif b>=c and b>=a:
# #     if a>=c:
# #         median = a
# #     else:
# #         median = c
# # else:
# #     if a>=b:
# #         median = a
# #     else :
# #         median = b
# #
# # print("median is",median)
#
# #35
# # number = int(input("enter number"))
# # if number>= 0:
# #     print("positive number")
# # else :
# #     print("negative number")
#
# #36.Write a program to check if the given number is palindrome or not.
# # s = 'nayan' #string
# # if s == s[::-1]:
# #     print("Yes")
# # else:
# #     print("No")
#
# #37.Write a program to check if the given number is Armstrong or not.
# # num=input("Enter a number:")
# # length=len(num)
# # #print(length)
# # sum=sum(int(digit)**length for digit in num)
# # print(sum)
# # if sum==int(num):
# #     print("armstrong")
# # else:
# #     print("NOT armstrong")
#
# #38.Write a program to check if the given strings are anagram or not
# # s1="listen"
# # s2="silent"
# # if sorted(s1)==sorted(s2):
# #     print("yes")
# # else:
# #     print("NO")
#
# # #39.Write a program to find a maximum of two numbers.
# # a=50
# # b=20
# # c=max(a,b)
# # print(c)
#
# ##40.Write a program to find a minimum of two numbers.
# # a=30
# # b=78
# # c=min(a,b)
# # print(c)
#
# #38.
# # dict1 ={}
# # dict2 ={}
# # a = input("enter first string")
# # b = input("enter second string")
# # for  i in a:
# #     if i not in dict1:
# #          dict1[i]=1
# #     else:
# #         dict1[i] = dict1[i]+1
# # for  j in b:
# #     if j not in dict2:
# #          dict2[j]=1
# #     else:
# #         dict2[j] = dict2[j]+1
# #
# # if dict1 == dict2 :
# #     print("strings are anagram")
# # else :
# #     print("strings are not anagram")
#
#
# # 41.Write a program to find a maximum of three numbers.
# def find_maximum(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(find_maximum(25,69,63))
#
# # 42.Write a program to find a minimum of three numbers.
#
# # def find_minimum(a, b, c):
# #     if a <= b and a <= c:
# #         return a
# #     elif b <= a and b <= c:
# #         return b
# #     else:
# #         return c
# # print(find_minimum(96,75,23))
#
# # 43.Write a program to find a factorial of a number.
# # def factorial(n):
# #     return 1 if n==0 else n*factorial(n-1)
# # print("factorial is ",factorial(5))
#
# # 44.Write a program to find GCD of two numbers.
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=min(a,b)
# d=1
# for i in range(2,c+1):
#     if a%i==0 and b%i==0:
#         d=i
# print(d)
#
# # 45.Write a program to print the following pattern.
# # 1
# # 1 2
# # 1 2 3
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# # 46.Write a Python program to find the largest element in a list.
# list=[1,34,67,9,45,67,99]
# b=sorted(list)[-1]
# print(b)
#
# # 47.Write a Python program to count the frequency of each element in a list
# d={}
# l=["apple","banana","orange","apple","banana"]
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
#
#
#
# # 48.Write a Python program to find the common elements between two lists.
# a=[1,3,5,7,9,33,20]
# b=[33,5,99,56,44,8]
# c=set(a)
# d=set(b)
# print(c.intersection(d))
#
# # 49.Write a Python program to find the second largest number in a list.
# l=[1,2,5,7,9,3,4,7,34,67,77]
# l.remove(max(l))
# print(max(l))
#
# 50.Write a Python program to remove duplicates from a list.
# list=[1,34,6,1,9,8,6,5,6]
# d=set(list)
# print(d)