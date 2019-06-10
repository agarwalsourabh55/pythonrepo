import datetime 
a=input("enter your name ")
b=int(input("enter your age"))

c=95 - b
d=datetime.datetime.now()
if c > 0 :
    print("you will turn 95 by year ")
    print( c + d.year )
else :
    print("you are already older then 95")


