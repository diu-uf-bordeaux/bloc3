#!/usr/bin/env python3

import sys
from scapy.all import *


def synscan(host):
    ports = range(100)
    packets = IP(dst=host)/TCP(dport=ports, flags="S")
    ans, unans = sr(packets, timeout=10)
    for x, y in ans:
        if y.haslayer(TCP):
            if y.sprintf("%TCP.flags%") == 'SA':
                print(x.dport)

synscan("www.perdu.com")
