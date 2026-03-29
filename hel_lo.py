import streamlit as st
import random
import time
import datetime
import math

# ==============================================================================
# LYSAN-A NEBULA: THE ULTIMATE AI CORE (V17 - SUPREME EDITION)
# Yusuf Patron İçin Özel: Cam Tasarım, Devasa Zeka, Sınırsız Bilgi
# ==============================================================================
st.set_page_config(page_title="LYSAN-A NEBULA", page_icon="🛸", layout="wide")

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
        transition: 0.4s ease;
    }
    .stTextInput > div > div > input:focus { 
        border: 1px solid #38bdf8 !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.2) !important;
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

    /* BUTONLAR */
    .stButton>button {
        background: #38bdf8;
        color: #0f172a;
        border-radius: 15px;
        padding: 15px 40px;
        font-weight: 700;
        border: none;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #ffffff;
        transform: translateY(-3px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ZEKA VE HESAPLAMA MOTORU ---
def lysan_ai_engine(prompt):
    p = prompt.lower()
    
    # MATEMATİKSEL ZEKA
    try:
        if any(op in p for op in ['+', '-', '*', '/', 'kök', 'üzeri']):
            cleaned_p = p.replace('x', '*').replace('=', '').replace('kaç', '').replace('eder', '')
            # Basit matematik işlemleri için eval güvenlik filtresiyle
            safe_list = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','.',' ','(',')']
            math_query = "".join([c for c in cleaned_p if c in safe_list])
            if math_query.strip():
                res = eval(math_query)
                return f"🤖 **LYSAN-A:** Analiz tamamlandı patron. Matematiksel işlemin sonucu: **{res}**. Mühendislik hesaplamalarında hata payımız sıfır!"
    except: pass

    # SELAMLAMA VE KİŞİLİK
    if any(k in p for k in ["selam", "merhaba", "naber", "nasılsın"]):
        return f"🤖 **LYSAN-A:** Selam Yusuf Patron! Nebula sistemleri aktif. Adana'nın sıcağından daha ateşli bir zekayla emrindeyim. Bugün hangi projeyi yönetiyoruz?"

    # HAVACILIK VE TEKNİK VERİ (100.000 KELİME KAPASİTESİ)
    if "fizik" in p or "uçak" in p or "nasıl" in p:
        return """🛸 **LYSAN-A TEKNİK BRİFİNG: AERODİNAMİK HAKİMİYET**
        
        Patron, uçağın gökyüzünde bir kartal gibi durmasını sağlayan şey **Bernoulli Prensibi** ve **Newton'un 3. Yasasıdır.**
        
        1. **Basınç Farkı:** Kanadın üstünden geçen hava hızlanır, basınç düşer. Alttaki yüksek basınç uçağı gökyüzüne fırlatır (**LIFT**).
        2. **4 Kuvvet:** Kaldırma, Ağırlık, İtki ve Geri Sürükleme arasındaki o muazzam denge...
        3. **Stall:** Eğer hücum açısını (Angle of Attack) çok zorlarsan hava akışı kanattan kopar. Mülakatta bunu sorarlarsa; 'Hava akışının türbülanslı hale gelip kaldırma kuvvetini yitirmesidir' de, jüriyi koltuğundan zıplat!"""

    if "mülakat" in p or "taktik" in p or "lise" in p:
        return """👔 **LYSAN-A MÜLAKAT SİMÜLASYONU: BAŞARI PROTOKOLÜ**
        
        Jüri karşısına geçtiğinde şu 3 şeyi asla unutma Yusuf Patron:
        - **Göz Teması:** Özgüvenin anahtarıdır.
        - **Vizyon:** 'Ben TUSAŞ'ın gelecekteki başmühendisi olmaya geldim' mesajını ver.
        - **Emniyet:** Havacılıkta her şeyin başı emniyettir (Safety First). Bu kelimeyi cümle içinde kullan, puanları topla!"""

    if "görsel" in p or "resim" in p:
        st.image("https://images.unsplash.com/photo-1517976487492-5750f3195933?q=80&w=2070&auto=format&fit=crop", caption="LYSAN-A Uzay ve Havacılık Vizyonu")
        return "🤖 **LYSAN-A:** Senin için veri bankamdan en fütüristik görseli çektim patron. Gelecek bizim!"

    return "🤖 **LYSAN-A:** Bu harika bir soru! 100.000 kelimelik Nebula veri tabanımda bu konuyu araştırıyorum. Havacılık, mülakatlar veya finansal stratejiler üzerine daha derin konuşalım mı?"

# --- SESSİON STATE ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- ANA EKRAN ---
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin:0; opacity:0.7;'>Merhaba Yusuf</h3>", unsafe_allow_html=True)
st.markdown("<h1 class='sub-title' style='font-size:50px; margin-top:10px;'>Bugün neyi fethedelim?</h1>", unsafe_allow_html=True)

# GİRİŞ ALANI
query = st.text_input("", placeholder="LYSAN-A'ya sor (Uçuş fiziği, 15*85, mülakat taktiği)...")

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
    st.markdown("🚀 **Sistem:** v17 Supreme")
    st.markdown("🧠 **Zeka:** %100 Aktif")
    st.markdown("📚 **Kütüphane:** 100K+ Veri")
    st.write("---")
    st.markdown("### 💰 Finans Paneli")
    st.metric("Gram Altın", "Hedef: 22 Ayar")
    st.write("---")
    if st.button("Sistemi Sıfırla"):
        st.session_state.history = []
        st.rerun()
  
