import streamlit as st
import re
import time

# ==============================================================================
# LYSAN-A PREMIER (V42 - ERROR FIX & FULL VISUAL)
# Yusuf Patron İçin: Hata Düzeltildi, Arka Plan Tam Entegre, Sesli Zeka Aktif
# ==============================================================================
st.set_page_config(page_title="LYSAN PREMIER", page_icon="🛸", layout="wide")

# --- SES MOTORU ---
def speak_lysan(text):
    clean_text = re.sub(r'[^\w\s]', '', text)
    speech_code = f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.lang = 'tr-TR';
            window.speechSynthesis.speak(msg);
        </script>
    """
    st.markdown(speech_code, unsafe_allow_html=True)

# --- ARKA PLAN VE TASARIM (HATASIZ CSS) ---
# Gönderdiğin o muazzam mavi görselin URL'si:
bg_url = "https://i.ibb.co/LdM5Xy1/image-2.png"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Plus+Jakarta+Sans:wght@400;700&display=swap');
    
    .stApp {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* CAM PANEL (Okunabilirlik için hafif karartma) */
    .glass-panel {{
        background: rgba(0, 5, 15, 0.65);
        backdrop-filter: blur(10px);
        border-radius: 35px;
        border: 1px solid rgba(56, 189, 248, 0.4);
        padding: 40px;
        margin-bottom: 20px;
    }}
    
    .lysan-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 60px;
        color: #38bdf8;
        text-shadow: 0 0 20px #38bdf8;
        text-align: center;
    }}

    /* SOHBET BALONLARI */
    .user-bubble {{
        background: rgba(56, 189, 248, 0.8);
        color: white;
        padding: 15px 25px;
        border-radius: 20px 20px 0 20px;
        margin: 10px 0;
        float: right;
        clear: both;
    }}
    
    .ai-bubble {{
        background: rgba(255, 255, 255, 0.05);
        border-left: 5px solid #38bdf8;
        padding: 20px;
        border-radius: 0 20px 20px 20px;
        margin: 10px 0;
        float: left;
        clear: both;
        width: 100%;
    }}

    .stTextInput > div > div > input {{
        background: rgba(0,0,0,0.5) !important;
        color: white !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 15px !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- ZEKA MOTORU ---
def lysan_engine(query):
    q = query.lower()
    if any(k in q for k in ["selam", "merhaba"]):
        return "Selam Yusuf Patron! Sistem hatasız ve tam güçte emrinde. Bugün gökyüzünü fethedelim mi?"
    
    # Matematik çözücü
    if any(op in q for op in ["+", "-", "*", "/"]):
        try:
            # Sadece matematiksel karakterleri al
            math_q = "".join([c for c in q if c.isdigit() or c in "+-*/."])
            return f"Hesaplama tamamlandı patron: {eval(math_q)}. Mühendislikte hata istemeyiz!"
        except: pass

    if "mülakat" in q:
        return "Mülakatta dik dur patron! 'Milli Teknoloji Hamlesi' ve 'Emniyet Kültürü' kelimelerini kullanmayı unutma. Sen Adana'nın gelecekteki başmühendisisin."

    return "Bu çok zekice bir soru! Veri bankamda analiz ediyorum. Ne yapmamı istersin?"

# --- ANA EKRAN ---
if 'history' not in st.session_state:
    st.session_state.history = []

st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
st.markdown("<div class='lysan-title'>LYSAN PREMIER</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#38bdf8;'>V42: Hata Düzeltildi & Tam Görsel Entegre</p>", unsafe_allow_html=True)

user_q = st.text_input("", placeholder="Komutunu buraya yaz...")

if st.button("ATEŞLE 🚀"):
    if user_q:
        response = lysan_engine(user_q)
        st.session_state.history.append({"u": user_q, "a": response})
        speak_lysan(response)

st.markdown("</div>", unsafe_allow_html=True)

# Sohbet akışı
for chat in reversed(st.session_state.history):
    st.markdown(f"<div class='user-bubble'>{chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-bubble'>🤖 {chat['a']}</div>", unsafe_allow_html=True)

with st.sidebar:
    st.title("🛰️ COMMAND CENTER")
    st.write("---")
    st.success("✅ Kod Hatası: GİDERİLDİ")
    st.success("🖼️ Arka Plan: AKTİF")
    st.info("📍 Konum: ADANA")
    if st.button("Temizle"):
        st.session_state.history = []
        st.rerun()
        
