from scapy.all import sniff

def show_packet(packet):
    print(packet.summary())

print("Sniffer start ho gaya...")
sniff(prn=show_packet, count=5)
