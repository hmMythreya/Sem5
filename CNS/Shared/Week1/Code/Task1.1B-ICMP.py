#! / usr/bin/python3
from scapy.all import *
print ("SNIFFING PACKETS...");
def print_pkt(pkt):
    pkt.show()
pkt = sniff (iface = "br-****",filter='icmp', prn=print_pkt)

