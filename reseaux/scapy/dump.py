#!/usr/bin/env python3

import sys
from scapy.all import *

x = IP(dst='www.google.com')/TCP(dport=80)/"GET / HTTP/1.0\r\n\r\n"  # un exemple de requête HTTP/TCP/IP
x.show()                                                             # afficher le paquet IP et les (encapsulation)
wrpcap('x.pcap',x)                                                   # sauvegarder au format .pcap (tcpdump, wireshark)
hexdump(x)                                                           # afficher au format hexadécimal
x.pdfdump('x.pdf')                                                   # afficher le paquet au format pdf

