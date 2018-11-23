import socket,sys,subprocess,collections,thread,time,os

def tcpscan():
    net = raw_input("\r\nEnter IP Address:- ")
    net1 = net.split('.')
    #print(net1)
    a='.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    #print(net2)
    stl = int(raw_input("Starting Number:- "))
    enl = int(raw_input("Later member:- "))
    enl = enl + 1

    def scan(addr):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = s.connect_ex((addr,135))
        if result == 0:
            s.close()
            print "[+]",addr,"--> Open"
            return 1
        else:
            s.close()
            print "[-]",addr,"--> closed"
            return 0
        
    def run(stl,enl):
        for ip in xrange(stl,enl):
            addr = net2+str(ip)
            scan(addr)
            #if scan(addr):
                #dic[ip] = addr
    run(stl,enl)
