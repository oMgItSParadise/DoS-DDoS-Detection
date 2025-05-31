class Config:
    def __init__(self):
        self.packet_rate_threshold = 100
        self.time_window = 10
        self.email_alerts_enabled = False
        self.email_sender = "alert@example.com"
        self.email_recipients = ["admin@example.com"]
        self.smtp_server = "smtp.example.com"
        self.smtp_port = 587
        self.smtp_use_tls = True
        self.smtp_username = None
        self.smtp_password = None
        self.ip_whitelist = set()
        self.ip_blacklist = set()
        self.connection_type = None
