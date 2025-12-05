#
# username="omkar"
# password=123
# balance=10000
# while True:
#     uname=input("enter your uname")
#     pin=int(input("enter your pin"))
#     if username==uname and password==pin:
#         print("login successfully")
#         while True:
#             aa=int(input("enter your choice 1.credit 2.debit 3,statement"))
#             if aa==1:
#                 print("your choice is credit")
#                 amount=int(input("enter your amount you want to credit"))
#                 balance=balance+amount
#                 print("amount credit successfully")
#             elif aa==2:
#                 print("your choice is debit")
#                 amount=int(input("enter your amount you want to debit"))
#                 if amount>balance:
#                     print("insufficient found")
#                 else:
#                   balance=balance-amount
#                   print("amount debit successfully")
#
#             elif aa==3:
#                 print("your choice is statement")
#                 print("your account balance is",balance)
#     else:
#             print("login failed")
#
#

# abstraction
# opps
# class Bank:                                     #abstraction
#     def _init_(self,balance):
#         self.balance=balance
#
#     def credit(self,balance):
#         self.balance = self.balance +balance
#
#     def debit(self,balance):
#         self.__debitamount(balance)
#
#     def __debitamount(self,balance):                #private method
#         if(balance <= self.balance):
#             self.balance = self.balance - balance
#         else:
#             print("insufficient funds")
#
#     def getbalance(self):
#         print("the account balance is",self.balance)
#
# c=bank (1000)
# c.getbalance()
#
# c.credit(5000)
# c.getbalance()
#
# c.debit(17000)
# c.getbalance()
#
# c.debit(13000)
# c.getbalance()
#
# class PrintSomething:                                     #encapsulation
#
#     def fruits(self):
#         print("I like orange")
#
#     def veges(self):
#         print("I like brinjal")
#
# c = PrintSomething()
# c.fruits()
# c.veges()


# Multiple Inheritance
#
# class Father :               #parent class
#     def height(self):
#         print("I am tall")
#
# class Mother :                 #parent class
#     def skincolor(self):
#         print("Skin color is fair")
#
# class Son(Father,Mother) :       #child class
#     def haircolor(self):
#         print("hair color is blonde")
#
# x = Son()
# x.height()
# x.skincolor()
# x.haircolor()

#  Multi level inheritance
# class Grandfather :               #parent class    #
#     def height(self):
#         print("I am tall")
#
# class Father(Grandfather) :                 #parent class
#     def skintype(self):
#         print("I am skinny")
#
# class Son(Father) :       #child class
#     def haircolor(self):
#         print("hair color is blonde")
#
# x = Son()
# x.height()
# x.skintype()
# x.haircolor()

# class MethodOverLoading :   #method overloading
#
#     def hello(self, a=None):
#         if a is None :
#             print("this has no param")
#         else :
#             print("value is somethng",a)
#
# c = MethodOverLoading()
# c.hello()
# c.hello("banana")

class Parent():                         #method overriding
    def height(self):
        print(" I am tall")

class Child(Parent):

    def height(self):
        print("I am short")

c = Child()
c.height()

