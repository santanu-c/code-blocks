#!/usr/bin/python3
 
import time
import sys
import os

filename = sys.argv[1]

if not os.path.isfile(filename): 
    print("invalid file name or file doesnot exist")

with open(filename) as fh:
    filesize = os.stat(filename)[6]
    fh.seek(filesize)   # move to end of file
    
    while True:
        where = fh.tell()
        line = fh.readline()
        if not line:
            time.sleep(1)
            fh.seek(where)
        else:
            print(line)

    