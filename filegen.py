import sys
import os
import re

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),'log')
FILE_NAME = r'us-log(.*?).log'
#FILE_NAME = 'us-log1.log'

def get_log_files(pattern, base):
    logfiles = []
    regexp1 = re.compile(pattern)
    
    for root, dirs, files in os.walk(base):
        for f in files:
            if regexp1.match(f):
                logfiles.append(os.path.join(root,f))
                
    return logfiles


def file_generator(filename):#
    with open(filename) as fh:
        for line in fh:
            yield line



def main():
    for f in get_log_files(FILE_NAME, LOG_DIR):
        for line in file_generator(f):
            print("filename:%s" %f,line.strip('\n'))
            # Prrocess your file here
            


if __name__ == "__main__":
    sys.exit(main())



    
    
    

