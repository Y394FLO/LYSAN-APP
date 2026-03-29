import os
import sys
import threading
import time
import cv2
import pyttsx3
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk

# =============================================================================
# 1. ÇEKİRDEK ZEKA VE SES MOTORU (THE BRAIN)
# =============================================================================
class LysanUltraX:
    def __init__(self, root):
        self.root = root
        self.root.title("LYSAN-ULTRA-X // NEXT-GEN AI OS")
        self.root.geometry("1100x850")
        self.root.configure(bg="#020f12") # Derin Uzay Mavisi/Siyah

        # Ses Sentezleyici (TTS)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.recognizer = sr.Recognizer()

        # Sistem Değişkenleri
        self.is_listening = False
        self.camera_on = False
        self.version = "3.0.1-GENESIS"

        self.setup_ui()
        self.log("Sistem yükleniyor... %100")
        self.log(f"Hoş geldin Pilot. LYSAN v{self.version} aktif.")
        self.speak("Sistemler aktif. Emirlerinizi bekliyorum.")

# =============================================================================
# 2. KOKPİT ARAYÜZÜ (THE INTERFACE)
# =============================================================================
    def setup_ui(self):
        # Üst Bilgi Paneli
        self.top_bar = tk.Frame(self.root, bg="#051c1f", height=50)
        self.top_bar.pack(fill=tk.X)
        
        self.header = tk.Label(self.top_bar, text="LYSAN-ULTRA-X: ADVANCED AVIONICS & AI", 
                              fg="#00ffcc", bg="#051c1f", font=("Orbitron", 18, "bold"))
        self.header.pack(pady=10)

        # Ana Ekran (Sol: Kamera/Görsel - Sağ: Konsol)
        self.display_frame = tk.Frame(self.root, bg="#020f12")
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Kamera Paneli
        self.view_panel = tk.Label(self.display_frame, text="SİSTEM BEKLEMEDE", 
                                  fg="#00ffcc", bg="#0a1a1e", font=("Consolas", 14),
                                  width=50, height=20, relief=tk.SUNKEN, bd=2)
        self.view_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Terminal / Log Ekranı
        self.terminal = scrolledtext.ScrolledText(self.display_frame, width=45, height=20, 
                                                 bg="#000000", fg="#33ff33", font=("Consolas", 10))
        self.terminal.pack(side=tk.RIGHT, fill=tk.Y, padx=5)

        # Kontrol Merkezi (Butonlar)
        self.controls = tk.Frame(self.root, bg="#051c1f", height=100)
        self.controls.pack(fill=tk.X, side=tk.BOTTOM)

        btn_cfg = {"font": ("Consolas", 11, "bold"), "width": 15, "height": 2, "bd": 3}
        
        tk.Button(self.controls, text="SESLİ KOMUT", bg="#005577", fg="white", 
                  command=self.start_listening, **btn_cfg).pack(side=tk.LEFT, padx=20, pady=20)
        
        tk.Button(self.controls, text="GÖRÜŞÜ AÇ", bg="#007755", fg="white", 
                  command=self.toggle_vision, **btn_cfg).pack(side=tk.LEFT, padx=20, pady=20)

        tk.Button(self.controls, text="HAVACILIK ANALİZ", bg="#775500", fg="white", 
                  command=self.aviation_calc, **btn_cfg).pack(side=tk.LEFT, padx=20, pady=20)

        tk.Button(self.controls, text="SİSTEMİ KAPAT", bg="#770000", fg="white", 
                  command=self.root.quit, **btn_cfg).pack(side=tk.RIGHT, padx=20, pady=20)

# =============================================================================
# 3. ÖZEL FONKSİYONLAR (CORE ABILITIES)
# =============================================================================
    def log(self, text):
        now = datetime.now().strftime("%H:%M:%S")
        self.terminal.insert(tk.END, f"[{now}] > {text}\n")
        self.terminal.see(tk.END)

    def speak(self, text):
        def _speak():
            self.engine.say(text)
            self.engine.runAndWait()
        threading.Thread(target=_speak).start()

    def start_listening(self):
        self.log("Mikrofon aktif... Dinleniyor.")
        threading.Thread(target=self.process_audio).start()

    def process_audio(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                query = self.recognizer.recognize_google(audio, language='tr-TR').lower()
                self.log(f"KOMUT: {query}")
                self.handle_command(query)
            except:
                self.log("Hata: Ses anlaşılamadı.")

    def handle_command(self, cmd):
        if "merhaba" in cmd:
            self.speak("Merhaba Pilot. Göreve hazırım.")
        elif "durum" in cmd:
            self.speak("Tüm motorlar ve AI çekirdekleri stabil durumda.")
        elif "altın" in cmd or "yatırım" in cmd:
            self.speak("Finansal veriler analiz ediliyor. Portföyünüz güvende.")
            self.show_chart()
        else:
            self.speak("Komut işleniyor, ancak veritabanı kısıtlı.")

    def toggle_vision(self):
        if not self.camera_on:
            self.camera_on = True
            self.log("Görsel sensörler aktif ediliyor...")
            threading.Thread(target=self.vision_stream).start()
        else:
            self.camera_on = False
            self.log("Görsel sensörler kapatıldı.")

    def vision_stream(self):
        cap = cv2.VideoCapture(0)
        while self.camera_on:
            ret, frame = cap.read()
            if ret:
                # Görüntüyü işle (Yüz tespiti ekleyebilirsin)
                frame = cv2.flip(frame, 1)
                img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                imgtk = ImageTk.PhotoImage(image=img)
                self.view_panel.imgtk = imgtk
                self.view_panel.configure(image=imgtk)
            time.sleep(0.01)
        cap.release()
        self.view_panel.configure(image='', text="SİSTEM BEKLEMEDE")

    def aviation_calc(self):
        """Havacılık ve Uzay Mühendisliği için basit itki simülasyonu."""
        self.log("Havacılık Modülü: İtki (Thrust) hesaplanıyor...")
        # Örnek: T = m_dot * Ve
        self.speak("Aerodinamik katsayılar optimize ediliyor. Uçuşa hazırız.")
        messagebox.showinfo("LGS/Havacılık Analiz", "Adana Havacılık Lisesi için hedef puan: 450+ \nStatü: Ulaşılabilir")

    def show_chart(self):
        """Yatırım verilerini görselleştirme."""
        data = np.random.randint(500, 600, size=10)
        plt.figure("Piyasa Analizi")
        plt.plot(data, color='cyan', marker='o')
        plt.title("Gram Altın / Yatırım Trendi")
        plt.grid(True)
        plt.show()

# =============================================================================
# 4. ATEŞLEME (LAUNCH)
# =============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = LysanUltraX(root)
    root.mainloop()
      
