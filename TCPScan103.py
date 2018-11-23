import threading
import time
import socket,subprocess,sys
import thread
import collections

#section 1
net = raw_input("Enter Network Address: ")
stl = int(raw_input("Enter the starting number: "))
enl = int(raw_input("Enter last number: "))
enl = enl + 1
dic = collections.OrderedDict()
net1 = net.split('.')
a='.'
net2 = net[0]+a+net[1]+a+net[2]+a
t1 = time.time()

#section 2
class myThread(threading.Thread):
    def __init__(self,st,en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en
    def run(self):
        run1(self.st,self.en)

#section 3
    def scan(addr):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = s.connect_ex((addr,135))
        if result ==0:
            s.close()
            return 1
        else:
            s.close()
            return 0

    def run1(stl,enl):
        for ip in xrange(stl,enl):
            addr = net2+str(ip)
            if scan(addr):
                dic[ip] = addr

#section 4
    total_ip = enl-stl
    tn = 20#number of ip handles by one thread
    total_thread = total_ip/tn
    total_thread = total_thread + 1
    threads = []
    try:
        for i in xrange(total_thread):
            print"i is ",i
            en  = stl + tn
            if (en > enl):
                en = enl
            thread = myThread(stl,en)
            thread.start()
            threads.append(thread)
            stl = en
    except:
        print("Error: Unable to start thread")
        print"\t Number of threads active:",threading.activeCount()
        for t in threads:
            t.join()
        print("Exiting Main Thread")
        dict = collections.OrderedDict(sorted(dic.items()))
        for key in dict:
            print(dict[key],"--> Live")
            t2 = time.time()
            total = t2 - t1
            print("Scanning complete in ",total,"seconds")
