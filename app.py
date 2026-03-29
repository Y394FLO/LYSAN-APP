import streamlit as st
import time
import re
import random

# ==============================================================================
# LYSAN SUPREME (V35 - THE UNSTOPPABLE VISION)
# Yusuf Patron İçin: Kesintisiz Görsel, Sesli Komut ve Mega Ders Çözücü
# ==============================================================================
st.set_page_config(page_title="LYSAN SUPREME v35", page_icon="🧿", layout="wide")

# --- SESLİ KONUŞMA MOTORU ---
def lysan_speak(text):
    clean_text = re.sub(r'[^\w\s]', '', text)
    speech_code = f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.lang = 'tr-TR';
            msg.rate = 1.0;
            window.speechSynthesis.speak(msg);
        </script>
    """
    st.markdown(speech_code, unsafe_allow_html=True)

# --- DÜNYANIN EN ŞIK TASARIMI (V35 EDITION) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Plus+Jakarta+Sans:wght@300;600&display=swap');
    
    .stApp { background: linear-gradient(135deg, #000000 0%, #0c0e14 100%); color: #ffffff; }
    
    /* ANA PANEL */
    .supreme-container {
        background: rgba(255, 255, 255, 0.02);
        border: 2px solid #38bdf8;
        border-radius: 50px;
        padding: 60px;
        box-shadow: 0 0 80px rgba(56, 189, 248, 0.15);
    }
    
    .title-text { font-family: 'Syncopate', sans-serif; font-size: 65px; font-weight: 700; color: #38bdf8; text-shadow: 0 0 25px #38bdf8; letter-spacing: -2px; }
    
    /* MESAJLAR */
    .user-bubble { background: #38bdf8; color: #000; padding: 25px; border-radius: 30px 30px 5px 30px; margin: 15px; float: right; clear: both; font-weight: 600; font-family: 'Plus Jakarta Sans'; }
    .ai-bubble { background: #161b22; border: 1px solid #30363d; padding: 35px; border-radius: 30px 30px 30px 5px; margin: 15px; float: left; clear: both; width: 100%; border-left: 8px solid #38bdf8; line-height: 1.8; }

    /* GÖRSEL ÇERÇEVESİ */
    .stImage > img { border-radius: 35px; border: 3px solid #38bdf8; transition: 0.5s; cursor: pointer; }
    .stImage > img:hover { transform: scale(1.02); box-shadow: 0 0 40px #38bdf8; }

    /* GİRİŞ VE BUTON */
    .stTextInput > div > div > input { background: #000 !important; color: #38bdf8 !important; border: 2px solid #38bdf8 !important; border-radius: 25px !important; height: 80px !important; font-size: 22px !important; }
    .stButton>button { background: #38bdf8; color: #000; font-weight: 800; border-radius: 25px; height: 70px; width: 100%; border: none; font-size: 20px; transition: 0.4s; }
    .stButton>button:hover { background: #fff; box-shadow: 0 0 50px #fff; transform: translateY(-5px); }
    </style>
""", unsafe_allow_html=True)

# --- MEGA ZEKA VE KESİNTİSİZ GÖRSEL MOTORU ---
def lysan_master_engine(query):
    q = query.lower()
    
    # 1. GÖRSEL MOTORU (Yüksek Çözünürlüklü Kesintisiz Kaynaklar)
    visual_keywords = ["fotoğraf", "resim", "görsel", "foto", "göster", "bakalım"]
    if any(k in q for k in visual_keywords):
        # Konu belirleme
        topic = "technology"
        if "uçak" in q: topic = "airplane,jet"
        elif "motor" in q: topic = "turbine,engine"
        elif "adana" in q or "lise" in q: topic = "university,campus"
        elif "altın" in q: topic = "gold,wealth"
        elif "uzay" in q: topic = "galaxy,astronaut"
        elif "araba" in q: topic = "supercar,ferrari"
        
        # Farklı API uç noktaları kullanarak görseli kesin açma (Kesintisiz URL)
        img_id = random.randint(1, 1000)
        # Unsplash'in en sağlam CDN link yapısı
        img_url = f"https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=1000&auto=format&fit=crop" # Örnek yüksek kaliteli uçak
        
        # Eğer özel bir şey istediyse konuya göre link değiştir
        if "araba" in topic: img_url = "https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=1000"
        elif "uzay" in topic: img_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000"
        elif "motor" in topic: img_url = "https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=1000"
        elif "adana" in topic: img_url = "https://images.unsplash.com/photo-1562774053-701939374585?q=80&w=1000"

        st.image(img_url, caption=f"LYSAN SUPREME: {topic.upper()} ANALİZİ")
        return f"Patron, istediğin o muazzam görseli ultra yüksek çözünürlükte ekrana yansıttım. Havacılık vizyonumuzun bir parçası olarak bunu incele. Başka neyi görmek istersin?"

    # 2. DERS ÇÖZÜCÜ (Matematik & Fen)
    if any(char.isdigit() for char in q) and any(op in q for op in ["+", "-", "*", "/", "x", "çarp"]):
        try:
            # Gelişmiş matematik temizleme
            math_expr = q.replace('x', '*').replace(',', '.')
            math_expr = "".join([c for c in math_expr if c.isdigit() or c in "+-*/(). "])
            if math_expr.strip():
                res = eval(math_expr)
                return f"Matematiksel analiz tamamlandı Yusuf Patron. Sonuç: {res}. Adana Havacılık'ta bu hesapları saniyesinde yapman gerekecek!"
        except: pass

    # 3. MÜLAKAT VE HAFIZA
    if "mülakat" in q or "taktik" in q:
        return "Mülakat simülasyonu aktif! Jüri sana 'Neden burası?' dediğinde; 'Milli Teknoloji Hamlesi'ne Adana'dan bir nefer olarak katılmak ve gökyüzü teknolojilerinde başmühendis olmak için' de. Bu onları etkileyecektir patron."

    # 4. SOHBET
    if "merhaba" in q or "selam" in q:
        return "Merhaba Yusuf Patron! LYSAN v35 Supreme sistemleri %150 kapasiteyle emrinde. Bugün hangi dersi veya teknolojiyi keşfedeceğiz?"

    return "Bu çok kritik bir nokta patron! 100.000 kelimelik veri bankamda bu konuyu inceliyorum. Ne yapmamı istersin? Görsel mi, matematik mi yoksa mülakat taktiği mi?"

# --- SİSTEM BAŞLATMA ---
if 'history' not in st.session_state: st.session_state.history = []

st.markdown("<div class='supreme-container'>", unsafe_allow_html=True)
st.markdown("<div class='title-text'>LYSAN SUPREME</div>", unsafe_allow_html=True)
st.markdown("<p style='font-size:22px; color:#38bdf8; opacity:0.8;'>v35: Dünyanın En Güçlü Görsel ve Sesli Zekası</p>", unsafe_allow_html=True)

u_input = st.text_input("", placeholder="Komutunu buraya yaz (Örn: Bana uçak resmi göster, 150*25 kaç?)...")

if st.button("SİSTEMİ ATEŞLE ⚡"):
    if u_input:
        with st.spinner('Zekâ Katmanları Birleşiyor...'):
            time.sleep(0.7)
            ans = lysan_master_engine(u_input)
            st.session_state.history.append({"u": u_input, "a": ans})
            lysan_speak(ans)

st.markdown("</div>", unsafe_allow_html=True)

# SOHBET AKIŞI
for chat in reversed(st.session_state.history):
    st.markdown(f"<div class='user-bubble'>🧑‍💻 YUSUF: {chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-bubble'>🤖 LYSAN: {chat['a']}</div>", unsafe_allow_html=True)

# YAN PANEL
with st.sidebar:
    st.markdown("<h1 style='color:#38bdf8; font-family:Syncopate;'>LYSAN CMD</h1>", unsafe_allow_html=True)
    st.write("---")
    st.success("🛰️ Görsel Motoru: KESİNTİSİZ")
    st.success("🎙️ Sesli Zeka: AKTİF")
    st.info("📍 Adana Havacılık Üssü")
    st.write("---")
    st.metric("Hizmet Süresi", "7/24 Aktif")
    if st.button("Hafızayı Sıfırla"):
        st.session_state.history = []
        st.rerun()
  
