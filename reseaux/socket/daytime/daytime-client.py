#!/usr/bin/python3
import socket

HOST = b'time-c.nist.gov'
PORT = 13

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
print(data.decode("utf-8"))
s.close()
