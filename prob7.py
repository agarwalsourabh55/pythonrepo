#make alias of python3 prob7.py
#and run the command
#create a single file 
import sys
f=open(sys.argv[1],'w+')
f.close()
#create multiple file 
var=len(sys.argv)
for i in range(var-2):
    s=str(sys.argv[i+2])
    f=open(s,'w+')
f.close()


         

