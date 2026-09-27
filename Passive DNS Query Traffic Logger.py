import logging
from scapy.all import sniff
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class PassiveDnsMonitor:
    def __init__(self, interface=None):
        self.interface = interface
    
    def process_dns_frame(self, packet):
        if packet.haslayer(IP) and packet.haslayer(DNS):
            dns_layer = packet[DNS]
            
            if dns_layer.qr == 0 and packet.haslayer(DNSQR):
                source_ip = packet[IP].src
                query_name = packet[DNSQR].qname.decode('utf-8', errors='ignore')
                
                print(f"[DNS REQUEST] Client: {source-ip:<15} queried -> {query_name}")
        
    def start_capture(self, count=0):
        """Spawns the socket sniffing engine targeting UDP port 53 exclusively."""
        print(f" Monitoring local DNS transactions (UDP Port 53)...")
        print("-" * 65)
    
        sniff(iface=self.interface, filter="udp port 53", prn=self.process_dns_frame, store=0, count=count)


if __name__ == "__main__":
    monitor = PassiveDnsMonitor()
    
    monitor.start_capture(count=10)











































