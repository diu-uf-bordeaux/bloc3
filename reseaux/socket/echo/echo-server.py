#!/usr/bin/python3
import socket

HOST = b''
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(0)

while True:
    sclient, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = sclient.recv(1024)
        if data == b'' or data == b'\n' : break
        print(data.decode('utf-8'),end='')
        sclient.sendall(data)
    print('Disconnected by', addr)
    sclient.close()

