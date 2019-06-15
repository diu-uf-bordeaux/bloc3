#!/usr/bin/env python3

import sys
from scapy.all import *

host="www.perdu.com"
ports = range(100)
packets = IP(dst=host)/TCP(dport=ports, flags="S")
ans, unans = sr(packets, timeout=10)   # stop after 10 seconds...
ans.summary()