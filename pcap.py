import sys
from scapy.all import *
from scapy.all import IP, TCP
from scapy.utils import *
from pathlib import Path
#rdpcap from scapy and load in pcap file

pkt=None
class Pkts:
    

    
    def packet_summary(pkt):
        return pkt.nsummary()

    def packet_option(pkt,value):
        return pkt[int(value)].summary()

    def packet_show(pkt,value):
        return pkt[int(value)].show()

# =============================================================================
#     def packet_proto(pkt,value): 
#         return (pkt[value][IP].proto)
# =============================================================================

    def src_dst(pkt,src,dst):
    #connections = set()
     src_dst_arr=[]
    
     if(src!=0 and dst!=0):
         
         for packet in pkt:
            if IP in packet:
             if(packet[IP].src==src and packet[IP].dst==dst):
                fullLine=fullLine="Source IP: "+str(packet[IP].src)+" Source Port: "+str(packet[IP].sport)+" Destination IP:"+str(packet[IP].dst)+" Destination Port "+str(packet[IP].dport)
                
                src_dst_arr.append(fullLine)
         return src_dst_arr    
     elif(src!=0):
        
         for packet in pkt:
            if IP in packet:
                if(packet[IP].src==src):
                    print("ok!")
                    fullLine=fullLine="Source IP: "+str(packet[IP].src)+" Source Port: "+str(packet[IP].sport)+" Destination IP:"+str(packet[IP].dst)+" Destination Port "+str(packet[IP].dport)
                    src_dst_arr.append(fullLine)
         return src_dst_arr    
                    
     elif(dst!=0):
        
         for packet in pkt:
             if IP in packet:
                if(packet[IP].dst==dst):
                     fullLine=fullLine="Source IP: "+str(packet[IP].src)+" Source Port: "+str(packet[IP].sport)+" Destination IP:"+str(packet[IP].dst)+" Destination Port "+str(packet[IP].dport)
                     src_dst_arr.append(fullLine)
         return src_dst_arr                
                     
     else:
         print("Invalid input")
            
                
                

    def packet_raw(pkt,value):
       return (hexdump(pkt[int(value)][Raw].load))

    '''
    for packet in pkt:
        if packet.getlayer(Raw):
            print ('[+] Found Raw' + '\n')
            l = packet.getlayer(Raw)
            rawr = Raw(l)
            hexdump(rawr)
            
                '''    
    def getPCAPInfo(filename,chkSummary,pOption,pOption2,pOptionNum,pSD_checked,pktSrc,pktDst):
        megaArr=[]
        filename=Path(filename).name
        pkt= rdpcap(filename)
        orig_stdout = sys.stdout
        if(chkSummary==1):
            
            
            sys.stdout = open('pcap_summary.txt', 'w')
            pkt.nsummary()
            sys.stdout.close()
            sys.stdout=orig_stdout
            f = open("pcap_summary.txt", "r")
            megaArr.append(f.read())
            megaArr.append("====================================================================")
            f.close()
        if(pOption==1):
            if(pOption2==0):
                 fileToOpen="pcap_show_"+str(pOptionNum)+".txt"
                 sys.stdout = open(fileToOpen,'w')
                 #Pkts.packet_show(pkt,pOptionNum)
                 pkt[int(pOptionNum)].show()
                 sys.stdout.close()
                 sys.stdout=orig_stdout
                 fp=open(fileToOpen,'r')
                 megaArr.append(fp.read())
                 megaArr.append("====================================================================")
                 fp.close()
                
            if(pOption2==1):
                 fileToOpen="pcap_option_"+str(pOptionNum)+".txt"
                 #megaArr.append(Pkts.packet_option(pkt,pOptionNum))
                 sys.stdout = open(fileToOpen,'w')
                 #Pkts.packet_show(pkt,pOptionNum)
                 pkt[int(pOptionNum)].summary()
                 sys.stdout.close()
                 sys.stdout=orig_stdout
                 fz=open(fileToOpen,'r')
                 megaArr.append(fz.read())
                 megaArr.append("====================================================================")
                 fz.close()
            
                 
                 
            else:
                  #megaArr.append(Pkts.packet_option(pkt,pOptionNum))
                 sys.stdout = open('pcap_raw.txt','w')
                 #Pkts.packet_show(pkt,pOptionNum)
                 hexdump(pkt[int(pOptionNum)][Raw].load)
                 sys.stdout.close()
                 sys.stdout=orig_stdout
                 fo=open('pcap_raw.txt','r')
                 megaArr.append(fo.read())
                 megaArr.append("====================================================================")
                 fo.close()
                
                
                 
                
                #megaArr.append(Pkts.packet_raw(pkt,pOptionNum))
        if(pSD_checked==1):
                 pksd=Pkts.src_dst(pkt,pktSrc,pktDst)  
                 for i in range(len(pksd)):                
                     megaArr.append((pksd[i]))
                 megaArr.append("====================================================================")    
        return megaArr       
                 
#packet_summary()
#pkter= rdpcap(r'smallFlows.pcap')
Pkts.packet_option(pkter,8132)
#packet_show(11815)
#packet_proto(82)
#src_dst("192.168.3.131","209.17.73.30")
#src_dst(0,0)
#packet_raw(11815)
