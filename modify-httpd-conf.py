#!/usr/bin/python3

import re
import sys


def new_config(fname,hn,dr):
    ''' returns mathcin or non matching lines'''
    
    vhost_start = re.compile(r'\s*<VirtualHost\s+(.*)>')
    doc_root = re.compile(r'(\s*DocumentRoot\s+)(.*)')
    vhost_end = re.compile(r'\s*</VirtualHost>')   
    current_host = ""
    
    with open(fname) as fh:
        for line in fh:
            result1 = vhost_start.search(line)
            if result1:
                vhost_section_begin = True
                current_host = result1.group(1)
                
            if current_host == hn and (vhost_section_begin == True):
                #print(current_host)
                result2 = doc_root.search(line)
                if result2:
                    print("HHHH",result2.group(1), result2.group(2),"\n")
                    old_doc_root = result2.group(1)
                    new_line = doc_root.sub(r"\1%s" %dr, line)
                    line = new_line
                
            result3 = vhost_end.search(line)
            if result3:
                vhost_section_begin = False
                current_host = ""
        
            yield line



if __name__ == '__main__':
    conf_file = sys.argv[1]
    host_name = sys.argv[2]
    doc_root = sys.argv[3]
    
    # call func
    #      ==> finc yields line
    # print line
    
    for line in new_config(conf_file,host_name, doc_root):
        print(line.strip('\n'))
    
    