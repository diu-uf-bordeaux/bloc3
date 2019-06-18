#!/usr/bin/python3
import sys
import socket

HOST = b'www.google.com'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'GET / HTTP/1.0\r\n\r\n')
data = s.recv(1024) # just the 1K first chars...
print(data)
s.close()

