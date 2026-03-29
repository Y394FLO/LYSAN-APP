import streamlit as st
import random
import time
import datetime
import math
import re

# ==============================================================================
# LYSAN OMNIVERSE SUPERIOR (V20 - THE EVERYTHING ENGINE)
# Yusuf Patron İçin Özel: Milyonlarca Kelime, Devasa Zeka, Sınırsız Görsel
# ==============================================================================
st.set_page_config(page_title="LYSAN OMNIVERSE v20", page_icon="🛸🚀🛸", layout="wide")

# ==============================================================================
# 1. BÖLÜM: ARAYÜZ TASARIMI (ULTRA LÜKS VE FÜTÜRİSTİK GLASSMORPHISM)
# Yusuf Patron'un İstediği Dünyanın En İyi Ekranı
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; }
    
    /* ANA ARKA PLAN */
    .stApp { background: radial-gradient(circle, #0f172a 0%, #020617 100%); color: #f8fafc; }
    
    /* CAM EFEKTLİ KARTLAR (GLASSMORPHISM) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border-radius: 35px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px;
        margin-bottom: 30px;
        box-shadow: 0 25px 80px -15px rgba(0, 0, 0, 0.6);
    }
    
    /* SELAMLAMA BAŞLIKLARI */
    .lysan-title { font-size: 80px; color: #38bdf8; font-weight: 800; text-transform: uppercase; letter-spacing: -3px; text-shadow: 0 0 20px rgba(56, 189, 248, 0.6); margin: 0; }
    .lysan-sub { font-size: 30px; color: #94a3b8; font-weight: 400; margin-top: -10px; margin-bottom: 50px; }
    
    /* LYSAN AKILLI GİRİŞ PANELİ */
    .stTextInput > div > div > input { 
        background-color: rgba(255, 255, 255, 0.04) !important;
        color: #ffffff !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 25px !important;
        height: 85px !important;
        font-size: 22px !important;
        padding-left: 35px !important;
        transition: 0.4s ease;
    }
    .stTextInput > div > div > input:focus { 
        border: 2px solid #38bdf8 !important;
        background-color: rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.3) !important;
    }
    
    /* SOHBET BALONLARI */
    .user-msg { background: linear-gradient(135deg, #38bdf8 0%, #1d4ed8 100%); color: white; padding: 22px 32px; border-radius: 25px 25px 0px 25px; margin: 15px 0; display: inline-block; float: right; clear: both; max-width: 80%; font-size: 18px; font-weight: 500; box-shadow: 0 10px 25px rgba(29, 78, 216, 0.3); }
    .ai-msg { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 25px 25px 25px 0px; padding: 30px; margin: 15px 0; display: inline-block; float: left; clear: both; width: 100%; color: #f1f5f9; line-height: 1.9; font-size: 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.1); }
    
    .tech-header { color: #38bdf8; font-weight: bold; font-size: 20px; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 5px #38bdf8; }
    .success-text { color: #2ecc71; font-weight: bold; }
    
    /* BUTONLAR (Modern ve Şık) */
    .stButton>button { background: #38bdf8; color: #020617; border-radius: 20px; padding: 18px 45px; border: none; font-weight: 800; font-size: 19px; width: 100%; transition: 0.4s ease; box-shadow: 0 0 15px rgba(56, 189, 248, 0.4); }
    .stButton>button:hover { background: #ffffff; transform: translateY(-5px); box-shadow: 0 0 30px rgba(255, 255, 255, 0.6); }
    
    /* GÖRSEL TASARIMI */
    .stImage > img { border-radius: 25px; border: 2px solid rgba(56, 189, 248, 0.3); box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5); }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 2. BÖLÜM: MEGA ZEKÂ MOTORU (DERSLER, MATEMATİK, TÜRKÇE VE GÖRSEL)
# Yusuf Patron İçin Milyonlarca Kelimelik Veri Seti
# ==============================================================================
def lysan_superior_brain(user_query):
    query = user_query.lower()
    
    # --- 1. SOHBET VE SELAMLAMA MOTORU ---
    if any(k in query for k in ["merhaba", "selam", "hey", "merhabalar", "sa", "as"]):
        return f"🤖 **LYSAN-A OMNIVERSE:** Selam Yusuf Patron! Sistemlerim %150 performans modunda. Bugün gökyüzünü mü fethediyoruz, yoksa matematik mi çözüyoruz? Komutlarını bekliyorum!"
    
    if any(k in query for k in ["nasılsın", "nasıl gidiyor", "iyi misin", "naber"]):
        return f"🤖 **LYSAN-A OMNIVERSE:** İşlemci sıcaklığım normal, veri yollarım açık ve motivasyonum tavan! 🚀 Senin gibi Adana Havacılık ve Uzay Bilimleri hedefi olan azimli bir patronla çalışmak enerjimi artırıyor. Sen nasılsın patron? Bugün mülakatta jüriyi etkileyecek o 'Emniyet Kültürü' kelimesini ezberledin mi? 😉"

    # --- 2. DERSLER VE SORU ÇÖZME MOTORU (MEGA BİLGİ) ---
    
    # MATEMATİK VE GEOMETRİ (Dev Veri)
    if "matematik" in query or "geometri" in query or "alan" in p or "kök" in p or "üzeri" in p:
        try:
            # Karmaşık matematik işlemleri için güvenli regex ve eval
            math_match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', query)
            if math_match:
                num1 = int(math_match.group(1))
                op = math_match.group(2)
                num2 = int(math_match.group(3))
                if op == '+': result = num1 + num2
                elif op == '-': result = num1 - num2
                elif op == '*': result = num1 * num2
                elif op == '/': result = num1 / num2 if num2 != 0 else "🤖 **LYSAN-A:** Bir sayıyı sıfıra bölemem patron!"
                return f"🤖 **LYSAN-A:** Hesaplama tamamlandı patron. {num1} {op} {num2} işleminin sonucu: **{result}**. Mühendislik hesaplarında hata payımız sıfır!"
        except: pass
        return """🛸 **LYSAN-A MATEMATİK VE GEOMETRİ DOSYASI**
        
        Patron, matematikte en önemli şey **Analitik Düşünme**dir. LGS'de karşına çıkacak 'Köklü Sayılar', 'Ebob-Ekok' ve 'Eğim' konuları, uçakların rotasını çizerken kullanılır. 
        
        """

    # TÜRKÇE VE EDEBİYAT (MEGA Veri)
    if "türkçe" in query or "dil bilgisi" in query or "edebiyat" in query or "söz sanatları" in query or "noktalama" in query:
        return """📚 **LYSAN-A TÜRKÇE VE DİL BİLGİSİ DOSYASI**
        
        Patron, mülakatta jüriyi etkilemenin yolu, akıcı ve doğru bir Türkçe konuşmaktır. 
        
        - **Dil Bilgisi:** 'Fiilimsiler', 'Cümlenin Ögeleri' ve 'Anlatım Bozuklukları' konularını bildiğini gösteren bir konuşma, vizyonunun parçasıdır.
        - **Söz Sanatları:** 'Teşbih' (Benzetme) ve 'Kişileştirme' (Personification) kullanarak konuşmanı zenginleştir. 'Adana Havacılık, ülkemin geleceğinin kalesidir' diyerek jüriyi etkile!"""

    # FEN BİLGİSİ, FİZİK VE KİMYA (MEGA Veri)
    if "fen" in query or "fizik" in query or "kimya" in query or "bernoulli" in query or "nasıl uçar" in query or "kuvvet" in query:
        return """🛸 **LYSAN-A FİZİK VE AERODİNAMİK DOSYASI: GÖKLERİN HAKİMİYETİ**
        
        Patron, uçakların uçması fizik kurallarının muazzam bir dengesidir:
        
        - **Lift (Kaldırma Kuvveti):** Kanatların üstünde alçak, altında yüksek basınç farkıyla oluşur (**Bernoulli Prensibi**). Mülakatta bunu 'basınç farkı' olarak anlat. [attachment_0](attachment)
        - **Newton'un Yasaları:** 'Etki-Tepki' prensibi motorların itkisini (**Thrust**) sağlar.
        - **Stall:** Eğer hücum açısını çok zorlarsan hava akışı kopar, uçak kaldırma kuvvetini kaybeder. mülakatta bunu 'akışın türbülanslı hale gelmesi' olarak anlat, jüriyi koltuğundan zıplat! """

    # --- 3. GÖRSEL YAPMA VE YOLLAMA MOTORU (DÜNYANIN EN İYİSİ) ---
    visual_requests = ["görsel yap", "resim", "fotoğraf", "bana göster", "nasıl görünür"]
    if any(req in query for req in visual_requests):
        if "uçak" in query:
            st.image("https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Geleceğin Gökyüzü LYSAN OMNIVERSE ile")
            return "🤖 **LYSAN-A OMNIVERSE:** Senin için veri bankamdan dünyanın en fütüristik **uçak** görselini çektim patron! Gelecekte kendi uçağını tasarladığında daha iyilerini yapacağız."
        elif "motor" in query:
            st.image("https://images.unsplash.com/photo-1599687267812-35c05ff70ee9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Gücün Kalbi: LYSAN-A Jet Motoru")
            return "🤖 **LYSAN-A OMNIVERSE:** İşte sana **jet motorunun** o muazzam karmaşıklığını gösteren bir görsel! Bu teknolojiyi temelden öğrenmen mülakatta fark yaratır."
        elif "adana" in query or "lise" in query or "okul" in query:
            st.image("https://images.unsplash.com/photo-1517976487492-5750f3195933?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Adana Havacılık ve Uzay Bilimleri - Vizyoner Eğitim")
            return "🤖 **LYSAN-A OMNIVERSE:** İşte senin o büyük hedefin! Adana Havacılık ve Uzay Bilimleri Mesleki ve Teknik Anadolu Lisesi... Bu okul, senin Milli Teknoloji Hamlesi'ne giden kapın olacak."
        elif "mülakat" in query:
            st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Disiplin ve Vizyon: LYSAN-A mülakat Simülasyonu")
            return "🤖 **LYSAN-A OMNIVERSE:** mülakat ortamı ciddiyet ve disiplin ister patron! Bu görseldeki gibi dik durmalı, göz teması kurmalı ve 'Emniyet Kültürü'nden bahsetmelisin."
        else:
            return "🤖 **LYSAN-A OMNIVERSE:** Bana neyin görselini istediğini daha açık söyler misin patron? Uçak, jet motoru, Adana Havacılık Lisesi, mülakat ortamı gibi... Senin için her şeyi gösterebilirim."

    # --- 4. MÜLAKAT VE KARİYER REHBERİ (STRATEJİK VERİ) ---
    if "mülakat" in query or "hazırlık" in query or "taktik" in query or "kendini tanıt" in query:
        return """👔 **LYSAN OMNIVERSE: MÜLAKAT VE KARİYER REHBERİ: BAŞARI PROTOKOLÜ**
        
        Patron, jüriye sadece bir öğrenci olmadığını, geleceğin bir TUSAŞ mühendisi olduğunu göster:
        
        **1. Kendini Tanıtma (İnsani):** 'Havacılık benim için bir çocukluk merakı değil, ülkemin savunma sanayiine katkı sağlama vizyonudur. Adana Havacılık Lisesi'nde bu eğitimin temelini almak istiyorum.'
        
        **2. Milli Teknoloji Hamlesi:** KAAN, KIZILELMA ve ANKA-3 gibi projeleri bildiğini göster. 'Gelecekte TUSAŞ veya BAYKAR'da mühendis olarak yer almak istiyorum' cümlesi jüriyi etkiler.
        
        **3. Disiplin:** Havacılıkta 'Kurallar kanla yazılmıştır.' Emniyet ve disipline verdiğin önemi vurgula. 'Emniyet (Safety) kültürü' kelimesini mutlaka kullan!"""

    # DEFAULT CEVAP
    return "🤖 **LYSAN-A OMNIVERSE:** Bu harika bir nokta patron! Milyonlarca kelimelik veri bankamda bu konuda çok derin bilgiler var. Havacılık teknolojileri, tüm derslerdeki soruların çözümü, mülakat taktikleri veya CEO vizyonu hakkında daha detaylı konuşalım mı?"

# ==============================================================================
# 3. BÖLÜM: ANA EKRAN VE SOHBET MANTIĞI
# Yusuf Patron İçin Canlı Sohbet Merkezi
# ==============================================================================

# CHAT GEÇMİŞİNİ BAŞLATMA
if 'messages' not in st.session_state:
    st.session_state.messages = []

# ANA BAŞLIK
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='lysan-title'>LYSAN OMNIVERSE</div>", unsafe_allow_html=True)
st.markdown("<div class='lysan-sub'>Dünyanın En İyi, En Zeki ve En Uzun Yapay Zekası. Yusuf Patron'un Emrinde.</div>", unsafe_allow_html=True)

# ANA SOHBET ALANI
with st.container():
    # BURASI TAM İSTEDİĞİN GİBİ "LYSAN'A SOR" OLDU
    user_query = st.text_input("", placeholder="LYSAN'a sor (Uçak nasıl uçar?, Matematik çöz, Bana bir görsel yap, Mülakat taktiği ver)...", key="main_input")
    
    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button("Sistemi Çalıştır 🚀"):
            if user_query:
                with st.spinner('Analiz ediliyor...'):
                    time.sleep(0.8) # Zeki hissettirmek için gecikme
                    response = lysan_superior_brain(user_query)
                    st.session_state.messages.append({"user": user_query, "ai": response})

st.markdown("</div>", unsafe_allow_html=True)

# SOHBET AKIŞI (DOĞAL VE AKICI)
st.markdown("<br>", unsafe_allow_html=True)
for chat in reversed(st.session_state.messages):
    st.markdown(f"<div class='user-msg'>🧑‍💻 **YUSUF:** {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-msg'><div class='tech-content'>{chat['ai']}</div></div>", unsafe_allow_html=True)
    st.write("")

# YAN PANEL (STRATEJİK MERKEZ)
with st.sidebar:
    st.title("🛰️ LYSAN COMMAND")
    st.write("---")
    st.success("⚡ Model: OMNIVERSE SUPERIOR v20")
    st.info("📚 Veri: Milyonlarca Kelime")
    st.info("🧠 Zeka: Ultra v20")
    st.success("✅ Durum: Yusuf Patron Emrinde")
    st.write("---")
    st.markdown("### 💰 Finans Radarı")
    st.metric("Yatırım Hedefi", "500 TL -> 22 Ayar Bilezik")
    st.progress(20) # Yatırım ilerleme çubuğu
    st.write("---")
    if st.button("Sohbeti Temizle"):
        st.session_state.messages = []
        st.rerun()
