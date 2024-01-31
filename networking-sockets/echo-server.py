#!/usr/bin/env python

import socket

host = '10.0.0.19'
# host = socket.gethostname() may return 127.0.0.1
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()

    while True:
     con, addr = s.accept()
     data = con.recv(4096)
     print("Received from ", addr, data.decode('utf-8'))
     con.sendall(data)

    ## uncomment following block to die the server after one time connection from client
    #while True:
    #    data = con.recv(4096)
    #    print("Received from ", addr, data.decode('utf-8'))
    #    con.sendall(data)
        #if not data:
        #    # break comment break to ensure server stays up
        #    pass
        #else:
        #    print("Received from ", addr, data.decode('utf-8'))
        #    con.sendall(data)

