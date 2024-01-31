#!/usr/bin/env python

import sys
import re
import subprocess
import ipaddress as ia
import multiprocessing as mp
import argparse



# read hostlist, put in the Q
# iterate ssh -l root host1 ip a
# extract ipv4 addr, get subnet, build dict (subnet, min IP)
# print dict


progname = sys.argv[0]

def exampleUsage(prog):
    ''' Displays help'''
    helpstring = """
    Example:
    ===========
    1. Display help
       prog_name -help
    2. Run the program
       prog_name -f <host list file>
    """
    return helpstring.replace("prog_namne", prog)


def readHostList(fname):
    #regexp = re.compile(r'^\s?(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')  # skips #10.211.55.20
    regexp = re.compile(r'^\s?\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')  # skips #10.211.55.20
    hosts = []
    with open(fname) as fh:
        for line in fh:
            if regexp.search(line):
                hosts.append(line.strip('\n'))
    
    print(hosts)
    return hosts
                

        

def getSubnet(hn,subnet_dict):
    
    regexp1 = re.compile(r'(?P<junk>\s+inet\s+)'
                    r'(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
                    r'(?P<net>/\d{1,2})'
                    )
    
    pingcmd = 'ping -c 1 ' + hn
    ping_res = subprocess.call(pingcmd, shell=True, stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)
    
    if ping_res == 0:
        icmd = 'ssh -o StrictHostKeyChecking=no -l root ' + hn + ' ip a'
        ipipe = subprocess.Popen(icmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ipipe_res = ipipe.communicate()
        ipipe_data = ipipe_res[0].decode('utf-8').split('\n')  ## this is how you handle byte stream
                       
        for line in ipipe_data:
            #print(line)
            res = regexp1.search(line)
            if res:
                #print("Found ", hn)
                ip = res.group('ip')
                net  = res.group('net')
                #print(ip,net)
                
                if '127.0.0.1' in ip: 
                    continue
                
                iface = ia.ip_interface(ip + net)
                subnet_addr = str(iface.network)
                
                if subnet_dict.get(subnet_addr):
                    if subnet_dict.get(subnet_addr) > ip:
                        subnet_dict[subnet_addr] = ip 
                else:
                    #print(subnet_addr, ip)
                    subnet_dict[subnet_addr] = ip 
        #print(subnet_dict)
      
    else:
        print(hn, " Not available")  

def main():
    
    parser = argparse.ArgumentParser(description="Scans the network for subnet and min IP",
                                     epilog=exampleUsage(progname),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('-f', '--fname', dest='fname', action='store', help="Provides Host list file")
    parser.add_argument('-o', '--outfile', dest='outfile', action='store', help='Provide output file name')
    parser.add_argument('-t', '--threads', dest='threads', action='store', default=2, help="Provide no of parallel thread to start")
    
    args = parser.parse_args()
    
    if args.fname:
    
        pool = mp.Pool(processes=int(args.threads))
        manager = mp.Manager()
        subnet_dict = manager.dict()
        
        [pool.apply_async(getSubnet, args=[h, subnet_dict]) for h in readHostList(args.fname)]
        
        pool.close()
        pool.join()

    else:
        print("Must provide input file name")
        sys.exit()

    #print(subnet_dict)
    
    if args.outfile:
        for k in subnet_dict:
            print(k," - ", subnet_dict.get(k))    



if __name__ == "__main__":
    sys.exit(main())
    
    
