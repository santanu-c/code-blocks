#!/usr/bin/env python

import socket

s = socket.socket()

#host = socket.gethostname()
host = '10.0.0.19'
port = 12345

s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept() ## accept() blocking call
    print('Got connection from ', addr)
    c.send(b'Thanks for connection') ## in network communications, always use byte string
    c.close()
