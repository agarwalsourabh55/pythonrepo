import subprocess
a=input("enter the command you want to enter ")
f=open('com.txt','a+')
f.seek(0)
data=f.read()

if a in data:
     subprocess.getoutput('echo  "dont write same commnd" |festival --tts')
else:
    f=open('com.txt','a+')
    f.write(str(a))
    f.write('\n')
    f.close()

    if subprocess.getstatusoutput(a)[0] == 0:
         print(subprocess.getoutput(a))
    else:
        subprocess.getoutput('echo "command is incorrect" |festival --tts')

