import sys
from scapy.all import *
from scapy.all import IP, TCP
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

def packet_raw(value):
    print (hexdump(pkt[value][Raw].load))

    '''
    for packet in pkt:
        if packet.getlayer(Raw):
            print ('[+] Found Raw' + '\n')
            l = packet.getlayer(Raw)
            rawr = Raw(l)
            hexdump(rawr)
            '''    

#packet_summary()
#packet_option(11815)
#packet_show(11815)
#packet_proto(82)
#src_dst("192.168.3.131","209.17.73.30")
#src_dst(0,0)
#packet_raw(11815)