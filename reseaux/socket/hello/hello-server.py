#!/usr/bin/python3
import sys
import socket

HOST = b''
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(0)
print("Welcome...")

while True:
    sclient, addr = s.accept()
    print('Connected by', addr)
    msg = sclient.recv(1024)
    print(msg.decode())
    sclient.sendall(b'goodbye!')
    # print("Press Enter to close client connection...")
    # sys.stdin.readline()
    sclient.close()
    print('Disconnected by', addr)

s.close()