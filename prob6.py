#first make cat. as a alias of python3 prob6.py
#then write cat. file_name on command line 

import sys

Q="%s"% str(sys.argv[1])

f=open(Q,'r')
data=f.read()
print(data)
f.close()


