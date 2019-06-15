#!/usr/bin/python3
import socket
import ssl
import pprint
import sys


HOST = b'www.perdu.com'
PORT = 443

# default SSL context with the recommended security settings
# context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_REQUIRED
context.verify_flags = ssl.VERIFY_DEFAULT
context.check_hostname = True
context.load_default_certs()

# context.check_hostname = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssec = context.wrap_socket(s, server_hostname=HOST)
ssec.connect((HOST, PORT))

print("~~~~~~~~~~~~~~~~~~~~ Cipher ~~~~~~~~~~~~~~~~~~~~")

print(ssec.cipher())

print("~~~~~~~~~~~~~~~~~~~~ Server Certificate ~~~~~~~~~~~~~~~~~~~~")
cert = ssec.getpeercert()
pprint.pprint(cert)

print("~~~~~~~~~~~~~~~~~~~~ HTTP Request ~~~~~~~~~~~~~~~~~~~~")

request = b'GET / HTTP/1.1\r\n'
request += b'Host: ' + HOST + b'\r\n'
request += b'Connection: close\r\n'
request += b'\r\n'

ssec.sendall(request)
print(request.decode('utf-8'), end='')

print("~~~~~~~~~~~~~~~~~~~~ HTTP Answer ~~~~~~~~~~~~~~~~~~~~")
while True:
    answer = ssec.recv(1024)
    if answer == b'':
        break
    print(answer.decode('utf-8'), end='')

ssec.close()
