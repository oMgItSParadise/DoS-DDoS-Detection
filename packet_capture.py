# github.com/oMgItSParadise
from scapy.all import sniff, get_if_list
from scapy.layers.inet import IP
import time
import sys
import os

class PacketCapture:
    def __init__(self, detector, config):
        if sys.platform.startswith("linux") and os.geteuid() != 0:
            print("[WARNING] You are not running as root. Packet capture may not work. Please run with sudo.")
        self.detector = detector
        self.config = config
        self.iface = self.select_interface_by_connection_type()

    def select_interface_by_connection_type(self):
        interfaces = get_if_list()
        if not interfaces:
            print("No network interfaces found! Please check your network adapter and permissions.")
            sys.exit(1)
        conn_type = getattr(self.config, "connection_type", None)
        if conn_type == "lan":
            for iface in interfaces:
                if "eth" in iface or "en" in iface:
                    print(f"Auto-selected LAN interface: {iface}")
                    return iface
        elif conn_type == "wifi":
            for iface in interfaces:
                if "wl" in iface or "wi" in iface or "wlan" in iface:
                    print(f"Auto-selected WiFi interface: {iface}")
                    return iface
        print("Available network interfaces:")
        for idx, iface in enumerate(interfaces):
            print(f"{idx + 1}: {iface}")
        while True:
            try:
                choice = int(input("Select interface for packet capture (number): "))
                if 1 <= choice <= len(interfaces):
                    return interfaces[choice - 1]
            except Exception:
                pass
            print("Invalid selection. Please enter a valid number.")

    def process_packet(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            protocol = packet[IP].proto
            packet_size = len(packet)
            timestamp = time.time()
            self.detector.process_packet(src_ip, packet_size, timestamp, protocol)

    def start_capture(self):
        sniff(iface=self.iface, prn=self.process_packet, store=False)
