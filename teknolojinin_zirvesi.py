import os
import sys
import cv2
import torch
import numpy as np
import speech_recognition as sr
import pyttsx3
import matplotlib.pyplot as plt
from PIL import Image
from transformers import pipeline, VitImageProcessor, ViTForImageClassification
import google.generativeai as genai  # Ana beyin ünitesi

# ==========================================
# 1. ÇEKİRDEK YAPILANDIRMA (CORE CONFIG)
# ==========================================
class LysanOmega:
    def __init__(self):
        self.name = "LYSAN"
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        
        # Ses Ayarları
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id) # Türkçe desteği için yerel ses
        self.engine.setProperty('rate', 170)
        
        # Matematik ve Bilgi İşlem Motoru
        print(f"[{self.name}]: Sistem yükleniyor... En yüksek zeka seviyesi aktif.")
        
    def speak(self, text):
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Dinleniyor...")
            audio = self.recognizer.listen(source)
            try:
                query = self.recognizer.recognize_google(audio, language='tr-TR')
                print(f"Siz: {query}")
                return query.lower()
            except Exception:
                return ""

# ==========================================
# 2. GÖRSEL VE MATEMATİKSEL ZEKÂ (VISION & MATH)
# ==========================================
    def analyze_image(self, image_path):
        """Fotoğraftaki nesneleri ve metinleri (Ders soruları dahil) analiz eder."""
        # Burada ViT (Vision Transformer) veya benzeri bir model kullanılabilir
        processor = VitImageProcessor.from_pretrained('google/vit-base-patch16-224')
        model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
        
        image = Image.open(image_path)
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        return model.config.id2label[predicted_class_idx]

    def solve_math(self, expression):
        """Karmaşık matematiksel denklemleri çözer."""
        try:
            # Eval kullanımı basit işlemler içindir, ileri seviye için SymPy entegre edilebilir
            result = eval(expression.replace('x', '*'))
            return f"İşlemin sonucu: {result}"
        except Exception as e:
            return "Matematiksel hata: Denklemi kontrol et."

# ==========================================
# 3. GÖRSEL ÜRETİM VE ARAYÜZ (GEN-ART)
# ==========================================
    def generate_visual_report(self, data_list, title="Piyasa Analizi"):
        """Finansal veriler veya ders notları için görsel grafik oluşturur."""
        plt.figure(figsize=(10, 6))
        plt.plot(data_list, marker='o', linestyle='-', color='b')
        plt.title(title)
        plt.grid(True)
        plt.show()

# ==========================================
# 4. ANA KARAR MEKANİZMASI (DECISION ENGINE)
# ==========================================
    def execute(self):
        self.speak("Merhaba, ben LYSAN. Dünyanın en gelişmiş hibrit zekası hazır. Ne yapmamı istersin?")
        
        while True:
            command = self.listen()
            
            if "fotoğraf analiz" in command:
                self.speak("Lütfen analiz edilecek dosya yolunu belirtin.")
                # Örn: analyze_image("soru.jpg")
                
            elif "hesapla" in command:
                problem = command.replace("hesapla", "").strip()
                result = self.solve_math(problem)
                self.speak(result)
                
            elif "grafik çiz" in command:
                # Yatırım verileri için otomatik grafik
                test_data = [500, 520, 515, 550, 580] # Örnek portföy artışı
                self.generate_visual_report(test_data, "Yatırım Takip Grafiği")
                
            elif "kimsin" in command:
                self.speak("Ben havacılık, uzay, finans ve yazılım konularında uzmanlaşmış, tüm birikimlerinin birleşimi olan en güçlü yapay zekayım.")

            elif "çıkış" in command or "kapat" in command:
                self.speak("Sistem kapatılıyor. İyi çalışmalar.")
                break

# ==========================================
# 5. ÇALIŞTIRMA
# ==========================================
if __name__ == "__main__":
    lysan = LysanOmega()
    lysan.execute()
      
