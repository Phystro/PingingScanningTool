import os,platform,socket,addrinfo,TCPScanner,portScanner
from time import time
__version__="1.2"

def pingscan():
        def startPing(pinger, index1, index2):        
                print("\r\nInitializing Scan...\r\nSending packets of ICMP ECHO request awaiting ICMP ECHO reply...\r\n")
                print "Scanning",enl-stl,"IP addresses from:\
                \r\n\t\t",net2+str(stl),"-",net2+str(enl-1),"\n"
                t1 = time()

                for ip in xrange(stl,enl):
                        addr = str(net2) + str(ip)
                        comm = ping1+addr
                        resp = os.popen(comm)
                        inf = resp.readlines()
                        if inf[:] != []:
                                if inf[2].count('ttl'):
                                        print "[+]",addr+" ,"+inf[index1].strip(" ").strip("\n"),"--> Live"
                                else:
                                        print "[-]",addr+" ,"+inf[index2].strip(" ").strip("\n")
                        elif inf[:]==[]:
                                print("Unable to ping!!Check Internet Connection!!")
                t2 = time()
                total = t2-t1
                total=str(total)
                print "Scanning Complete in ",total+" seconds"
                
        net = raw_input("\r\nEnter IP Address:- ")
        net1 = net.split('.')
        a='.'
        net2 = net1[0]+a+net1[1]+a+net1[2]+a
        stl = int(raw_input("Starting Number\t:- "))
        enl = int(raw_input("Ending Number\t:- "))
        enl = enl + 1
        packs = raw_input("Packets To Send\t:- ")

        socket.setdefaulttimeout(0.02)
        oper = platform.system()
        if (oper == "Windows"):
                ping1 = "ping -n "+packs+" "
                startPing(ping1, -3, -1)
        elif (oper == "Linux"):
                ping1 = "ping -c "+packs+" "
                startPing(ping1, -2, -2)
        else:
                ping1 = "ping -c "+packs+" "
                startPing(ping1, -2, -2)

if __name__=="__main__":
        while 1:
            print ("\n\tPINGING SCANNING TOOL\r\n")
            print ("Select From The Menu:")
            print ("  1) PingSweep IP Address")
            print ("  2) Scan IP Addresses' Most Useful Ports")
            print ("  3) Get IP Address Info")
            print ("  4) TCP/IP Address Scan")
            print ("  5) Random/Full IP Address Port Scan")
            print ("  6) Application Banner Grabbing")
            print ("  'q' to Quit/Close")
            nxt = raw_input("\r\npst:- ")
            nxt=nxt.lower()
            if nxt == '1':
                print("\r\n\t***...PingSweep IP Addresses...***")
                pingscan()
            elif nxt == '2':
                print("\r\n\t***...Scan IP Addresses' Useful Ports...***")
                portScanner.specificScan()
            elif nxt == '3':
                print("\r\n\t***...Get IP Address Information...***")
                addrinfo.info()
            elif nxt == '4':
                print("\r\n\t***...TCP/IP Address Scan...***")
                TCPScanner.tcpscan()
            elif nxt == '5':
                print("\r\n\t***...Random/Full IP Address Port Scan...***")
                portScanner.randomScan()
            elif nxt == '6':
                print("\r\n\t***...Application Banner Grabbing...***")
                portScanner.banner()
            elif nxt == 'help' and nxt.startswith('help'):
                print('\r\n[Error] "help" not Available at the moment\r\nEverything is crystal clear\r\n[-] Try Again Later')
            elif nxt == 'q':
                print("Thank You and Good-Bye...")
                break
                os.close(0)
