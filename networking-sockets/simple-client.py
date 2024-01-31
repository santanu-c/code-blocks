#!/usr/bin/env python

import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

print('Host name is  ', host)
s.connect((host,port))

print(s.recv(1024))

s.close()

