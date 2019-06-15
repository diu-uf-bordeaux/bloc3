#!/usr/bin/env python3

import sys
from scapy.all import *

ping = IP(dst='www.google.com')/ICMP(type='echo-request')
ping.show()
pong = sr1(ping)
pong.show()
