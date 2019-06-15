#!/usr/bin/python3
import sys
import socket

HOST = b'localhost'
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = sys.stdin.readline()
    s.sendall(msg.encode())
    data = s.recv(1024)
    if data == b'' or data == b'\n' : break
    print(data.decode('utf-8'),end='')
s.close()

