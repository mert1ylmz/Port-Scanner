# 🚀 Hızlı Port Tarayıcı (Port Scanner)

Bu proje, Python'ın `socket` modülünü ve `ThreadPoolExecutor` (Multi-threading) yapısını kullanarak belirli bir hedef IP adresi üzerindeki ağ portlarını hızlı bir şekilde tarayan hafif ve etkili bir araçtır.

Aynı anda birden fazla portu (100 iş parçacığı/worker) tarayarak işlemleri geleneksel sıralı tarayıcılara göre çok daha kısa sürede tamamlar.

---

## 🔍 Özellikler

*   **Çoklu İş Parçacığı (Multi-threading):** `concurrent.futures.ThreadPoolExecutor` ile 100 eşzamanlı istek kapasitesi.
*   **Hızlı Yanıt:** `connect_ex` metodu ile soket seviyesinde hızlı ve performanslı kontrol.
*   **Ayarlanabilir Parametreler:** Hedef IP, port aralığı ve zaman aşımı (timeout) süreleri kolayca değiştirilebilir.

---

## 🛠️ Kurulum ve Çalıştırma

Projenin herhangi bir harici kütüphane bağımlılığı yoktur, standart Python 3 kütüphanelerini kullanır.

1. **Depoyu bilgisayarınıza indirin veya klonlayın:**
   ```bash
   git clone https://github.com
   cd Port-Scanner
   ```

2. **Programı çalıştırın:**
   ```bash
   python3 port_scanner.py
   ```

---

## ⚙️ Yapılandırma (Konfigürasyon)

Kod içerisindeki aşağıdaki değişkenleri kendi ihtiyacınıza göre düzenleyebilirsiniz:

*   `TARGET`: Taramak istediğiniz hedef IP adresi veya alan adı (Varsayılan: `127.0.0.1` - Localhost).
*   `PORT_START` / `PORT_END`: Taranacak port aralığı (Varsayılan: `1` ile `3000` arası).
*   `TIMEOUT`: Her bir bağlantı denemesi için beklenecek maksimum saniye (Varsayılan: `1`).
*   `max_workers`: Aynı anda çalışacak iş parçacığı sayısı (Varsayılan: `100`).

---

## ⚠️ Yasal Uyarı

Bu araç yalnızca **eğitim, siber güvenlik farkındalığı ve kendi sistemlerinizin güvenliğini test etme (penetrasyon testi)** amacıyla geliştirilmiştir. İzniniz olmayan hedef sistemlere karşı tarama yapmak yasal suç teşkil edebilir. Oluşabilecek tüm sorumluluk kullanıcıya aittir.
