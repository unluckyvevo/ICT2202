import sys
from scapy.all import *
from scapy.all import IP, TCP, ICMP, UDP
   

#rdpcap from scapy and load in pcap file
pkt = rdpcap('smallFlows.pcap')

#displays a list of summary of each packet, with packet number
def packet_summary():
    print (pkt.nsummary())

#displays 1 packet 
def packet_option(value):
    print (pkt[value].summary())

#displays a developed view of a specific packet 
def packet_show(value):
    print (pkt[value].show())

#Choose a source and destination to check for communication
def src_dst(src,dst):
    for packet in pkt:
        #validate source and destination entered is in PCAP
        if(src!=0):
            if IP in packet:
             if(packet[IP].src==src and packet[IP].dst==dst):
                print (packet[IP].src, packet[IP].dst, packet[IP].sport, packet[IP].dport)
        else:
            if IP in packet:
                print (packet[IP].src, packet[IP].dst)

#display RAW data of a packet in hexdump format
def packet_raw(value):
    print (hexdump(pkt[value][Raw].load))

#analyse all the packets that are ICMP 
def analyse_icmp():
    i=0
    for pkts in pkt:

        if pkts.haslayer(ICMP):
            i += 1
            print ("-" * 40)
            print ("[*] Packet : " + str(i))
            print ("[+] ###[ ICMP ] ###")
            #ICMP Type
            ICMPpkt = pkts[ICMP]
            ICMP_type = ICMPpkt.type
            print ("[*] ICMP Type : ", ICMP_type)
            #ICMP Code
            ICMP_code = ICMPpkt.code	
            print ("[*] ICMP Code : ", ICMP_code)
            #ICMP Checksum
            ICMP_chksum = ICMPpkt.chksum
            print ("[*] ICMP Chksum : ", ICMP_chksum)
            #ICMP Id
            ICMP_id = ICMPpkt.id
            print ("[*] ICMP Id : ", ICMP_id)
            #ICMP Sequence Number
            ICMP_seq = ICMPpkt.seq
            print ("[*] ICMP Seq : ", ICMP_seq)	 
            #displays in hexdump format 
            print (("[*] ICMP Dump : "))
            print (hexdump(ICMPpkt))

#get mac source/destination     
# *Eth type 2048 = IPv4*
def analyse_eth():
	i=0
	for pkts in pkt:
		i += 1
        #formatting line && increment packet number
		print ("-" * 40)
		print ("[*] Packet : " + str(i))
		print ("[+] ### [ Ethernet ] ###")
		print ("[*] Mac Destination : " + pkts.dst)
		print ("[*] Mac Source : " + pkts.src)
		print ("[*] Ethernet Type : " + str(pkts.type))


def packet_raw():
    for packet in pkt:
        if packet.getlayer(Raw):
            print ('[+] Found Raw' + '\n')
            l = packet.getlayer(Raw)
            rawr = Raw(l)
            hexdump(rawr)   


#packet_summary()
#packet_option(1500)
#packet_show(11815)
#packet_proto(82)
#src_dst("192.168.3.131","209.17.73.30")
#src_dst(0,0)
#packet_raw()

#analyse_eth()
#analyse_icmp()
#analyse_tcp()
#analyse_udp()
