#!usr/bin/python3
import os
a=int(input("Enter a number of directories you want to make "))
for i in range(1,a+1):
    try:
        os.mkdir(input())
    except:
        print("Already Exist")


         


