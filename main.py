from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def start_detection():
    sniff(prn=packet_callback)

if __name__ == "__main__":
    start_detection()
