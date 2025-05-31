# github.com/oMgItSParadise

import logging
import smtplib
from email.mime.text import MIMEText

class AlertManager:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger("DOS_DDOS_Detector")
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def trigger_alert(self, message):
        self.logger.warning(message)
        if self.config.email_alerts_enabled:
            self.send_email_alert(message)

    def send_email_alert(self, message):
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'DOS/DDoS Detection Alert'
            msg['From'] = self.config.email_sender
            msg['To'] = ', '.join(self.config.email_recipients)
            with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port) as server:
                if self.config.smtp_use_tls:
                    server.starttls()
                if self.config.smtp_username and self.config.smtp_password:
                    server.login(self.config.smtp_username, self.config.smtp_password)
                server.sendmail(self.config.email_sender, self.config.email_recipients, msg.as_string())
        except Exception as e:
            self.logger.error(f"Failed to send email alert: {e}")
