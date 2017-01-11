#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time
import threading


def tcplink(sock, addr):
    print ('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print ('Connection from %s:%s closed.' % addr)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 9000))

server.listen(5)

print ('Wait for connecting...')

sock, addr = server.accept()

t = threading.Thread(target=tcplink, args=(sock, addr))

t.start()
