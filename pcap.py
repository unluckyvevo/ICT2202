import sys
from scapy.all import *
from scapy.all import IP, TCP, DNS, DNSQR
from scapy.utils import *

#rdpcap from scapy and load in pcap file
pkt = rdpcap('smallFlows.pcap')


def packet_summary():
    print (pkt.nsummary())

def packet_option(value):
    print (pkt[value].summary())

def packet_show(value):
    print (pkt[value].show())

def packet_proto(value): 
    print (pkt[value][IP].proto)

def src_dst(src,dst):
    connections = set()
    for packet in pkt:
        if(src!=0):
            if IP in packet:
             if(packet[IP].src==src and packet[IP].dst==dst):
                print (packet[IP].src, packet[IP].dst, packet[IP].sport, packet[IP].dport)
        else:
            if IP in packet:
                print (packet[IP].src, packet[IP].dst)

def packet_raw():
    for packet in pkt:
        if packet.getlayer(Raw):
            print ('[+] Found Raw' + '\n')
            l = packet.getlayer(Raw)
            rawr = Raw(l)
            hexdump(rawr)


for packet in pkt:
    if DNSQR in packet:
        if packet[DNS].id == 0x1eef:
            data = packet[DNS][6423].rdata
            print (data)

#packet_summary()
#packet_option(82)
#packet_show(6423)
#packet_proto(82)
#src_dst("10.0.2.3","10.0.2.15")
#src_dst(0,0)
#packet_raw()