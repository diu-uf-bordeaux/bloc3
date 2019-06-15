#!/usr/bin/env python3

import sys
import socket
from scapy.all import *


def mytraceroute(target, maxttl):
    for k in range(1, maxttl):
        x = IP(dst=target, ttl=k)/ICMP()
        y = sr1(x, verbose=0)
        if y.getlayer(ICMP).type == 11 and y.getlayer(ICMP).code == 0:    # time to leave exceeded (11)
            print(k, y.src)
        elif y.getlayer(ICMP).type == 0 and y.getlayer(ICMP).code == 0:   # echo-reply (0)
            print(k, y.src)
            break
        else:
            print(k, "* * *")


target = socket.gethostbyname("www.google.com")
mytraceroute(target, 64)
