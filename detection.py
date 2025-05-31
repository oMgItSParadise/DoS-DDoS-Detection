# github.com/oMgItSParadise
#selam
import time
import numpy as np
from collections import defaultdict, deque

class Detector:
    def __init__(self, config, alert_manager):
        self.config = config
        self.alert_manager = alert_manager
        self.packet_data = defaultdict(lambda: deque(maxlen=1000))
        self.packet_rate_threshold = self.config.packet_rate_threshold
        self.time_window = self.config.time_window

    def process_packet(self, src_ip, packet_size, timestamp, protocol):
        self.packet_data[src_ip].append(timestamp)
        self.check_threshold(src_ip)

    def check_threshold(self, src_ip):
        timestamps = self.packet_data[src_ip]
        current_time = time.time()
        count = sum(1 for t in timestamps if current_time - t <= self.time_window)
        if count > self.packet_rate_threshold:
            self.alert_manager.trigger_alert(f"High packet rate detected from {src_ip}: {count} packets in last {self.time_window} seconds")

    def display_stats(self):
        print("Current packet rates per IP:")
        current_time = time.time()
        for src_ip, timestamps in self.packet_data.items():
            count = sum(1 for t in timestamps if current_time - t <= self.time_window)
            print(f"  {src_ip}: {count} packets in last {self.time_window} seconds")
