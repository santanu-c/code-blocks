import sys
import time
import logging
import datetime


progname = sys.argv[0]


logging.basicConfig(filename='somelog.log',
                    filemode='a',
                    format='[%(asctime)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

x=1
while True:
    sys.stdout.flush()
    logging.info("Logging started")
    logging.info("Sleeping for 1 sec")
    time.sleep(1)
    x += 1
    if x == 10:
        break
