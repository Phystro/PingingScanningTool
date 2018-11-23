"""
This module is part of PhystroTech
Copyright 2017 Anthony Karoki
This module simply arranges contents of a list in oderly vertically descending
manner. You can either call the list directly or through a path directory to
a file containing a list or whose contents can be compiled and arranged into a list.
"""
import os,time
import threading

def dirlist(path):
    files=os.listdir(path)
    items=len(files)
    print("%s items found:"%(items))
    def ch():
        for n,i in enumerate(files):
            print("\t",n+1,files[n])
    t=threading.Thread(target=ch,)
    t.start()
    #print("\r\nTime Taken",e-s,"secs")
def listarr(nlist):
    nlen=len(nlist)
    print("%s items in list:"%(nlen))
    for n, i in enumerate(nlist):
        print("\t",n+1,".",nlist[n])
        

if __name__=="__main__":
    dirlist(os.getcwd())
    
