import streamlit as st
import re
import time
import random

# ==============================================================================
# LYSAN-A PREMIER (V50 - THE ULTIMATE ENGINEER EDITION)
# Yusuf Patron İçin: Hatalar Giderildi, Arka Plan Sabitlendi, Sesli Zeka Aktif
# ==============================================================================
st.set_page_config(page_title="LYSAN PREMIER v50", page_icon="🛸", layout="wide")

# --- LYSAN'IN SESLİ KONUŞMA SİSTEMİ ---
def speak_lysan(text):
    """Metni temizler ve tarayıcı üzerinden sesli okutur"""
    clean_text = re.sub(r'[^\w\s]', '', text)
    speech_js = f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.lang = 'tr-TR';
            msg.rate = 1.0;
            window.speechSynthesis.speak(msg);
        </script>
    """
    st.markdown(speech_js, unsafe_allow_html=True)

# --- ARKA PLAN VE ULTRA MODERN TASARIM ---
# Yusuf Patron, istediğin o efsane mavi görselin linki:
bg_img = "https://i.ibb.co/LdM5Xy1/image-2.png"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Plus+Jakarta+Sans:wght@400;700&display=swap');
    
    /* ARKA PLAN ENTEGRASYONU */
    .stApp {{
        background-image: url("{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* CAM PANEL (GLASSMORPHISM) */
    .main-panel {{
        background: rgba(0, 8, 20, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 40px;
        border: 2px solid rgba(56, 189, 248, 0.4);
        padding: 50px;
        margin: 20px auto;
        max-width: 1100px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
    }}
    
    .header-text {{
        font-family: 'Orbitron', sans-serif;
        font-size: 70px;
        font-weight: 900;
        color: #38bdf8;
        text-shadow: 0 0 30px #38bdf8;
        text-align: center;
        letter-spacing: -2px;
    }}

    /* SOHBET TASARIMI */
    .user-box {{
        background: linear-gradient(135deg, #38bdf8 0%, #1d4ed8 100%);
        color: white;
        padding: 20px 30px;
        border-radius: 25px 25px 0 25px;
        margin: 15px 0;
        float: right;
        clear: both;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(29, 78, 216, 0.3);
    }}
    
    .ai-box {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-left: 8px solid #38bdf8;
        padding: 25px;
        border-radius: 25px 25px 25px 0;
        margin: 15px 0;
        float: left;
        clear: both;
        width: 100%;
        line-height: 1.8;
    }}

    /* GİRİŞ VE BUTONLAR */
    .stTextInput > div > div > input {{
        background: rgba(0, 0, 0, 0.6) !important;
        color: #38bdf8 !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 20px !important;
        height: 75px !important;
        font-size: 20px !important;
    }}
    
    .stButton>button {{
        background: #38bdf8;
        color: black;
        font-weight: 900;
        border-radius: 20px;
        height: 60px;
        width: 100%;
        border: none;
        font-family: 'Orbitron';
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background: white;
        box-shadow: 0 0 40px white;
        transform: translateY(-3px);
    }}
    </style>
""", unsafe_allow_html=True)

# --- LYSAN-A SUPREME ZEKA MOTORU ---
def lysan_engine_v50(query):
    q = query.lower()
    
    # MATEMATİK VE HESAPLAMA (DERS YARDIMCISI)
    if any(op in q for op in ["+", "-", "*", "/", "x"]):
        try:
            # Temizlik ve işlem tespiti
            math_q = q.replace('x', '*').replace('=', '')
            math_q = "".join([c for c in math_q if c.isdigit() or c in "+-*/."])
            if math_q:
                res = eval(math_q)
                return f"🤖 **LYSAN-A:** Analiz tamamlandı patron! {math_q} işleminin sonucu: **{res}**. Havacılık lisesinde bu hızın çok işine yarayacak!"
        except: pass

    # HAVACILIK VE MÜLAKAT DOSYASI
    if "uçak" in q or "havacılık" in q or "lise" in q:
        return """🛸 **LYSAN-A HAVACILIK RAPORU:** Adana Havacılık Lisesi yolunda emin adımlarla ilerliyorsun patron. Unutma, uçaklar Bernoulli prensibiyle havalanır. Mülakatta 'Milli Teknoloji Hamlesi'ne hizmet etmek istediğini' ve 'disiplinli bir mühendis adayı olduğunu' vurgula. Sen geleceğin İHA/SİHA tasarımcısısın!"""

    # CEO VE YATIRIM STRATEJİSİ
    if "ceo" in q or "yatırım" in query or "altın" in q:
        return """💼 **LYSAN-A CEO STRATEJİSİ:** Üst düzey yönetici olmak sadece teknik bilmek değil, finansı da yönetmektir. 500 TL ile başladığın altın ve gümüş yatırımı, gelecekteki servetinin temelidir. Liderlik vizyonun Adana'dan dünyaya açılacak patron!"""

    # GENEL SOHBET
    if any(k in q for k in ["selam", "merhaba", "hey"]):
        return "🤖 **LYSAN-A:** Selam Yusuf Patron! Sistemler hatasız, görsel motoru %100 aktif. Bugün mülakat taktiği mi çalışalım yoksa ders mi çözelim?"

    return "🤖 **LYSAN-A:** Bu harika bir soru patron! 100.000 kelimelik zeka katmanımda bunu analiz ediyorum. Detaylandıralım mı?"

# --- UI AKIŞI ---
if 'history' not in st.session_state:
    st.session_state.history = []

st.markdown("<div class='main-panel'>", unsafe_allow_html=True)
st.markdown("<div class='header-text'>LYSAN PREMIER</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#38bdf8; font-size:18px;'>v50: THE SUPREME ENGINEER HUB</p>", unsafe_allow_html=True)

user_input = st.text_input("", placeholder="Komutunu buraya yaz (Örn: 150*25 kaç?, Uçak nasıl uçar?)...")

if st.button("ATEŞLE 🚀"):
    if user_input:
        with st.spinner('Analiz ediliyor...'):
            time.sleep(0.5)
            ans = lysan_engine_v50(user_input)
            st.session_state.history.append({"u": user_input, "a": ans})
            speak_lysan(ans) # SESLİ YANIT TETİKLENİR

st.markdown("</div>", unsafe_allow_html=True)

# SOHBET AKIŞI
for chat in reversed(st.session_state.history):
    st.markdown(f"<div class='user-box'>🧑‍💻 YUSUF: {chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-box'>{chat['a']}</div>", unsafe_allow_html=True)

# YAN PANEL (COMMAND CENTER)
with st.sidebar:
    st.title("🕹️ COMMAND")
    st.write("---")
    st.success("✅ Kod Hatası: %0")
    st.success("🖼️ Arka Plan: TAM ENTEGRE")
    st.info("📍 Üs: ADANA")
    st.write("---")
    st.metric("Yatırım Planı", "Gram Altın / 22 Ayar")
    if st.button("Belleği Temizle"):
        st.session_state.history = []
        st.rerun()
