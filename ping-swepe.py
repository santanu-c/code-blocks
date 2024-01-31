#!/usr/bin/env python

import sys
import subprocess
from multiprocessing import  Process, Queue
from IPy import IP


def ping2host(i,q):
    ''' Ping one packet to target host'''

    while True:
        if q.empty():
            sys.exit(0)

        ip = q.get()
        pingcmd = "timeout 1 ping -c 1 " + str(ip)

        ret = subprocess.call(pingcmd, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT )
        if ret == 0:
            print("Thread %s pinged %s successfully" %(i,ip))
        else:
            print("Thread %s found no response from %s" %(i,ip))


if __name__ == "__main__":

     num_procs = sys.argv[1]

     ips = IP('10.0.0.0/24')
     q = Queue()

     for ip in ips:
         q.put(ip)


     for i in range(int(num_procs)):
         p = Process(target=ping2host, args=[i,q])
         p.start()


     print("Main process started ...")

     p.join()
     print("Main process finished ...")




