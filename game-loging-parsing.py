#!/usr/bin/python3 

import sys
import re
import csv
from datetime import datetime


def read_log_file(fname):
    re_obj_user_start = re.compile(r'\s*\[(.*)\]\s+Player submitted name:\s+(.*)')
    re_obj_user_end = re.compile(r'\s*\[(.*)\]\s+Player exit name:\s+(.*)')
    
    start_dict = {}
    end_dict = {}
    with open(fname) as fh:
        for line in fh:
            result1 = re_obj_user_start.search(line)
            result2 = re_obj_user_end.search(line)
            if result1: 
                player_start = result1.group(2)
                start_time = result1.group(1)
                start_date_obj = datetime.strptime(start_time, "%m/%d/%Y %I:%M:%S %p")
                start_time = datetime.strftime(start_date_obj, "%Y-%m-%dT%H:%M:%S.%f%z")    # remove %f
                if not(start_dict.get(player_start)):
                    start_dict[player_start] = start_time  
            if result2:
                player_exit = result2.group(2)
                end_time = result2.group(1)
                end_date_obj = datetime.strptime(end_time, "%m/%d/%Y %I:%M:%S %p")
                end_time = datetime.strftime(end_date_obj, "%Y-%m-%dT%H:%M:%S.%f%z")    # remove %f
                end_dict[player_exit] = end_time
                if start_dict.get(player_exit):
                    csv_row = {"User": player_exit, "Start Time": start_dict.get(player_exit), "End Time": end_dict.get(player_exit)}
                    yield csv_row


if __name__ == '__main__':
    log_file = sys.argv[1]
    report_file = sys.argv[2]
    
    if not report_file.endswith(".csv"):
        print("output file name must end with .csv")
    else:
        fields = ['User', 'Start Time', 'End Time']
        
    with open(report_file, 'w') as of:
        writer = csv.DictWriter(of, fieldnames=fields)
        writer.writeheader()
        
        for line in read_log_file(log_file):
            writer.writerow(line)
            
        