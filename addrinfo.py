import socket
def info():
    def ipn(ip):
        try:
            ipdname=socket.getfqdn(ip)
            ipname=socket.gethostbyname_ex(ipdname)
        except:
            print("connect:Check Internet Connection")
            pass
        else:
            print "\r\nDomain Name.........:",ipdname
            print "Hostname............:",ipname[0]
            print "Canonical Names.....:",ipname[1]
            print "IP Address List.....:",ipname[2]
            #connect(ip)
    def domain(url):
        try:
            urldname=socket.getfqdn(url)
            urlname=socket.gethostbyname_ex(urldname)
        except:
            print("connect:Check Internet Connection")
            pass
        else:
            print "\r\nDomain Name.........:",urldname
            print "Hostname............:",urlname[0]
            print "Canonical Names.....:",urlname[1]
            print "IP Address List.....:",urlname[2]
            #connect(url)
    def connect(host):
        ports=[7,20,21,22,23,25,53,68,69,80,110,135,137,138,139,143,179,443,445,912,1080,8080,1023,1024,3306,6665,6666,6667,6668,6669,49151,65535]
        for port in ports:
            try:
                portname=socket.getservbyport(port)
            except:
                portname=None
                pass
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result=s.connect_ex((host,port))
            if result==0:
                print "Service Name: %s\tPort: %d\t: ",result,"--> Open"%(portname,port)
        else:
            print "[-] Useful Ports Closed"
            s.close()
            
    socket.setdefaulttimeout(2)
    myhost = socket.gethostbyname_ex(socket.gethostname())
    print "\r\n",myhost[0],"-",myhost[1],"-",myhost[2]

    print("Choose Option:")
    print("\t1)IP Address\r\n\t2)Url/Domain Name")
    choice = raw_input(":-")
    if choice=="1":
        ip=raw_input("Enter IP Address: ")
        ipn(ip)
    elif choice=="2":
        url=raw_input("Enter Domain Name: ")
        domain(url)      
    else:
        print("Wrong Input")
        info()   
    
    
if __name__=="__main__":
    while 1:
        info()
