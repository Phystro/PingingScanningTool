from time import time,sleep
import socket,sys

def main():
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

    for port in range(r11,r21):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(c)
        res= s.connect_ex((rmip,port))
        if res==0:
            print("Port open")
            s.close()
        else:
            print("Port Closed")

if __name__=="__main__":
    main()
