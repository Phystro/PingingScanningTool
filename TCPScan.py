import socket
from datetime import datetime

net = raw_input("Enter the IP address: ")
net1 = net.split('.')
a='.'
net2 = net[0]+a+net[1]+a+net[2]+a
stl = int(raw_input("Enter the Starting Number: "))
enl = int(raw_input("Enter the Last Number: "))
enl=enl + 1

t1 = datetime.now()

def scan(addr):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    #ports=137,138,139(NetBIOSnameservice),445(Micrsoft-DSActiveDirectory) are usually open
    #for better results change port
    result = sock.connect_ex((addr,135))
    if result == 0:
        return 1
    else:
        return 0

def run1():
    for ip in xrange(stl,enl):
        addr = net2 + str(ip)
        if(scan(addr)):
            print(addr,"is live")

run1()
t2 = datetime.now()
total = t2 - t1
print("Scanning Complete in",total)
