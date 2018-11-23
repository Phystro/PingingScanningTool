import socket,subprocess,sys,select
from time import time

def randomScan():
    subprocess.call('clear',shell=True)
    rmip = raw_input("\r\nRemote IP to Scan:- ")
    r1 = int(raw_input("Start Port Number:- "))
    r2 = int(raw_input("Last Port Number:- "))
    t = float(raw_input("Specify Default Time Out:- "))
    r2 = r2 + 1
    print "\r\n*"*40
    print "Scanner is working on ",rmip,"\r\nFrom Ports:",r1,"to",r2-1
    print"*"*40

    t1 = time()

    for port in range(r1,r2):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(t)
        try:
            result = sock.connect_ex((rmip,port))
            name = socket.getservbyport(port)
            if result==0:
                print "[+]",port,"-",name,"\t--> Open"
                sock.close()
            else:
                print "[-]",port,"-",name,"\t--> Closed"
                #print desc[port]
                sock.close()
        except KeyboardInterrupt:
            print"[!] [Error] You Stopped This"
            sys.exit()
        except socket.gaierror:
            print"[!] [Error]",port,"Hostname could not be resolved"
        except socket.error:
            print"[!] [Error]",port,"Could not connect to server"
    t2=time()

    total = t2-t1
    print("Scanning complete in ",total)

def specificScan():
    ip = raw_input("\r\nEnter IP Address:- ")
    #port 5555/5556 for UAVs
    ports=[7,20,21,22,23,25,42,53,68,69,80,88,110,111,123,135,137,138,139,143,
           161,162,179,389,443,445,514,636,912,1080,1241,1433,1434,8080,1023,
           1024,1494,2598,1521,2512,2513,3306,3389,5432,5555,5556,6662,6663,
           6664,6665,6666,6667,6668,6669,49151,65536]
    for port in ports:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2.4)
        try:
            res=s.connect_ex((ip,port))
            name=socket.getservbyport(port)
            if res==10061:
                print "[-]",port,"-\t",name,"\t:",res,"--> Closed"
            elif res==0:
                print "[+]",port,"-\t",name,"\t:",res,"--> Open"
                #banner(ip,port)
            s.close()
        except:
            print "[!] [Error]",port,"-\t",name,"\t:",res,": port/proto not found"
            continue
def banner():
    #python sockets to acquire service banners to identify services associated with open ports on target
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = raw_input("\r\nEnter IP Address:- ")
    port = int(raw_input("Enter Port:- "))
    try:
        try:
            socket.setdefaulttimeout(5)
            s.connect((ip,port))
        except:
            print("[-] [Error] Either No Route To Host or Connection Refused")
        else:
            s.send('mw40.home\r\n')
            #arguments to object include:
            #select.select([read list], [write list], [exception list], timeout)
            ready = select.select([s],[],[],5)
            if ready[0]:
                answ=s.recv(1024)
                print "IP: %s at Port: %s >>"%(ip,port)
                print(answ)
            else:
                print("[-] No Banner")
    except KeyboardInterrupt:
        print "[!] You Stopped This"
        sys.exit()
    
if __name__=="__main__":
    while 1:
        ex=raw_input("\r\n'c' to Start/Continue\t'q' to Quit/Exit\r\n:- ")
        ex=ex.lower()
        if ex=='q':
            sys.exit()
        else:
            #randomScan()
            specificScan()
            #banner()
