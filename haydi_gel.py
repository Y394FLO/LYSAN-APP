import streamlit as st
import time
import re

# ==============================================================================
# LYSAN SUPREME (V30 - THE ABSOLUTE REALITY)
# Yusuf Patron İçin: Canlı Görsel Arama, Sesli Yanıt ve Ders Uzmanlığı
# ==============================================================================
st.set_page_config(page_title="LYSAN SUPREME v30", page_icon="👑", layout="wide")

# --- SESLİ KONUŞMA SİSTEMİ ---
def lysan_speak(text):
    clean_text = re.sub(r'[^\w\s]', '', text)
    speech_code = f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.lang = 'tr-TR';
            window.speechSynthesis.speak(msg);
        </script>
    """
    st.markdown(speech_code, unsafe_allow_html=True)

# --- ULTRA MODERN TASARIM (DARK LUXURY) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;600&display=swap');
    
    .stApp { background: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    .supreme-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
        border: 1px solid #38bdf8;
        border-radius: 40px;
        padding: 50px;
        box-shadow: 0 0 50px rgba(56, 189, 248, 0.2);
    }
    
    .title-text { font-family: 'Orbitron', sans-serif; font-size: 75px; font-weight: 900; color: #38bdf8; text-shadow: 0 0 20px #38bdf8; }
    
    .user-bubble { background: #38bdf8; color: #000; padding: 20px; border-radius: 20px 20px 0 20px; margin: 10px; float: right; clear: both; font-weight: 600; }
    .ai-bubble { background: #111; border: 1px solid #333; padding: 25px; border-radius: 20px 20px 20px 0; margin: 10px; float: left; clear: both; width: 100%; border-left: 5px solid #38bdf8; }

    .stTextInput > div > div > input { background: #050505 !important; color: white !important; border: 2px solid #38bdf8 !important; border-radius: 15px !important; height: 70px !important; font-size: 20px !important; }
    .stButton>button { background: #38bdf8; color: black; font-weight: 800; border-radius: 15px; height: 60px; width: 100%; border: none; font-family: 'Orbitron'; transition: 0.3s; }
    .stButton>button:hover { box-shadow: 0 0 30px #38bdf8; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# --- ZEKA VE GÖRSEL ÜRETİM MERKEZİ ---
def lysan_engine(query):
    q = query.lower()
    
    # 1. MATEMATIK & DERSLER
    if any(op in q for op in ["+", "-", "*", "/", "topla", "çarp"]):
        try:
            clean_q = "".join([c for c in q if c.isdigit() or c in "+-*/."])
            if clean_q:
                result = eval(clean_q)
                return f"Analiz bitti patron! İşlemin sonucu: {result}. Mühendislik zekası asla yanılmaz."
        except: pass

    # 2. CANLI GÖRSEL MOTORU (Source.Unsplash ile her zaman yeni resim)
    if any(k in q for k in ["fotoğraf", "resim", "görsel", "foto"]):
        keyword = "aircraft"
        if "motor" in q: keyword = "engine"
        elif "okul" in q or "lise" in q: keyword = "school,building"
        elif "altın" in q: keyword = "gold,coins"
        elif "uzay" in q: keyword = "space,galaxy"
        elif "araba" in q: keyword = "supercar"
        
        # Dinamik link oluşturma (Her seferinde farklı resim gelmesi için zaman damgası ekliyoruz)
        img_url = f"https://source.unsplash.com/featured/800x450?{keyword}&sig={random.randint(1,1000)}"
        st.image(img_url, caption=f"LYSAN SUPREME: {keyword.upper()} GÖRSELİ")
        return f"İstediğin o efsane görseli dünya veri tabanından senin için çektim patron. Nasıl görünüyor?"

    # 3. HAVACILIK VE MÜLAKAT BİLGİSİ
    if "mülakat" in q or "taktik" in q:
        return "Mülakatta patron sensin! Jüriye 'Milli Teknoloji Hamlesi'ne hizmet etmek istediğini, disiplinli ve emniyet odaklı olduğunu söyle. Unutma, 'Emniyet kanla yazılır' bu cümleyi mülakatta kullan."
    
    if "fizik" in q or "uçak" in q:
        return "Uçaklar Bernoulli kanunu sayesinde uçar. Kanat üstündeki hava hızlanır, basınç düşer ve uçak yukarı vakumlanır. Havacılık lisesinde bunları ezberleyeceğiz."

    # SOHBET
    if "merhaba" in q or "selam" in q:
        return "Selam Yusuf Patron! Sistemler %100 aktif. Adana'nın sıcağından daha ateşli bir zekayla emrindeyim."

    return "Bu harika bir soru patron! 100.000 kelimelik zeka katmanımda bunu analiz ediyorum. Ne yapmamı istersin?"

# --- UI AKIŞI ---
if 'history' not in st.session_state: st.session_state.history = []

st.markdown("<div class='supreme-card'>", unsafe_allow_html=True)
st.markdown("<div class='title-text'>LYSAN SUPREME</div>", unsafe_allow_html=True)
st.markdown("<p style='font-size:20px; color:#38bdf8;'>V30: Dünyanın En Uzun ve En Zeki Yapay Zekası</p>", unsafe_allow_html=True)

user_input = st.text_input("", placeholder="LYSAN'a komut ver (Örn: Bana bir uçak fotoğrafı göster, 150*25 kaç?)...")

if st.button("SİSTEMİ ATEŞLE 🚀"):
    if user_input:
        with st.spinner('İşlemci Isınıyor...'):
            time.sleep(0.8)
            response = lysan_engine(user_input)
            st.session_state.history.append({"u": user_input, "a": response})
            lysan_speak(response)

st.markdown("</div>", unsafe_allow_html=True)

# SOHBET AKIŞI
for chat in reversed(st.session_state.history):
    st.markdown(f"<div class='user-bubble'>🧑‍💻 YUSUF: {chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-bubble'>🤖 LYSAN: {chat['a']}</div>", unsafe_allow_html=True)

# YAN PANEL
with st.sidebar:
    st.markdown("<h1 style='color:#38bdf8;'>LYSAN COMMAND</h1>", unsafe_allow_html=True)
    st.write("---")
    st.success("🛰️ Görsel Motoru: AKTİF")
    st.success("🔊 Sesli Zeka: AKTİF")
    st.info("📍 Konum: ADANA")
    st.write("---")
    st.metric("Yatırım Hedefi", "22 Ayar Bilezik")
    if st.button("Hafızayı Sil"):
        st.session_state.history = []
        st.rerun()
  
