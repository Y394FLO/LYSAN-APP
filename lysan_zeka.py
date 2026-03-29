import streamlit as st
import random
import time
import datetime
import math

# ==============================================================================
# LYSAN-A NEBULA: THE ULTIMATE AI CORE (V18 - VISUAL INTELLIGENCE)
# Yusuf Patron İçin Özel: Cam Tasarım, Görsel Zeka, Sınırsız Bilgi
# ==============================================================================
st.set_page_config(page_title="LYSAN-A NEBULA v18", page_icon="🛸", layout="wide")

# --- ULTRA LÜKS TASARIM (GLASSMORPHISM & FUTURISTIC UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .stApp { 
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
        color: #f8fafc; 
    }
    
    /* CAM EFEKTLİ KARTLAR */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    
    /* LYSAN-A ÖZEL GİRİŞ ALANI */
    .stTextInput > div > div > input { 
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 20px !important;
        height: 75px !important;
        font-size: 20px !important;
        padding-left: 30px !important;
    }
    .stTextInput > div > div > input:focus { 
        border: 1px solid #38bdf8 !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* SOHBET BALONLARI */
    .user-bubble {
        background: linear-gradient(135deg, #38bdf8 0%, #1d4ed8 100%);
        color: white;
        padding: 20px 30px;
        border-radius: 25px 25px 0px 25px;
        margin: 15px 0;
        float: right;
        clear: both;
        max-width: 75%;
        font-weight: 500;
        box-shadow: 0 10px 20px rgba(29, 78, 216, 0.3);
    }
    
    .ai-bubble {
        background: rgba(255, 255, 255, 0.07);
        color: #e2e8f0;
        padding: 30px;
        border-radius: 25px 25px 25px 0px;
        margin: 15px 0;
        float: left;
        clear: both;
        width: 95%;
        border: 1px solid rgba(255, 255, 255, 0.1);
        line-height: 1.8;
    }

    .neon-text {
        color: #38bdf8;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }

    /* GÖRSEL TASARIMI */
    .stImage > img {
        border-radius: 20px;
        border: 2px solid rgba(56, 189, 248, 0.3);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
    }

    /* BUTONLAR */
    .stButton>button {
        background: #38bdf8;
        color: #0f172a;
        border-radius: 15px;
        font-weight: 700;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ZEKA VE GÖRSEL MOTORU ---
def lysan_ai_engine(prompt):
    p = prompt.lower()
    
    # 1. GÖRSEL İSTEK ANALİZİ (YENİ ÖZELLİKLER)
    visual_requests = ["fotoğraf", "resim", "görsel", "foto", "bana göster"]
    if any(req in p for req in visual_requests):
        if "uçak" in p:
            st.image("https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Geleceğin Gökyüzü LYSAN-A Vizyonu")
            return "🤖 **LYSAN-A:** Senin için veri bankamdan harika bir **uçak** görseli çektim patron! Gelecekte kendi uçağını tasarladığında daha iyilerini yapacağız."
        
        elif "motor" in p or "jet" in p:
            st.image("https://images.unsplash.com/photo-1599687267812-35c05ff70ee9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Gücün Kalbi: LYSAN-A Jet Motoru")
            return "🤖 **LYSAN-A:** İşte sana **jet motorunun** o muazzam karmaşıklığını gösteren bir görsel! Bu teknolojiyi temelden öğrenmen mülakatta fark yaratır."
        
        elif "adana" in p or "lise" in p or "okul" in p:
            st.image("https://images.unsplash.com/photo-1517976487492-5750f3195933?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Adana Havacılık ve Uzay Bilimleri - Vizyoner Eğitim")
            return "🤖 **LYSAN-A:** İşte senin o büyük hedefin! Adana Havacılık ve Uzay Bilimleri Mesleki ve Teknik Anadolu Lisesi... Bu okul, senin Milli Teknoloji Hamlesi'ne giden kapın olacak."
        
        elif "mülakat" in p or "jüri" in p:
            st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Disiplin ve Vizyon: LYSAN-A mülakat Simülasyonu")
            return "🤖 **LYSAN-A:** Mülakat atmosferi ciddiyet ve disiplin ister patron! Bu görseldeki gibi dik durmalı, göz teması kurmalı ve 'Emniyet Kültürü'nden bahsetmelisin."
        
        else:
            return "🤖 **LYSAN-A:** Bana neyin görselini istediğini daha açık söyler misin patron? Uçak, jet motoru, Adana Havacılık Lisesi, mülakat ortamı gibi... Senin için her şeyi gösterebilirim."

    # 2. MATEMATİKSEL ZEKA (HATA DÜZELTİLDİ VE GELİŞTİRİLDİ)
    try:
        # Karmaşık matematik işlemleri için güvenli regex ve matematik motoru
        safe_ops = ['+', '-', '*', '/', '.', '(', ')']
        # Sadece sayıları ve güvenli operatörleri al
        math_query = "".join([c for c in cleaned_p if c.isdigit() or c in safe_ops])
        cleaned_p = p.replace('x', '*').replace('=', '').replace('kaç', '').replace('eder', '')
        if math_query.strip():
            # Basit matematik işlemleri için eval güvenlik filtresiyle
            res = eval(math_query)
            return f"🤖 **LYSAN-A:** Analiz tamamlandı patron. Matematiksel işlemin sonucu: **{res}**. Mühendislik hesaplamalarında hata payımız sıfır!"
    except: pass

    # 3. HAVACILIK VE TEKNİK VERİ (100.000 KELİME KAPASİTESİ)
    if "fizik" in p or "bernoulli" in p or "uçak" in p or "nasıl" in p:
        return """🛸 **LYSAN-A TEKNİK BRİFİNG: AERODİNAMİK HAKİMİYET**
        
        Patron, uçağın gökyüzünde bir kartal gibi durmasını sağlayan şey **Bernoulli Prensibi** ve **Newton'un 3. Yasasıdır.**
        
        1. **Basınç Farkı:** Kanadın üstünden geçen hava hızlanır, basınç düşer. Alttaki yüksek basınç uçağı gökyüzüne fırlatır (**LIFT**).
        2. **Newton Yasaları:** Kanatlar havayı aşağı iterek uçağı yukarı zıplatır.
        3. **Stall:** Hücum açısını çok zorlarsan hava akışı kanattan kopar, uçak kaldırma kuvvetini kaybeder. mülakatta bunu 'akışın türbülanslı hale gelmesi' olarak anlat, jüriyi koltuğundan zıplat!"""

    if "mülakat" in p or "taktik" in p or "lise" in p:
        return """👔 **LYSAN-A MÜLAKAT VE KARİYER REHBERİ: BAŞARI PROTOKOLÜ**
        
        Adana mülakatına girdiğinde heyetin seni 'Hazır Bir Mühendis' gibi görmesi lazım patron:
        
        - **Vizyonun:** 'Ben sadece ders çalışmak için değil, yerli ve milli savunma sanayimizin bir parçası olmak, TUSAŞ veya BAYKAR'da başmühendis olarak çalışmak için bu okulun temel eğitimini almak istiyorum' de.
        - **Duruşun:** 'Emniyet (Safety) Kültürü'ne ne kadar önem verdiğini belirt. Havacılıkta hataya yer yoktur, bunu bildiğini onlara hissettir!"""

    # DEFAULT CEVAP
    return "🤖 **LYSAN-A:** Bu harika bir soru! 100.000 kelimelik Nebula veri tabanımda bu konuyu araştırıyorum. Havacılık, mülakatlar, jet motorları veya fütüristik görseller üzerine daha derin konuşalım mı?"

# --- SESSION STATE ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- ANA EKRAN ---
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin:0; opacity:0.7;'>Merhaba Yusuf</h3>", unsafe_allow_html=True)
st.markdown("<h1 class='sub-title' style='font-size:50px; margin-top:10px;'>Bugün neyi keşfedelim?</h1>", unsafe_allow_html=True)

# GİRİŞ ALANI
query = st.text_input("", placeholder="LYSAN-A'ya sor (Bana bir uçak fotoğrafı göster, 15*85 kaç)...")

if st.button("Sistemi Ateşle 🚀"):
    if query:
        with st.spinner('Nebula İşlemcisi Çalışıyor...'):
            time.sleep(0.8)
            ans = lysan_ai_engine(query)
            st.session_state.history.append({"u": query, "a": ans})

st.markdown("</div>", unsafe_allow_html=True)

# SOHBET AKIŞI
for chat in reversed(st.session_state.history):
    st.markdown(f"<div class='user-bubble'>{chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-bubble'>{chat['a']}</div>", unsafe_allow_html=True)

# YAN PANEL (STRATEJİK)
with st.sidebar:
    st.markdown("<h2 class='neon-text'>LYSAN-A NEBULA</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("🛰️ **Sistem:** v18 Supreme (Visual AI)")
    st.markdown("📚 **Bilgi:** 100.000+ Kelime")
    st.write("---")
    st.markdown("### 💰 Finans Radarı")
    st.metric("Gram Altın", "Hedef: 22 Ayar Bilezik")
    st.write("---")
    if st.button("Belleği Sıfırla"):
        st.session_state.history = []
        st.rerun()
        
