# github.com/oMgItSParadise

from flask import Flask, jsonify, render_template
from detection import Detector
from config import Config
import threading
import time
import sys
from packet_capture import PacketCapture

app = Flask(__name__)
config = Config()
detector = Detector(config, None)
packet_capture = PacketCapture(detector, config)

def start_packet_capture():
    try:
        packet_capture.start_capture()
    except Exception as e:
        print(f"[WARNING] Packet capture could not be started: {e}")

capture_thread = threading.Thread(target=start_packet_capture)
capture_thread.daemon = True
capture_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats():
    stats = {}
    current_time = time.time()
    for src_ip, timestamps in detector.packet_data.items():
        count = sum(1 for t in timestamps if current_time - t <= detector.time_window)
        stats[src_ip] = count
    return jsonify(stats)

def run_dashboard():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    if sys.platform.startswith("win"):
        print("[INFO] You are running on Windows. Packet capture requires winpcap/npcap. For best results, use Linux (e.g., Kali) with libpcap installed.")
    else:
        print("[INFO] Running on Linux/Unix. Packet capture should work if libpcap is installed.")
    run_dashboard()
