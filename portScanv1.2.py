import threading,socket,subprocess,sys,thread,shelve
from time import time

subprocess.call('clear',shell=True)#works in linux to clear screeen
#database file that stores port info
shelf = shelve.open("karoki.kar",writeback=True)
shelf['desc']={}
shelf.close()
print("Dic Created")

class myThread(threading.Thread):
    def __init__(self,threadName,rmip,r1,r2,c):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.rmip = rmip
        self.r1 = r1
        self.r2 = r2
        self.c = c
    def run(self):
        scantcp(self.threadName,self.rmip,self.r1,self.r2,self.c)

    def scantcp(threadName,rmip,r1,r2,c):
        try:
            for port in range(r1,r2):
                sock=socket,socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimenout(c)
                result = sock.connect_ex((rmip,port))

                if result==0:
                    print"port open:-->",port,"==",data.get(port,"Not in Database")
                    sock.close()
        except KeyboardInterrupt:
            print("You Stopped This")
            sys.exit()

        except socket.gaierror:
            print("Hostname could not Be Resolved")
            sys.exit()
        except socket.error:
            print("could not connect to serve")
            sys.exit()
            
        shelf.close()
    print"*"*60
    print"\tWelcome to port scanner\n"
    d=raw_input("\tPress D for Domain Name or I for IP Address\t")
    if(d=='D' or d=='d'):
        rmserver = raw_input("\tDomain name to scan:-\t")
        rmip = socket.gethostbyname(rmserver)
    elif(d=='I' or d=='i'):
        rmip = raw_input("\tIP Address to scan: ")
    else:
        print("Wrong Input")
    r11=int(raw_input("\tStart port number:\t"))
    r21=int(raw_input("\tlast port number:\t"))
    conect=raw_input("For Low Connectivity press L and High connectivity press H\t")
    if(conect=='L' or conect=='l'):
        c=1.5
    elif(conect=='H' or conect=='h'):
        c=0.5
    else:
        print"Wrong Input"
    print("\nScanner working on ",rmip)
    print"*"*60
    t1=time()
    tp=r21-r11

    tn = 30#number of ports handled by one thread
    tnum = tp/tn#number of threads
    if(tp%tn != 0):
        tnum = tnum + 1

    if(tnum > 300):
        tn = tp/300
        tn = tn + 1
        tnum = tp/tn
        if(tp%tn != 0):
            tnum = tnum  + 1
    threads = []
    try:
        for i in range(tnum):
            k = i
            r2 = r11 + tn
            thread = myThread("T1",rmip,r11,r2,c)
            thread.start()
        threads.append(thread)
        r11 = r2
    except:
        print("Error: unable to start thread")
    print"\t Number of threads active:",threading.activeCount()

    for t in threads:
        t.join()
    print"Exiting Main Thread"
    t2 = time()

    total = t2 - t1
    print("Scanning complete in ",total)
