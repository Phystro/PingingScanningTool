import os
import collections
import platform
import socket,subprocess,sys
import threading
from time import time

#section 1
net = raw_input("Enter the Network Address ")
net1 = net.split('.')
a='.'
net2 = net1[0]+a+net[1]+a+net[2]+a
st = int(raw_input("Enter the Starting Number: "))
en = int(raw_input("Enter the Last Number: "))
en = en + 1
dic = collections.OrderedDict()
oper = platform.system()

if(oper == "Windows"):
    ping1 = "ping -n 4 "
elif(oper == "Linux"):
    ping1 = "ping -c 4 "
else:
    ping1 = "ping -c 4 "

t1=time()

#section 2
class myThread(threading.Thread):
    def __init__(self,st,en):
        threading.Thread.__init__(self,st,en)
        self.st = st
        self.en = en
    def run(self):
        run1(self.st,self.en)

#section 3
    def run1(stl,enl):
        print("Scanning in progress")
        for ip in xrange(stl,enl):
            print(".")
            addr = net2 + str(ip)
            comm = ping1+addr
            response = os.popen(comm)
            inf = response.readlines()
            for line,i in enumerate(inf):
                if(line.count("TTL")):
                    break
            if(line.count("TTL")):
                print(addr,"--> Live")
                dic[ip] = addr

#section 4
    total_ip = en-st
    tn = 20 #number of ip handled by on thread
    total_thread = total_ip/tn
    total_thread = total_thread + 1
    threads = []

    try:
        for i in xrange(total_thread):
            en = st + tn
            if(en > en):
                en=en
            thread = myThread(st,en)
            thread.start()
            threads.append(thread)
            stl = en
    except:
        print("Error: unable to start thread")
        print "\t Number of Threads active:",threading.activeCount()

    for t in threads:
        t.join()
    print("Exiting Main Thread")
    dict = collections.OrderedDict(sorted(dic.items()))
    for key in dict:
        print dict[key],"--> Live"

    t2 = time()
    total = t2 - t1
    print"Scanning Comlete in",total,"seconds"

myThread(threading.Thread).run()
