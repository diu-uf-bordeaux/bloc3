#!/usr/bin/python3
import sys
import socket

HOST = b'localhost'
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
addr = s.getpeername()
print('Connected to', addr)
s.sendall(b'hello world!')
msg = s.recv(1024)
print(msg.decode())
print("Press Enter to quit...")
sys.stdin.readline()
s.close()
print('Disconnected from', addr)

