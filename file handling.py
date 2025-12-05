# --- create a new file----

# data=open("expo.txt","x")

# ---- create a new  file ("w")-----

# data=open("expo.txt","w")
# data.write("welcome to exponent")
# data.close()

# --- read data from file("r")----

# data=open("expo.txt","r")
# print(data.read())

# -- add new dada same file --

# data=open("expo.txt","a")
# data.write(" data engineering")
# data.close()

# data=open("expo.txt","r")
# print(data.read())


# with open("expo.txt","w")as f:
#     f.write("welcome to python")
#     f.close()
#
# with open("expo.txt","r") as f:
#     print((f.read())

# -- function declaration---
#
def test(f):
 with open(f,"r")as t:
                      data=t.readline()
                      for i in data:
                          print((i.split()))


 print(test("expo.txt"))
