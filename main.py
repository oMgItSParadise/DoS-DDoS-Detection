# github.com/oMgItSParadise

from packet_capture import PacketCapture
from detection import Detector
from alert import AlertManager
from config import Config
import threading
import time
import sys
import os

def show_ascii_banner():
    print(r"""
__________                          .___.__               
\______   \_____ ____________     __| _/|__| ______ ____  
 |     ___/\__  \\_  __ \__  \   / __ | |  |/  ___// __ \ 
 |    |     / __ \|  | \// __ \_/ /_/ | |  |\___ \\  ___/ 
 |____|    (____  /__|  (____  /\____ | |__/____  >\___  >
                \/           \/      \/         \/     \/ 
    """)

def check_environment():
    if sys.platform.startswith("linux") and os.geteuid() != 0:
        print("[WARNING] Not running as root. Packet capture may not work. Please run with sudo.")
    elif sys.platform.startswith("win"):
        print("[INFO] You are running on Windows. Packet capture requires winpcap/npcap. For best results, use Linux (e.g., Kali) with libpcap installed.")

def select_connection_type():
    print("Select your internet connection type:")
    print("1 - LAN (Ethernet)")
    print("2 - WiFi (Wireless)")
    while True:
        choice = input("Enter your choice (1/2): ").strip()
        if choice == "1":
            return "lan"
        elif choice == "2":
            return "wifi"
        else:
            print("Invalid choice. Please select 1 or 2.")

def main():
    show_ascii_banner()
    check_environment()
    config = Config()
    config.connection_type = select_connection_type()
    alert_manager = AlertManager(config)
    detector = Detector(config, alert_manager)
    packet_capture = PacketCapture(detector, config)
    capture_thread = threading.Thread(target=packet_capture.start_capture)
    capture_thread.daemon = True
    capture_thread.start()
    print("DOS/DDoS Detection tool started. Press Ctrl+C to stop.")
    try:
        while True:
            detector.display_stats()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping DOS/DDoS Detection tool...")

if __name__ == "__main__":
    main()
