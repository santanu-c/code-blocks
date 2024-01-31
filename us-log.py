import sys
import re
import os
import csv
import argparse


LOGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log')
FILENAME = r'us-log\d+.log'
PROGNAME = sys.argv[0]


def example_usage(prog):
    '''This displays help'''
    helpstring = """
    1. prog_name -a
    2. prog_name -a -o <filename>
    """
    
    helpstring.replace("prog_name", prog)
    
    

def get_log_files(pattern, base):
    regexp = re.compile(pattern)
    logfiles = []
    
    for root, dirs, files in os.walk(base):
        for f in files:
            if regexp.search(f):
                logfiles.append(os.path.join(root,f))
                
    return logfiles


def read_file(fname):
    with open(fname) as fh:
        for line in fh:
            yield line
            
            
def main():
    
    parser = argparse.ArgumentParser(description='This extracts data from a log file',
                                     epilog = example_usage(PROGNAME),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('-a', '--analyze', dest='analyze', action='store', help='Analyze the file')
    parser.add_argument('-o', '--outfile', dest='ofile', action='store', help='Provide the out file name')
    
    args = parser.parse_args
    
    if args.ofile:
        report_file = args.ofile        
    else:
        print("Provide the output file name")    
    
    
    if args.analyze:
        
        log_line_exp = re.compile(r'\[(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d)\]\s+([A-Z]+):\s+(.*?)')
        #time_stamp = ""
        #user_name = 
        field_names = ["Timestamp", "Log_level", "Message"]
        with open(report_file, 'w', field_names=field_names) as of:
            csv_writer= csv.DictWriter(of, fieldnames=field_names)
            csv_writer.writeheader()
        
            for file in get_log_files(FILENAME, LOGDIR):
                for line in read_file(file):
                    #d,f = os.path.split(file)
                    #new_f = f + '.csv'
                    #report_file = os.path.join(d,new_f)
                    ## Process the file line by line here
                    result = log_line_exp.search(line)
                    if result:
                        Timestamp = result.group(1)
                        Log_level = result.group(2)
                        Message = result.group(3)
                        csv_writer.writerow({"Timestamp": Timestamp, "Log_level":Log_level, "Message": Message})
    
    else:
        print("-a is a must switch")
        

if __name__ =='__main__':
    sys.exit(main())

        
        
        

        
    
    
    
    
    