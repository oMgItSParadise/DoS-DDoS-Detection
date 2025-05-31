<!-- github.com/oMgItSParadise -->
# DOS/DDoS Detection Tool by Paradise

---

## ENGLISH

### Overview
This Python-based tool detects DOS and DDoS attacks by capturing and analyzing network packets in real-time. It uses threshold and statistical analysis to identify suspicious traffic patterns and can trigger alerts.

### Features
- Real-time packet capture using scapy.
- Threshold-based and statistical anomaly detection.
- Configurable thresholds and IP whitelist/blacklist.
- Alerting via logs and optional email notifications.
- Optional Flask-based web dashboard for visualization.

### Installation
1. Install Python 3.7 or higher.
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. **On Linux (recommended):** Run the tool as root or with sudo to allow packet capture.
4. **On Windows:** Packet capture requires winpcap/npcap. Linux (e.g., Kali) is recommended for best compatibility.

### Usage
1. Run the detection tool:
   ```
   python main.py
   ```
2. (Optional) Run the web dashboard:
   ```
   python dashboard.py
   ```
   Then open http://localhost:5000 in your browser.

### Configuration
Edit `config.py` to adjust thresholds, email alert settings, and IP whitelist/blacklist.

### Testing
Test the tool against simulated attacks using tools like LOIC or Hping3.

### Notes
- Run with appropriate permissions to capture network packets (e.g., administrator/root).
- Ensure dependencies are installed.
- The tool is modular and extensible for future enhancements.

### License
MIT License

---

## TÜRKÇE

### Genel Bakış
Bu Python tabanlı araç, ağ paketlerini gerçek zamanlı olarak yakalayıp analiz ederek DOS ve DDoS saldırılarını tespit eder. Şüpheli trafik desenlerini belirlemek için eşik ve istatistiksel analiz kullanır ve uyarılar oluşturabilir.

### Özellikler
- Scapy ile gerçek zamanlı paket yakalama.
- Eşik tabanlı ve istatistiksel anomali tespiti.
- Ayarlanabilir eşikler ve IP beyaz/siyah listesi.
- Loglar ve isteğe bağlı e-posta ile uyarı.
- Gerçek zamanlı görselleştirme için opsiyonel Flask tabanlı web paneli.

### Kurulum
1. Python 3.7 veya üzerini yükleyin.
2. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```
3. **Linux'ta (önerilir):** Paket yakalama için aracı root olarak veya sudo ile çalıştırın.
4. **Windows'ta:** Paket yakalama için winpcap/npcap gereklidir. En iyi uyumluluk için Linux (örn. Kali) önerilir.

### Kullanım
1. Tespit aracını başlatın:
   ```
   python main.py
   ```
2. (Opsiyonel) Web panelini başlatın:
   ```
   python dashboard.py
   ```
   Ardından tarayıcınızda http://localhost:5000 adresini açın.

### Yapılandırma
Eşik değerlerini, e-posta ayarlarını ve IP beyaz/siyah listesini ayarlamak için `config.py` dosyasını düzenleyin.

### Test
Aracı LOIC veya Hping3 gibi araçlarla simüle saldırılarla test edin.

### Notlar
- Ağ paketlerini yakalamak için uygun yetkilerle (örn. root/administrator) çalıştırın.
- Bağımlılıkların kurulu olduğundan emin olun.
- Araç modülerdir ve gelecekteki geliştirmeler için uygundur.

### Lisans
MIT Lisansı
