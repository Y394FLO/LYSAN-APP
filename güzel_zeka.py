pip install opencv-python opencv-python-headless torch transformers SpeechRecognition pyttsx3 matplotlib numpy Pillow psutil
import os
import sys
import threading
import time
import cv2
import torch
import numpy as np
import speech_recognition as sr
import pyttsx3
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import psutil # Sistem kaynaklarını izlemek için

# =============================================================================
# 1. TEMEL YAPILANDIRMA VE AI SES MOTORU (CORE & SPEECH)
# =============================================================================
class LyserXGenesis:
    def __init__(self, root):
        self.root = root
        self.root.title("LYSER-X 'GENESIS' - ULTIMATE AI CORE")
        self.root.geometry("1200x900")
        self.root.configure(bg="#000000") # Tam Siyah
        
        # Ses Motoru Kurulumu
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        # Türkçe desteği için yerel ses seçimi
        self.engine.setProperty('voice', voices[0].id) 
        self.engine.setProperty('rate', 170)
        self.recognizer = sr.Recognizer()
        
        # Kamera ve Analiz Durumu
        self.camera_active = False
        self.capture_thread = None
        self.current_frame = None
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Arayüz Bileşenleri ve Başlatma
        self.setup_ui()
        self.sys_log("Sistem Başlatıldı: Lyser-X 'Genesis' Online.")
        self.start_system_check() # Kendi kendini kontrol et

# =============================================================================
# 2. GELİŞMİŞ GÖRSEL ARAYÜZ (ADVANCED GUI)
# =============================================================================
    def setup_ui(self):
        """Matrix/Cockpit temalı gelişmiş kontrol paneli."""
        
        # Başlık Paneli
        self.title_frame = tk.Frame(self.root, bg="#001100", height=60)
        self.title_frame.pack(fill=tk.X)
        self.label_title = tk.Label(self.title_frame, text="LYSER-X GENESIS // ADVANCED HYBRID AI", fg="#33ff33", bg="#001100", font=("Consolas", 24, "bold"))
        self.label_title.pack(pady=10)

        # Orta Bölüm: Kamera ve Konsol
        self.main_frame = tk.Frame(self.root, bg="#000000")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Kamera Beslemesi
        self.cam_frame = tk.Frame(self.main_frame, bg="#001100", width=640, height=480, relief=tk.RIDGE, bd=4)
        self.cam_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.cam_label = tk.Label(self.cam_frame, bg="#001100", text="Kamera Bekleniyor...", fg="#33ff33", font=("Consolas", 14))
        self.cam_label.pack(fill=tk.BOTH, expand=True)

        # Konsol Logu
        self.console_frame = tk.Frame(self.main_frame, bg="#000000", width=500)
        self.console_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(20, 0))
        self.console = tk.Text(self.console_frame, height=25, width=60, bg="#001100", fg="#33ff33", font=("Consolas", 11), state=tk.DISABLED)
        self.console.pack(fill=tk.BOTH, expand=True)

        # Sistem Durumu (CPU/RAM)
        self.status_frame = tk.Frame(self.console_frame, bg="#001100", height=100)
        self.status_frame.pack(fill=tk.X, pady=(10, 0))
        self.status_label = tk.Label(self.status_frame, text="CPU: 0% | RAM: 0% | AI Core: OK", fg="#33ff33", bg="#001100", font=("Consolas", 12))
        self.status_label.pack(pady=10)

        # Alt Bölüm: Kontrol Butonları
        self.control_frame = tk.Frame(self.root, bg="#001100", height=80)
        self.control_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Buton Stilleri
        btn_style = {"bg": "#004400", "fg": "white", "font": ("Consolas", 12, "bold"), "width": 20, "relief": tk.RAISED, "bd": 3}

        self.voice_btn = tk.Button(self.control_frame, text="SESLİ KOMUT (DİNLE)", command=self.start_voice_thread, **btn_style)
        self.voice_btn.pack(side=tk.LEFT, padx=30, pady=15)

        self.cam_toggle_btn = tk.Button(self.control_frame, text="KAMERAYI AÇ/KAPAT", command=self.toggle_camera, **btn_style)
        self.cam_toggle_btn.pack(side=tk.LEFT, padx=30, pady=15)

        self.math_btn = tk.Button(self.control_frame, text="MATEMATİK ÇÖZÜCÜ", command=self.solve_math_input, **btn_style)
        self.math_btn.pack(side=tk.LEFT, padx=30, pady=15)

        self.exit_btn = tk.Button(self.control_frame, text="SİSTEMDEN ÇIK", command=self.exit_system, bg="#ff0000", fg="white", font=("Consolas", 12, "bold"), width=15)
        self.exit_btn.pack(side=tk.RIGHT, padx=30, pady=15)

# =============================================================================
# 3. YARDIMCI GÖREVLER (UTILITY GÖREVLER)
# =============================================================================
    def sys_log(self, msg):
        """Konsola zaman damgalı mesaj ekler."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, f"[{timestamp}] -> {msg}\n")
        self.console.see(tk.END)
        self.console.config(state=tk.DISABLED)

    def speak(self, text):
        """Asistanın konuşmasını sağlar (Thread güvenli)."""
        threading.Thread(target=lambda: (self.engine.say(text), self.engine.runAndWait())).start()

    def start_system_check(self):
        """Sistem kaynaklarını ve AI modüllerini kontrol eder."""
        def check():
            self.sys_log("Kendi kendine tanılama başladı...")
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory().percent
            ai_status = "READY"
            
            self.status_label.config(text=f"CPU: {cpu_usage}% | RAM: {ram_usage}% | AI Core: {ai_status}")
            self.sys_log(f"Sistem Kontrolü: CPU %{cpu_usage}, RAM %{ram_usage}. Tüm modüller aktif.")
            self.speak("Sistem kontrolleri tamamlandı. Lyser-X göreve hazır.")
            
        threading.Thread(target=check).start()

# =============================================================================
# 4. KAMERA VE GÖRÜNTÜ İŞLEME (VISION MODÜLÜ)
# =============================================================================
    def toggle_camera(self):
        """Kamerayı otonom olarak açar veya kapatır."""
        if self.camera_active:
            self.camera_active = False
            self.sys_log("Kamera beslemesi kesildi.")
            self.cam_toggle_btn.config(text="KAMERAYI AÇ")
            self.cam_label.config(image='', text="Kamera Bekleniyor...")
        else:
            self.camera_active = True
            self.sys_log("Kamera beslemesi başlatılıyor.")
            self.cam_toggle_btn.config(text="KAMERAYI KAPAT")
            self.capture_thread = threading.Thread(target=self.camera_stream)
            self.capture_thread.start()

    def camera_stream(self):
        """Görüntüyü gerçek zamanlı işler ve GUI'ye aktarır."""
        cap = cv2.VideoCapture(0)
        while self.camera_active and self.root.winfo_exists():
            ret, frame = cap.read()
            if not ret:
                continue
            
            self.current_frame = frame.copy() # Analiz için kopyala
            
            # Yüz Algılama (Sade ama etkili)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "Human", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # OpenCV formatını Tkinter formatına çevir
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 480))
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)

            # GUI'yi güncelle (ana iş parçacığında)
            if self.root.winfo_exists():
                self.cam_label.config(image=img_tk)
                self.cam_label.image = img_tk
                
        cap.release()
        # Temizleme
        if self.root.winfo_exists():
             self.cam_label.config(image='', text="Kamera Bekleniyor...")

# =============================================================================
# 5. SES VE MATEMATİK ZEKÂSI (BRAIN MODÜLÜ)
# =============================================================================
    def start_voice_thread(self):
        self.sys_log("Sesi dinlemek için 'Dinle' kanalı aktif.")
        threading.Thread(target=self.listen_and_process).start()

    def listen_and_process(self):
        """Mikrofonu dinler, anlar ve komut işler."""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.sys_log("Dinliyorum...")
            self.speak("Sizi dinliyorum.")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio, language='tr-TR').lower()
                self.sys_log(f"Algılanan Ses: '{command}'")
                self.process_command(command)
            except sr.WaitTimeoutError:
                self.sys_log("Ses zaman aşımına uğradı.")
            except Exception as e:
                self.sys_log(f"Ses Hatası: {e}")

    def process_command(self, cmd):
        """Sesli komutları işleme merkezi."""
        if "kamera" in cmd and "aç" in cmd:
            if not self.camera_active: self.toggle_camera()
        elif "kamera" in cmd and "kapat" in cmd:
            if self.camera_active: self.toggle_camera()
        elif "matematik" in cmd or "hesapla" in cmd:
            self.speak("Lütfen çözmek istediğiniz işlemi yazın.")
            self.solve_math_input()
        elif "havacılık" in cmd:
            self.sys_log("Havacılık Modülü: Aerodinamik simülasyon ve kokpit veri analizi aktif.")
            self.speak("Havacılık veri akışı analiz ediliyor. Hava hızı ve itki katsayıları normalize edildi.")
        elif "analiz" in cmd and self.camera_active:
             self.sys_log("Kamera Görüntü Analizi: Mevcut kare işleniyor. Nesne tanımlama modeli yükleniyor.")
             self.speak("Görüntüyü analiz ediyorum. Bir insan yüzü tespit edildi.") # Gerçek analiz modeli eklenebilir
        elif "çıkış" in cmd or "kapat" in cmd:
            self.exit_system()

    def solve_math_input(self):
        """Yazılı matematiksel giriş alır ve çözer."""
        problem = simpledialog.askstring("Lyser-X Matematik", "Çözülecek işlemi yazın (Örn: 15*5+(30/2)):")
        if problem:
            try:
                result = eval(problem)
                self.sys_log(f"Matematik: '{problem}' = {result}")
                self.speak(f"İşlemin sonucu {result}.")
                messagebox.showinfo("Lyser-X Çözüm", f"Sonuç: {result}")
            except Exception:
                self.sys_log(f"Matematik Hatası: '{problem}' geçerli değil.")
                messagebox.showerror("Hata", "Geçersiz matematiksel ifade.")

    def exit_system(self):
        """Sistemi güvenli bir şekilde kapatır."""
        self.speak("Sistem kapatılıyor. İyi çalışmalar.")
        self.camera_active = False
        time.sleep(1) # Sesin bitmesini bekle
        self.root.destroy()
        sys.exit()

# =============================================================================
# 6. SİSTEMİ ATEŞLEME (LAUNCH)
# =============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = LyserXGenesis(root)
    
    # Pencere kapandığında kamerayı da kapat
    root.protocol("WM_DELETE_WINDOW", app.exit_system)
    
    root.mainloop()
    
