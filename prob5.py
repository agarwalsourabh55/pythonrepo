from datetime import datetime
name=input("enter your name")
now=datetime.now()
time=now.strftime("%H")
if int(time) > 22 :
    print("good night "+name)
if int(time) > 0 and  int(time) < 5:
    print("good night"+name)
if int(time) > 5 and int(time) < 12:
    print("good morning"+name)
if int(time) > 12 and int(time) < 16:
    print("good afternoon"+name)
if int(time) > 16 and int(time) < 22:
    print("good evening"+name)


