class eCommerceApp :

    def __init__(self, username, passw, dict):
        self.username = username
        self.password = passw
        self.dict = dict

    def addMobile(self,qty):
        qty = self.dict["mobile"]+qty
        self.dict.update(mobile=qty)
        print(qty,"quantity added successfully")

    def addTablet(self,qty):
        qty = self.dict["tablet"]+qty
        self.dict.update(tablet=qty)
        print(qty, "quantity added successfully")

    def addTV(self,qty):
        qty = self.dict["TV"]+qty
        self.dict.update(TV=qty)
        print(qty, "quantity added successfully")

    def addMonitor(self,qty):
        qty = self.dict["monitor"]+qty
        self.dict.update(monitor=qty)
        print(qty, "quantity added successfully")
    def totalBill(self):
        total = (dict["mobile"]*15000 + dict["tablet"]*5000 + dict["TV"]*30000 + dict["monitor"]*20000)
        d= total - (total*0.05)
        if(total > 100000) :
            print("your have got 5% discount and the value is",d)
        else :
            print("your total billing value is",total)


dict = {"mobile":0,"tablet":0,"TV":0,"monitor":0}
B = eCommerceApp("omkar",1234,dict)


while True :
    u = input("please enter username")
    p = int(input("please enter password"))

    if u == B.username and p == B.password :
        print("Login successful")
        while True :
            a = int(input("please choose 1 to add mobile 2 for tablet 3 for TV 4 for monitor 5 for billing"))

            if a == 1 :
                qty =int(input("enter the quantity"))
                B.addMobile(qty)

            elif a == 2 :
                qty = int(input("enter the quantity"))
                B.addTablet(qty)
            elif a == 3:
                qty = int(input("enter the quantity"))
                B.addTV(qty)
            elif a == 4 :
                qty = int(input("enter the quantity"))
                B.addMonitor(qty)
            elif a == 5:
                B.totalBill()
            else :
                print("Invalid choice")
    else :
        print("Login failed please try again")