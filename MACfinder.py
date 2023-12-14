import webbrowser
from scapy.all import ARP, Ether, srp

# Create an ARP request packet to get the MAC address associated with the IP address
ip_range = '192.168.1.1/24'
arp = ARP(pdst=ip_range)
ether = Ether(dst='ff:ff:ff:ff:ff:ff')  # Broadcast Ethernet frame
packet = ether/arp

# Send and receive packets, timeout is set to 3 seconds
result = srp(packet, timeout=3, verbose=0, iface='Ethernet')[0]

# Return the MAC address from the received packet
for sent, received in result:
    if received.hwsrc == 'fc:ee:91:00:f4:ce':
        print(f'IP Address: {received.psrc} on {received.hwsrc} is alive')
        webbrowser.open(f'http://{received.psrc}')
    else:
        pass

