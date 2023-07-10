# plain ip_udp
import  random 
import time
def ip_udp_only():
    eth=Ether(dst= "ff:ff:ff:ff:ff:ff", src ="ac:1f:6b:a5:0a:e6") # 46:d5:f3:fc:fc:92 #fe:7e:d7:6f:55:21 # 32:68:f7:09:a6:de # 6e:76:03:e3:13:c5 #16:BD:4E:4E:94:C2 #
    vlan=Dot1Q(vlan=2001)
    ip=IP()
    udp=UDP(dport=2152)
    #iface="ens2f0"
    payload="X"*100
    pload= Raw(load = "DATA!!")
    i=0
    while True:#i<60:
        #gtp=GTP_U_Header(gtp_type=255,teid=random.randint(1000,9000))
        #pkt = eth/vlan/ip/pload
        pkt = eth/ip/pload
        sendp(pkt,iface="enp216s0f0",count=100)
        #time.sleep(1)
        i+=1

ip_udp_only()