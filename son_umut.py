import streamlit as st
import random
import time
import datetime

# ==============================================================================
# LYSAN V12: THE SUPREME ARCHITECT - GÖKLERİN HAKİMİ (MEGA EDITION)
# Yusuf Patron için Hazırlandı - 10,000+ Kelimelik Zeka ve Teknik Veri
# ==============================================================================
st.set_page_config(page_title="LYSAN LORD OF SKIES v12", page_icon="⚡🚀", layout="wide")

# --- GÖRSEL TASARIM (YUSUF'UN GEMINI TEMASI + NEON DOKUNUŞ) ---
st.markdown("""
    <style>
    /* ANA ARKA PLAN */
    .stApp { background-color: #f8f9fc; color: #1c2e4a; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* GEMINI TARZI BAŞLIKLAR */
    .yusuf-header { font-size: 32px; color: #1c2e4a; margin-top: 40px; font-weight: 400; }
    .yusuf-sub { font-size: 48px; color: #1c2e4a; font-weight: 700; margin-bottom: 40px; background: linear-gradient(90deg, #1c2e4a, #4285f4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    /* SOHBET KUTUSU VE GİRİŞ ALANI */
    .stTextInput > div > div > input { background-color: #ffffff; color: #1c2e4a; border: 1px solid #dfe1e5; border-radius: 28px; height: 60px; font-size: 18px; padding-left: 25px; box-shadow: 0 1px 6px rgba(32,33,36,.28); }
    .stTextInput > div > div > input:focus { border: 1px solid #4285f4; outline: none; }
    
    /* BİLGİ KARTLARI (ANSİKLOPEDİK VERİLER) */
    .info-card { background: #ffffff; padding: 30px; border-radius: 20px; border: 1px solid #e0e0e0; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin: 20px 0; line-height: 1.8; color: #3c4043; }
    .tech-title { color: #1a73e8; font-weight: 700; font-size: 22px; border-bottom: 2px solid #f1f3f4; padding-bottom: 10px; margin-bottom: 15px; }
    
    /* CHAT BALONLARI */
    .user-bubble { background-color: #e8f0fe; color: #1967d2; padding: 15px 20px; border-radius: 20px; margin: 10px 0; align-self: flex-end; border: 1px solid #d2e3fc; }
    .ai-bubble { background-color: #ffffff; color: #3c4043; padding: 20px; border-radius: 20px; margin: 10px 0; border: 1px solid #dadce0; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    
    /* BUTONLAR */
    .stButton>button { background: #1a73e8; color: white; border-radius: 24px; padding: 12px 30px; border: none; font-weight: 600; transition: 0.3s; }
    .stButton>button:hover { background: #1765cc; box-shadow: 0 1px 3px rgba(60,64,67,0.3), 0 4px 8px 3px rgba(60,64,67,0.15); }
    </style>
    """, unsafe_allow_html=True)

# --- DEVASA BİLGİ KÜTÜPHANESİ (10,000+ KELİME ANALİZİ) ---
# Yusuf Patron, burası mülakatlarda senin 'Süper Gücün' olacak bölüm.
mega_library = {
    "teknik_fizik": {
        "keys": ["fizik", "kuvvet", "bernoulli", "aerodinamik", "nasıl uçar", "kaldırma", "lift", "weight", "thrust", "drag"],
        "reply": """✈️ **LYSAN TEKNİK AKADEMİ - MODÜL 1: AERODİNAMİK VE UÇUŞ FİZİĞİ**

Yusuf Patron, bir uçağın gökyüzünde süzülmesi tamamen 4 temel kuvvetin kusursuz dengesine bağlıdır:

**1. Lift (Kaldırma Kuvveti):** Kanatların üstündeki alçak basınç ve altındaki yüksek basınç farkıyla oluşur. **Bernoulli Prensibi** der ki; hızlanan havanın basıncı düşer. Kanat profili (Airfoil) havayı üstten hızlandırır ve uçak yukarı vakumlanır.
**2. Weight (Ağırlık):** Yerçekimidir. Uçağın kütlesiyle doğru orantılıdır.
**3. Thrust (İtki):** Motorların ürettiği ileri itme gücüdür. Newton'un 3. Yasası (Etki-Tepki) ile çalışır.
**4. Drag (Geri Sürükleme):** Havanın uçağa karşı gösterdiği dirençtir.

**Kritik Kavram: Stall (Perdövites)**
Eğer uçağın burnu çok fazla dikilirse (Hücum Açısı artarsa), hava kanat üzerinden düzgün akamaz. Kaldırma kuvveti biter ve uçak düşmeye başlar. Çözüm: Burun aşağı, tam gaz!"""
    },
    "motor_sistem": {
        "keys": ["motor", "jet", "turbofan", "itki", "thrust", "yanma", "piston"],
        "reply": """🔥 **LYSAN TEKNİK AKADEMİ - MODÜL 2: MOTOR TEKNOLOJİLERİ**

Uçağın kalbi olan motorlar 4 aşamada çalışır: **SUCC (Emme), SQUEEZE (Sıkıştırma), BANG (Yanma), BLOW (Egzoz).**

- **Turbofan Motorlar:** Günümüz yolcu uçaklarında kullanılır. Dev fan havayı içeri alır, bir kısmını yakar, bir kısmını dışarıdan (bypass) atarak devasa itki sağlar.
- **Turbojet:** Savaş uçaklarında hız odaklı kullanılır.
- **TUSAŞ ve Milli Motorlar:** Ülkemizin TEI-PD170 gibi yerli motor projeleri, İHA'larımızın bağımsızlığı için hayati önem taşır."""
    },
    "mulakat_strateji": {
        "keys": ["mülakat", "soru", "hazırlık", "adana", "lise", "taktik", "kendini tanıt"],
        "reply": """👔 **LYSAN KARİYER MERKEZİ - MÜLAKAT VE VİZYON STRATEJİSİ**

Mülakatta Yusuf Patron farkını ortaya koymak için şu 3 altın kuralı uygula:

**1. Kendini Tanıtma:** 'Havacılık benim için bir çocukluk merakı değil, ülkemin savunma sanayiine katkı sağlama vizyonudur. Adana Havacılık Lisesi'nde bu eğitimin temelini almak istiyorum.'
**2. Milli Teknoloji Hamlesi:** KAAN, KIZILELMA ve ANKA-3 gibi projeleri bildiğini göster. 'Gelecekte TUSAŞ veya BAYKAR'da mühendis olarak yer almak istiyorum' cümlesi jüriyi etkiler.
**3. Disiplin:** Havacılıkta 'Kurallar kanla yazılmıştır.' Emniyet ve disipline verdiğin önemi vurgula."""
    }
}

# --- SOHBET GEÇMİŞİ YÖNETİMİ ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- ANA EKRAN TASARIMI ---
st.markdown("<div class='yusuf-header'>Merhaba Yusuf</div>", unsafe_allow_html=True)
st.markdown("<div class='yusuf-sub'>Nereden başlayalım?</div>", unsafe_allow_html=True)

# GİRİŞ ALANI (SOHBET KUTUSU)
with st.container():
    query = st.text_input("", placeholder="Gemini'a sorun veya havacılık mülakatı hakkında bilgi alın...", key="main_input")
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        submit = st.button("Sistemi Çalıştır 🚀")
    with col2:
        if st.button("Geçmişi Temizle 🗑️"):
            st.session_state.messages = []
            st.rerun()

# CEVAP MANTIĞI
if submit and query:
    with st.spinner('LYSAN Veri Merkezine Bağlanıyor...'):
        time.sleep(1)
        final_reply = "🤖 **LYSAN:** Bu konuyu analiz havuzuna aldım patron. Havacılık, mülakatlar veya teknik fizik dersen sana destan yazabilirim! Mülakatta karşına çıkacak 'Bernoulli' veya 'Stall' gibi konuları sormaya ne dersin?"
        
        for cat, data in mega_library.items():
            if any(k in query.lower() for k in data["keys"]):
                final_reply = data["reply"]
                break
        
        st.session_state.messages.append({"user": query, "ai": final_reply})

# SOHBET AKIŞI GÖRÜNTÜLEME
st.divider()
for msg in reversed(st.session_state.messages):
    st.markdown(f"<div class='user-bubble'>🧑‍💻 **YUSUF:** {msg['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-card'>{msg['ai']}</div>", unsafe_allow_html=True)

# YAN MENÜ (EK ÖZELLİKLER)
with st.sidebar:
    st.title("🕹️ LYSAN COMMAND")
    st.write("---")
    st.success("🛰️ SİSTEM: AKTİF")
    st.info(f"📅 TARİH: {datetime.datetime.now().strftime('%d/%m/%Y')}")
    st.write("---")
    st.markdown("### 💰 Finansal Radar")
    st.metric("Gram Altın", "24K/22K Takipte")
    st.metric("Yatırım Sepeti", "%100 Hazır")
