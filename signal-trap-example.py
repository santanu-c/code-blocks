import signal
#import sys
import time
#import os

def signal_handler(signum, frame):
    print("signal handler called with signal",signum)
    if signum == 2:
        print("Stop pressing CRTL+C")
    else:
        print("It is not 2")

signal.signal(signal.SIGINT, signal_handler)
#signal.signal(signal.SIGALRM, signal_handler)
#signal.alarm(5)

def main():
    while True:
        print(".")
        time.sleep(1)


if __name__=="__main__":
    main()
    #signal.alarm(0)
