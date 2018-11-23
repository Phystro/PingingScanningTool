import socket,time

def info():
    def protnumber(prefix):
        return dict((getattr(socket,a),a)
            for a in dir(socket)
                if a.startswith(prefix))

    proto_fam = protnumber("AF_")
    types = protnumber("SOCK_")
    protocols = protnumber("IPPROTO_")
    socket.setdefaulttimeout(1.6)
    myhost=socket.gethostbyname_ex(socket.gethostname())
    
    print "\r\nHOST: ",myhost[0]," - ",myhost[1]," - ",myhost[2]
    
    choice = raw_input("\r\nChoose Option:\n\t1)IP Address\n\t2)Domain Name\r\n:- ")
    if choice=='1':
        ipaddr = raw_input("\r\nIP Address:- ")
        try:
            dname=socket.getfqdn(ipaddr)
        except:
            print("\r\nconnect:Check Your Internet Connection\r\n")
            pass
    elif choice=='2':
        dnaddr = str(raw_input("\r\nDomain Name:- "))
        try:
            dnaddrname=socket.getfqdn(dnaddr)
        except:
            print("\r\nconnect:Check Your Internet Connection\r\n")
            pass
    else:
        print"Wrong Input"
        info()
    reqport = raw_input("Protocol eg.'http','ftp','smtp' etc:- ").lower()
    
    try:
        web=socket.gethostbyaddr(dname)
        reqaddr=socket.gethostbyname_ex(dname)
    except:
        print("\r\nconnect:Check Your Internet Connection\r\n")
        pass
    try:
        for res in socket.getaddrinfo(reqaddr,reqport):
            family,socktype,proto,canonname,sockaddr = res
            print 'Family...........:',proto_fam[family]
            print 'Type.............:',types[socktype]
            print 'Protocol.........:',protocols[proto]
            print 'Canonical name...:',canonname
            print 'Socket address...:',sockaddr
        print 'Website/Hostname.:',web[0]
        print "Domain Name......:",host
        print "Name Info:.......:",pot
    except:
        print("\r\n\nconnect:Check Your Internet Connection\r\n")
        print("Quiting...Closing...")
        time.sleep(0.9)
    
        
if __name__=="__main__":
    while 1:
        info()
