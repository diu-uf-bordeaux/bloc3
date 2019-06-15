#!/usr/bin/python3
import sys
import socket

HOST = b'www.perdu.com'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("~~~~~~~~~~~~~~~~~~~~ HTTP Request ~~~~~~~~~~~~~~~~~~~~")

request = b'GET / HTTP/1.1\r\n'
request += b'Host: ' + HOST + b'\r\n'
request += b'Connection: close\r\n'
request += b'\r\n'
s.sendall(request)
print(request.decode('utf-8'), end='')

print("~~~~~~~~~~~~~~~~~~~~ HTTP Answer ~~~~~~~~~~~~~~~~~~~~")
while True:
    answer = s.recv(1024)
    if answer == b'': break
    print(answer.decode('utf-8'), end='')

s.close()
