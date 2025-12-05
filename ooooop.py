# from fontTools.merge.base import mergeObjects
#
#
# class eCommerceApp:
#     def __init__(self,username, password, dict):
#         self.username=username
#         self.password=password
#         self.card={"Mobile":0, "Tablet":0, "TV":0, "Monitor":0,"Belling":0}
#         # self.totalbil={"Mobile":15000, "Tablet":5000 ,"TV":30000, "Monitor":20000}
#
#   def Mobile(self):
#         print("your choice is mobile")
#         quantity=int(input("enter your Quantithy="))
#         addtocart=input("do you want to Add to cart?=")
#         if addtocart=="yes":
#            d.update(mobile=quantity)
#         else:
#             quantity=int(input("please enter your quantity"))
#             addtocart=input("do you want to add to cart?=")
#             d.update(Mobile=quantity)
#
#
#   def Tablet(self):
#     print("your choice is mobile")
#     quantity = int(input("enter your Quantithy="))
#     addtocart = input("do you want to Add to cart?=")
#     if addtocart == "yes":
#         d.update(Tablet=quantity)
#     else:
#         quantity = int(input("please enter your quantity"))
#         addtocart = input("do you want to add to cart?=")
#         d.update(Tablet=quantity)
#   def Moniter(self):
#     print("your choice is mobile")
#     quantity = int(input("enter your Quantithy="))
#     addtocart = input("do you want to Add to cart?=")
#     if addtocart == "yes":
#         d.update(Moniter=quantity)
#     else:
#         quantity = int(input("please enter your quantity"))
#         addtocart = input("do you want to add to cart?=")
#         d.update(Moniter=quantity)
#
#   def Tv(self):
#     print("your choice is mobile")
#     quantity = int(input("enter your Quantithy="))
#     addtocart = input("do you want to Add to cart?=")
#     if addtocart == "yes":
#         d.update(Tv=quantity)
#     else:
#         quantity = int(input("please enter your quantity"))
#         addtocart = input("do you want to add to cart?=")
#         d.update(Tv=quantity)
#
#
# class eCommerceApp :
#
#     def _init_(self,username,passw,dict):
#         self.username = username
#         self.password = passw
#         self.dict = dict
#
#     def addMobile(self,qty):
#         qty = self.dict["mobile"]+qty
#         self.dict.update(mobile=qty)
#         print(qty,"quantity added successfully")
#
#     def addTablet(self,qty):
#         qty = self.dict["tablet"]+qty
#         self.dict.update(tablet=qty)
#         print(qty, "quantity added successfully")
#
#     def addTV(self,qty):
#         qty = self.dict["TV"]+qty
#         self.dict.update(TV=qty)
#         print(qty, "quantity added successfully")
#
#     def addMonitor(self,qty):
#         qty = self.dict["monitor"]+qty
#         self.dict.update(monitor=qty)
#         print(qty, "quantity added successfully")
#
#     def totalBill(self):
#         total = (dict["mobile"]*15000 + dict["tablet"]*5000 + dict["TV"]*30000 + dict["monitor"]*20000)
#               ["monitor"]*20000)
#         d= total - (total*0.05)
#         if(total > 100000) :
#             print("your have got 5% discount and the value is",d)
#         else :
#             print("your total billing value is",total)
#
#
# dict = {"mobile":0,"tablet":0,"TV":0,"monitor":0}
# B = eCommerceApp("harry",1234,dict)
#
#
# while True :
#     u = input("please enter username")
#     p = int(input("please enter password"))
#
#     if u == B.username and p == B.password :
#         print("Login successful")
#         while True :
#             a = int(input("please choose 1 to add mobile 2 for tablet 3 for TV 4 for monitor 5 for billing"))
#
#             if a == 1 :
#                 qty =int(input("enter the quantity"))
#                 B.addMobile(qty)
#
#             elif a == 2 :
#                 qty = int(input("enter the quantity"))
#                 B.addTablet(qty)
#             elif a == 3:
#                 qty = int(input("enter the quantity"))
#                 B.addTV(qty)
#
#
# numbers = [1, 2, 3, 4, 5, -1, 11,7]
# for num in numbers:
#     if num < 0:
#         print("Negative number found! Exiting loop.")
#         continue
#     print(num)
#
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(fruit)
# for i in range(len(fruits)):
#     print(f" Fruit: {fruits[i]}")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
#
numbers = [1, 2, 0, 4, 0, 6]
for num in numbers:
  if num == 0:
    print("Skipping zero.")
    continue
  print(num)