import os
a=input("enter the no.")
if a.isalpha():
    str1="hello"
    print("true")
    def addnewuser():

    upass=str1+a

    os.system("useradd -m -p "+upass+" "+a)

    addnewuser()




