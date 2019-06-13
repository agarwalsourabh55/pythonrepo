from qrtools import QR
my_QR=QR(filename="sou.png")
my_QR.decode()
print(my_QR.data)

