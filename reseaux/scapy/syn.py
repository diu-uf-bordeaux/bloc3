#!/usr/bin/env python3

import sys
from scapy.all import *

x=IP(dst="www.perdu.com")/TCP(flags="S",dport=80)
x.show()
y = sr1(x)
y.show()
