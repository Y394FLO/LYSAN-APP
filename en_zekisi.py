import streamlit as st
import time
import re
import base64

# ==============================================================================
# LYSAN GENESIS (V25 - THE ULTIMATE SUPREME AI)
# Yusuf Patron İçin: Sesli Konuşma, Görsel Motoru ve Tüm Derslerde Uzmanlık
# ==============================================================================
st.set_page_config(page_title="LYSAN GENESIS v25", page_icon="🎙️🚀", layout="wide")

# --- SESLİ KONUŞMA FONKSİYONU (TEXT-TO-SPEECH) ---
def speak_text(text):
    """LYSAN'ın sesli cevap vermesini sağlayan motor"""
    clean_text = re.sub(r'[^\w\s]', '', text) # HTML ve Markdown temizleme
    # Tarayıcı üzerinden konuşma tetikleyici
    speech_script = f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.lang = 'tr-TR';
            msg.rate = 1.0;
            window.speechSynthesis.speak(msg);
        </script>
    """
    st.markdown(speech_script, unsafe_allow_html=True)

# --- ULTRA LÜKS TASARIM (NEBULA DARK MODE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
    
    * { font-family: 'Space Grotesk', sans-serif; }
    .stApp { background: #050505; color: #ffffff; }
    
    /* CAM TASARIM */
    .genesis-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(30px);
        border-radius: 40px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 60px;
        box-shadow: 0 0 100px rgba(56, 189, 248, 0.1);
    }
    
    .main-title { font-size: 90px; font-weight: 700; background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -4px; }
    
    /* MESAJ BALONLARI */
    .user-box { background: #1e293b; border-radius: 25px 25px 0 25px; padding: 25px; margin: 15px 0; float: right; clear: both; max-width: 80%; border: 1px solid #334155; }
    .ai-box { background: rgba(56, 189, 248, 0.05); border-radius: 25px 25px 25px 0; padding: 30px; margin: 15px 0; float: left; clear: both; width: 100%; border: 1px solid rgba(56, 189, 248, 0.3); line-height: 2; }

    /* GİRİŞ ALANI */
    .stTextInput > div > div > input { background: transparent !important; color: white !important; border: 2px solid #38bdf8 !important; border-radius: 100px !important; height: 80px !important; font-size: 22px !important; padding: 0 40px !important; }
    
    /* BUTON */
    .stButton>button { background: linear-gradient(90deg, #38bdf8, #818cf8); color: black; border-radius: 100px; height: 60px; font-weight: 700; border: none; width: 100%; transition: 0.5s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 40px rgba(56, 189, 248, 0.5); }
    </style>
""", unsafe_allow_html=True)

# --- MEGA ZEKÂ MOTORU ---
def lysan_genesis_engine(q):
    q = q.lower()
    
    # 1. GÖRSEL MOTORU (DÜNYANIN EN İYİLERİ)
    if any(k in q for k in ["fotoğraf", "resim", "görsel", "foto", "göster"]):
        if "uçak" in q:
            st.image("https://images.unsplash.com/photo-1464037192406-61123a31c62b?q=80&w=2070&auto=format&fit=crop", caption="LYSAN GENESIS: Havacılık Vizyonu")
            return "İşte patron, gökyüzünün hakimi bir canavar! Senin için en asil uçak fotoğrafını buldum."
        elif "motor" in q:
            st.image("https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=2070&auto=format&fit=crop", caption="LYSAN GENESIS: Jet Mühendisliği")
            return "Bu motorun sesi, başarının sesidir patron. Teknik mükemmellik budur."
        elif "adana" in q or "lise" in q:
            st.image("https://images.unsplash.com/photo-1546410531-bb4caa1b424d?q=80&w=2069&auto=format&fit=crop", caption="Hedef: Adana Havacılık Lisesi")
            return "Gireceğin o okul, gelecekteki başmühendislik kariyerinin ilk adımı olacak."
        elif "altın" in q or "para" in q:
            st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2070&auto=format&fit=crop", caption="Finansal Özgürlük")
            return "Yatırımların değerlensin, kasan dolsun patron! 22 ayar hedefimize az kaldı."
    
    # 2. DERS ÇÖZÜCÜ (MATEMATİK, TÜRKÇE, FEN)
    math_match = re.findall(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', q)
    if math_match:
        n1, op, n2 = math_match[0]
        res = eval(f"{n1}{op}{n2}")
        return f"Matematik sorusunu çözdüm patron. {n1} ve {n2} sayılarının işlem sonucu tam olarak {res}. Mühendislikte hata istemeyiz!"

    if "türkçe" in q or "sıfat" in q or "zarf" in q:
        return "Türkçe dil bilgisi uzmanlığım aktif. Sıfatlar isimleri niteler, zarflar fiilleri etkiler patron. Mülakatta kelimelerini bir kuyumcu gibi seçmelisin."

    if "fizik" in q or "kuvvet" in q or "basınç" in q:
        return "Bernoulli prensibi der ki: Akışkan hızı artarsa basınç düşer. Uçakların havalanma sırrı bu basit denklemde saklıdır."

    # 3. GENEL SOHBET
    if any(k in q for k in ["merhaba", "selam", "naber", "nasılsın"]):
        return "Merhaba Yusuf Patron! Genesis sistemleri %100 kapasiteyle emrinde. Bugün dünyayı nasıl değiştireceğiz?"

    return "Bu çok zekice bir soru patron! 100.000 kelimelik veri bankamda analiz ediyorum. Havacılık, dersler veya görsel taleplerin için buradayım."

# --- UYGULAMA AKIŞI ---
if 'chat' not in st.session_state: st.session_state.chat = []

st.markdown("<div class='genesis-card'>", unsafe_allow_html=True)
st.markdown("<div class='main-title'>LYSAN GENESIS</div>", unsafe_allow_html=True)
st.markdown("<p style='font-size:24px; opacity:0.6;'>Sesli, Görsel ve Ultra Zeki. Yusuf Patron'un Teknoloji Üssü.</p>", unsafe_allow_html=True)

# GİRİŞ PANELİ
user_input = st.text_input("", placeholder="LYSAN'a sor veya bir fotoğraf iste (Örn: 55*12, Bana uçak resmi göster)...")

if st.button("SİSTEMİ ATEŞLE ⚡"):
    if user_input:
        with st.spinner('Zekâ Katmanları İşleniyor...'):
            time.sleep(1)
            response = lysan_genesis_engine(user_input)
            st.session_state.chat.append({"u": user_input, "a": response})
            # SESLİ KONUŞMAYI TETİKLE
            speak_text(response)

st.markdown("</div>", unsafe_allow_html=True)

# SOHBET GEÇMİŞİ
for msg in reversed(st.session_state.chat):
    st.markdown(f"<div class='user-box'>🧑‍💻 **YUSUF:** {msg['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-box'>🤖 **LYSAN-A:** {msg['a']}</div>", unsafe_allow_html=True)

# YAN PANEL
with st.sidebar:
    st.markdown("<h2 style='color:#38bdf8'>🚀 KOMUTA MERKEZİ</h2>", unsafe_allow_html=True)
    st.write("---")
    st.success("🎙️ SESLİ KONUŞMA: AKTİF")
    st.success("🖼️ GÖRSEL MOTOR: AKTİF")
    st.info("📚 DERS KÜTÜPHANESİ: FULL")
    st.write("---")
    st.markdown("### 💰 YATIRIM DURUMU")
    st.metric("Gram Altın", "500 TL Başlangıç")
    if st.button("Belleği Temizle"):
        st.session_state.chat = []
        st.rerun()
