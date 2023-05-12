from scapy.all import ARP, Ether, srp

#The ip address to target
target_ip = "192.168.142.128/24"

#The code to create an ARP packet
arp = ARP(pdst=target_ip)

#create an Ether broadcast packet, ff:ff:ff:ff:ff:ff is for broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

#stack ARP and Ether
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

#a list of clients, we will find them in the upcoming loop
clients = [ ]

for sent, received in result:
    #for each response, append the ip and mac addresses to the clients list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    
#printing the clients 
print("Available devices in the network: ")
print("IP" + " "*18+"MAC")

for client in clients:
    print("{:16}  {}".format(client['ip'], client['mac']))