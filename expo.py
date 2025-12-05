# username=input("enter your user_name=")
# password=int(input("enter your password="))
# balance=50000
# if username=="omkar" and password==1234:
#     print("welcome to hdfc bank")
#     print("1.credit 2.debit 3.forgot password 4.mini statement")
#     choice = int(input("enter your choice=="))
# class bank:
#     def credit(self):
#         if choice==1:
#             print("your option is credit")
#             accno = int(input("enter your accountno=="))
#             credit_amount = int(input("enter your credit_amount=="))
#             print("account number", accno, "is credited with", credit_amount)
#
#     def debit(self):
#         if choice==2:
#              print("your option is debit")
#              accno = int(input("enter your account=="))
#              debit_amount = int(input("enter your debit_amount=="))
#              print("account number", accno, "is debited with", debit_amount)
#     def forgotpassword(self):
#         if choice==3:
#             print("your option is forgotpassword")
#     def ministatement(self):
#         if choice==4:
#             print("your option is ministatement")
# a=bank()
# a.credit()
# a.debit()
# a.forgotpassword()
# a.ministatement()

#
# class Bank:
#     def _init_(self):
#         self.username = "ashok"
#         self.password = "ashok123"
#
#     def login(self):
#         username = input("Username: ")
#         password = input("Password: ")
#         if username == self.username and password == self.password:
#             print("Login successful!")
#             return True
#         else:
#             print("Invalid username or password")
#
#     def credit(self):
#
#         print("Your option is credit")
#         accno = int(input("Enter your account no: "))
#         credit_amount = int(input("Enter your credit amount: "))
#         print("Account number", accno, "is credited with", credit_amount)
#
#     def debit(self):
#
#         print("Your option is debit")
#         accno = int(input("Enter your account: "))
#         debit_amount = int(input("Enter your debit amount: "))
#         print("Account number", accno, "is debited with", debit_amount)
#
#         def forgotpassword(self):
#             print("Your option is forgot password")
#
#         def ministatement(self):
#             print("Your option is ministatement")
#
#     def main():
#         account = Bank()
#         if not account.login():
#             return
#
#         while True:
#             print("\nBanking Options:")
#             print("1. Credit")
#             print("2. Debit")
#             print("3. Forgot Password")
#             print("4. Mini Statement")
#             print("5. Exit")
#
#             choice = input("Enter your choice (1-5): ")
#         if choice == '1':
#             account.credit()
#         elif choice == '2':
#             account.debit()
#         elif choice == '3':
#             account.forgotpassword()
#         elif choice == '4':
#             account.ministatement()
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if _name_ == "_main_":
#     main()
#
#





class bankAccount :
    def _init_(self,username,passw,balance):
        self.username = username
        self.password = passw
        self.balance = balance

    def credit(self,amt):
        self.balance= self.balance + amt
        print(amt,"amount credited successfully")

    def debit(self,amt):
        if(amt<=self.balance):
            self.balance = self.balance - amt
            print(amt,"amount debited successfully")
        else :
            print("insufficient balance")
    def getbalance(self):
        print("current account balance is",self.balance)

B = bankAccount("harry",1234,10000)
while True :
    u = input("please enter username")
    p = int(input("please enter password"))

    if (u == B.username and p == B.password) :
        print("Login successful")
        while True :
            a = int(input("please choose 1 for credit 2 for debit and 3 for balance check"))

            if a == 1 :
                amt =int(input("enter the amount to credit"))
                B.credit(amt)
            elif a == 2 :
                amt = int(input("enter the amount to debit"))
                B.debit(amt)
            elif a == 3 :
                B.getbalance()
            else :
                    print("Invalid choice")
    else :
        print("Login failed")
