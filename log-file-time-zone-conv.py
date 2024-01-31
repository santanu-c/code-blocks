#!/usr/bin/env python

import sys
import os
import re
import csv
import argparse
from datetime import datetime, timedelta
from pytz import timezone


LOGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logSamples')
PATTERN = 'log_sample_(.*?).log'  # to match log_sample_1.log, log_sample_2.log ..


def getLogFiles(pattern,base):
    regexp = re.compile(pattern)
    logfiles = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if regexp.match(f):
                print(f)
                logfiles.append(os.path.join(root,f))

    return logfiles
            


def convertTZ(date1, z1, z2):
    '''Cconverts time from zone to zone, z1 is always 'EST'
    '''
    
    if z1 == "EST" and (z2 == "EST" or z2 == "EST5EDT"):
        date2 = date1
    else:
        dateobj = datetime.strptime(date1, "%m/%d/%Y %H:%M:%S:%f")
        eastern_tz = timezone('US/Eastern')
        # convert z2 to EST
        if z1 == "EST" and z2 == "Singapore":
            other_tz = timezone('Asia/Singapore')
        if z1 == "EST" and z2 == "GB":
            other_tz = timezone('Europe/London')
            
        other_tz_local = other_tz.localize(dateobj)
        t_eastern_local = other_tz_local.astimezone(eastern_tz)
        #date2 = t_eastern_local("%m/%d/%Y %H:%M") ## convert timezone to EST, trip seconds part
        date2 = t_eastern_local.strftime("%m/%d/%Y %H:%M:%S:%f")
        
    return date2 
        
    
    
def findTimeDiff(d1,d2):
    '''Calculates Time diff, d2 > d1, both in same timezone
    '''
    d1_obj = datetime.strptime(d1, "%m/%d/%Y %H:%M:%S:%f")
    d2_obj = datetime.strptime(d2, "%m/%d/%Y %H:%M:%S:%f")
    d_diff = (d2_obj - d1_obj)
    
    return (round(d_diff.total_seconds()/(60*60),1))           
    
#def writeReport(fname, fields, data, format='csv'):
#    '''Dumps report to output file of give format'''
#    if format == 'csv':
#        with open(fname, 'w') as fh:
#            wrt = csv.writer(fh)
#            wrt.writerow(fields)
#            wrt.writerows(data)
            
    
def main():

    # 02/13/2014 22:39:51:463914 -I- Messages of severity "-M-" and above will now be logged.
    regexp1 = re.compile(r"(?P<dttm>(\s+)?(\d\d/\d\d/\d\d\d\d)(\s+)(\d\d:\d\d:\d\d:\d\d\d\d\d\d)(\s+)?)"
                        )
    # 02/14/2014 11:39:52:838663 -E- SQL-Message Handler[5701]: <Changed database context to 'clientmlp'.>
    regexp2 = re.compile(r"(?P<errcd>(\s+)?(-E-)(\s+)?)"
                        )

    # 02/13/2014 22:39:52:429697 -I- SQLRPC (607bb50) = getUserDbIdRSA_sp @u_name="janedoe", @u_id(OUTPUT)
    regexp3 = re.compile(r"(?P<uname>@u_name=\"(.*?)\")"
                        )

    # 02/13/2014 22:39:51:464155 -I- Running Trading System version 7.1.3.24.ft.rh6.m64.lnx . Log file setup complete.
    regexp4 = re.compile(r"(?P<junk1>.*(\s)+(Running Trading System version)(\s)+)"
                         r"(?P<clver>(.*.lnx)\s+)"
                        )
                        # r"(?P<junk2>.*)"  # do not ccare what is after lnx
                        
    # 02/13/2014 22:39:52:707067 -I- Setting Timezone to Singapore
    regexp5 = re.compile(r"(?P<junk>.*\s+Setting Timezone to\s+)"
                         r"(?P<tzone>.*)"
                        )
                        
    # 02/14/2014 11:40:32:835262 -I- Gathering Portfolio View <~PM_TEST>
    regexp6 = re.compile(r"(?P<junk>.*(Gathering Portfolio View)\s+)"
                         r"(?P<pfolio>.*)"
                        )
    
    x = 1
    y = 1
    z = 1
    m = 1 
    p_folio = []
    for f in getLogFiles(PATTERN,LOGDIR):
        errcount = 0
        ## check the access time/modification of a file
        mtime = os.stat(f).st_mtime
        pfile = datetime.fromtimestamp(mtime).strftime('%Y%m%d_%H%M%S')
        logfile = "log_summary."+ pfile + ".csv" 
        mtime_dict = {f:logfile}
        
        with open(f) as fh:
            for line in fh:
                
                # get session start date and end time
                res1 = regexp1.search(line)
                if res1:
                    if x == 1:    
                        start_dt = res1.group('dttm').strip()
                        x = 2
                    
                        # capture time, time from last line
                    end_dt = res1.group('dttm').strip()
                
                # get error count -E- for each line
                res2 = regexp2.search(line)
                if res2:
                    errcount += 1
                
                # get username 
                if y == 1:
                    res3 = regexp3.search(line)
                    if res3:
                        uname_temp = res3.group('uname')
                        uname_regexp= re.compile(r'(?P<uname1>\"(.*?)\")')
                        uname_res = uname_regexp.search(uname_temp)
                        if uname_res:
                            uname = uname_res.group('uname1')
                        #print(uname )
                        y = 2
                        
                # get client ver
                if z == 1:
                    res4 = regexp4.search(line)
                    if res4:
                        client_ver = res4.group('clver')
                        #print(client_ver)
                        z = 2
        
                # get timezone info (one time code)
                if m == 1:
                    res5 = regexp5.search(line)
                    if res5:
                        tz = res5.group('tzone').strip()
                        m = 2
                    else: 
                        tz = 'EST'
                   
                # get portfolios
                res6 = regexp6.search(line)
                if res6:
                    p_folio.append(res6.group('pfolio'))
                
        

            ## compile the data for each logfile
            pfolio = "|".join(p_folio)
            (logfolder,logfilename) = os.path.split(f)
            log_file_name = logfilename
            error_count = errcount
            
            time_zone = tz
            
            start_time_obj = datetime.strptime(start_dt, "%m/%d/%Y %H:%M:%S:%f")
            start_time_full = datetime.strftime(start_time_obj, "%m/%d/%Y %H:%M:%S:%f")
            start_time_est = datetime.strftime(start_time_obj, "%m/%d/%Y %H:%M")
            
            # convert end time to local EST time
            converted_end_time = convertTZ(end_dt,'EST',time_zone)
            #print("Hello",converted_end_time)
            
            converted_end_time_obj = datetime.strptime(converted_end_time, "%m/%d/%Y %H:%M:%S:%f")
            #converted_end_time_full = datetime.strptime(converted_end_time_obj, "%m/%d/%Y %H:%M:%S:%f")
            end_time_est = datetime.strftime(converted_end_time_obj, "%m/%d/%Y %H:%M")
            #end_time_local = datetime.strftime(end_time_obj, "%m/%d/%Y %H:%M") 
            
            #print("tada", end_time_est)
            
            session_length = findTimeDiff(start_time_full,converted_end_time)
            #print("TADADAAAA", session_length)
            username = uname
            client_version = "cmlib/" + client_ver
            portfolios_loaded = pfolio
            
            l1 = [log_file_name, error_count, time_zone, start_time_est, end_time_est, session_length, username, client_version, portfolios_loaded]
            l2 = [ str(item) for item in l1]
            #print (l2)
            #print(":".join(l2))
            
            #fname_set = set()
            #for k in mtime_dict:
            #    fname_set.add(mtime_dict[k])
            
            fname = os.path.join(logfolder,mtime_dict[f])
            fields = ['log_file_name', 'error_count', 'time_zone', 'start_time_est', 'end_time_est', 'session_length', 'username', 'client_version', 'portfolios_loaded']
            data = [l2]
            #writeReport(fname, fields, l2, 'csv')
            
            
            ## write report
            with open(fname, 'a') as fh:
                wrt = csv.writer(fh)
                wrt.writerow(fields)
                wrt.writerows(data)
    
    

if __name__ == '__main__':
    sys.exit(main())