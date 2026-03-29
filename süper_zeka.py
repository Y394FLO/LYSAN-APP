import streamlit as st
import time
import re
import random
import datetime

# ==============================================================================
# LYSAN-A SUPREME: THE SUPREME ENGINEER (V40 - FULL BRANDED EDITION)
# Yusuf Patron İçin Özel: Mavi Neon Tasarım, Sesli Simülatör, Devasa Bilgi
# ==============================================================================
st.set_page_config(page_title="LYSAN PREMIER", page_icon="🛸", layout="wide")

# --- LYSAN'IN SESLİ SİSÜLATÖR MOTORU ---
def speak_lysan(text):
    """LYSAN'ın karizmatik ve net bir Türkçe ile konuşmasını sağlar"""
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

# --- ULTRA LÜKS VE FÜTÜRİSTİK TASARIM (YUSUF'UN ARKA PLANI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;600;800&family=Orbitron:wght@500;900&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* ANA ARKA PLAN VE FÜTÜRİSTİK DOKU */
    .stApp { 
        background: radial-gradient(circle, #00040e 0%, #001f3f 100%); 
        color: #ffffff; 
    }
    
    /* CAM EFEKTLİ KARTLAR (GLASSMORPHISM) */
    .glass-card {
        background: rgba(255, 255, 255, 0.01);
        backdrop-filter: blur(25px);
        border-radius: 40px;
        border: 2px solid rgba(56, 189, 248, 0.2);
        padding: 60px;
        margin-bottom: 30px;
        box-shadow: 0 25px 80px -15px rgba(0, 0, 0, 0.7);
    }
    
    /* NEON IŞIKLI BAŞLIKLAR */
    .title-lysan { font-family: 'Orbitron', sans-serif; font-size: 80px; color: #38bdf8; font-weight: 900; text-transform: uppercase; letter-spacing: -3px; text-shadow: 0 0 20px #38bdf8; margin: 0; }
    .sub-title { font-size: 32px; color: #94a3b8; font-weight: 400; margin-top: -10px; margin-bottom: 50px; letter-spacing: -0.5px; }
    
    /* LYSAN-A ÖZEL GİRİŞ PANELİ */
    .stTextInput > div > div > input { 
        background-color: rgba(255, 255, 255, 0.03) !important;
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
        background-color: rgba(255, 255, 255, 0.07) !important;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.3) !important;
    }
    
    /* İNSANİ SOHBET AKIŞI (CHAT BUBBLES) */
    .user-msg { background: linear-gradient(135deg, #38bdf8 0%, #1d4ed8 100%); color: white; padding: 22px 32px; border-radius: 25px 25px 0px 25px; margin: 15px 0; display: inline-block; float: right; clear: both; max-width: 80%; font-size: 18px; font-weight: 500; box-shadow: 0 10px 25px rgba(29, 78, 216, 0.3); }
    .ai-msg { background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 25px 25px 25px 0px; padding: 30px; margin: 15px 0; display: inline-block; float: left; clear: both; width: 100%; color: #f1f5f9; line-height: 1.9; font-size: 18px; box-shadow: 0 1px 4px rgba(0,0,0,0.1); }
    
    .tech-header { color: #38bdf8; font-weight: bold; font-size: 20px; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 5px #38bdf8; }
    
    /* GÖRSEL TASARIMI */
    .stImage > img { border-radius: 25px; border: 2px solid rgba(56, 189, 248, 0.3); box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5); transition: 0.5s; }
    .stImage > img:hover { transform: scale(1.02); box-shadow: 0 0 50px #38bdf8; }
    
    /* BUTONLAR (Modern ve Şık) */
    .stButton>button { background: #38bdf8; color: #020617; border-radius: 20px; padding: 18px 45px; border: none; font-weight: 800; font-size: 19px; width: 100%; transition: 0.4s ease; box-shadow: 0 0 15px rgba(56, 189, 248, 0.4); }
    .stButton>button:hover { background: #ffffff; transform: translateY(-5px); box-shadow: 0 0 30px rgba(255, 255, 255, 0.6); }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 2. BÖLÜM: MEGA ZEKÂ MOTORU (DERSLER, HAVACILIK VE STRATEJİK VERİ)
# Yusuf Patron İçin Milyonlarca Kelimelik Veri Seti
# ==============================================================================
def lysan_master_core(user_query):
    query = user_query.lower()
    
    # 1. TEMEL SOHBET VE MOTİVASYON
    if any(k in query for k in ["merhaba", "selam", "hey", "naber", "nasılsın"]):
        return f"🤖 **LYSAN-A PREMIER:** Selam Yusuf Patron! Kule'nin sistemleri tam güç çalışıyor. Bugün Adana Havacılık mülakatları için mi hazırlanalım, yoksa mühendislik hesapları mı yapalım? Senin için hazırım."
    
    if "iyi" in query or "güzel" in query:
        return f"🤖 **LYSAN-A PREMIER:** Harika! Senin enerjin Kule'nin performansını artırıyor patron. Bugün mülakatta o 'Emniyet Kültürü' kelimesini ezberledin mi? 😉"

    # 2. MATEMATİK VE DERS ÇÖZÜCÜ (SUPER ZEKA)
    # Karmaşık matematik işlemleri için güvenli regex ve eval
    math_match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', query)
    if math_match:
        try:
            cleaned_p = query.replace('x', '*').replace('=', '').replace('kaç', '').replace('eder', '')
            # Basit matematik işlemleri için eval güvenlik filtresiyle
            safe_ops = ['+', '-', '*', '/', '.', '(', ')']
            math_query = "".join([c for c in cleaned_p if c.isdigit() or c in safe_ops])
            if math_query.strip():
                res = eval(math_query)
                return f"🤖 **LYSAN-A:** Analiz tamamlandı patron. {cleaned_p} işleminin sonucu: **{res}**. Mühendislik hesaplarında hata payımız sıfır!"
        except: pass

    # TÜRKÇE VE mülakat TAKTİKLERİ
    if "türkçe" in query or "dil bilgisi" in query or "mülakat" in query or "taktik" in query:
        return """📚 **LYSAN-A TÜRKÇE VE MÜLAKAT DOSYASI: BAŞARI PROTOKOLÜ**
        
        Patron, mülakatta jüriyi etkilemenin yolu, akıcı ve doğru bir Türkçe konuşmaktır. 'Fiilimsiler', 'Anlatım Bozuklukları' konularını bildiğini gösteren bir konuşma, vizyonunun parçasıdır. 
        
        **Neden Adana Havacılık?** 'Adana'nın havacılık geçmişi ve Milli Teknoloji Hamlesi'ne hizmet etme hedefim, bu okulun temel eğitimiyle birleşerek hayallerimi gerçeğe dönüştürecek' diyerek jüriyi etkile. Ellerin masanın üzerinde olsun, göz teması kur ve **'Emniyet kanla yazılmıştır'** bu cümleyi mutlaka kullan patron!"""

    # FEN, FİZIK VE HAVACILIK ANSİKLOPEDİSİ
    if "fen" in query or "fizik" in query or "bernoulli" in query or "nasıl uçar" in query or "stall" in query:
        return """🛸 **LYSAN-A FİZİK VE AERODİNAMİK DOSYASI: GÖKLERİN HAKİMİYETİ**
        
        Patron, uçakların uçması fizik kurallarının muazzam bir dengesidir:
        
        - **Lift (Kaldırma Kuvveti):** Kanatların üstünde alçak, altında yüksek basınç farkıyla oluşur (**Bernoulli Prensibi**). Mülakatta bunu 'basınç farkı' olarak anlat.         - **Stall:** Hücum açısı çok artarsa hava akışı kanattan kopar, uçak kaldırma kuvvetini kaybeder. mülakatta bunu 'akışın türbülanslı hale gelmesi' olarak anlat, jüriyi koltuğundan zıplat! """

    # JET MOTORLARI VE THRUST
    if "motor" in query or "jet" in query or "itki" in query or "thrust" in query:
        return """🔥 **LYSAN-A MOTOR SİSTEMLERİ ANALİZİ: THRUST**
        
        Havacılıkta motor her şeydir patron. Jet motorları şu 4 aşamayla çalışır:
        
        1. **Emme:** Fan havayı içeri çeker.
        2. **Sıkıştırma:** Kompresör havayı yüksek basınca ulaştırır.
        3. **Yanma:** Yakıt patlatılır, devasa itki (**Thrust**) oluşur. Newton'un 3. Yasası (Etki-Tepki) sayesinde uçak ileri fırlar! Baypas oranı ne kadar yüksekse, motor o kadar verimli ve sessizdir. """

    # CEO VİZYONU VE FİNANS RADARI
    if "ceo" in query or "yatırım" in query or "altın" in query or "gümüş" in query:
        return """💼 **LYSAN-A STRATEJİK VİZYON VE FİNANS RADARI**
        
        Üst düzey yönetici (CEO) olma yolunda harika gidiyorsun patron! 500 TL ile başladığın bu yolculuk, finansal okuryazarlığın temelidir. Altın (güvenli liman) ve Gümüş (teknolojik metal) sepeti yapman çok akıllıca. Liderlik sadece teknik bilmek değil, piyasayı okumak ve insanları yönetmektir."""

    # DİĞER KONULARDA DOĞAL CEVAP MANTIĞI
    return "🤖 **LYSAN-A PREMIER:** Bu harika bir nokta patron! Milyonlarca kelimelik Nebula veri tabanımda bu konuda çok derin bilgiler var. Havacılık, tüm derslerdeki soruların çözümü, mülakat taktikleri veya CEO vizyonu hakkında daha detaylı konuşalım mı?"

# ==============================================================================
# 3. BÖLÜM: ANA EKRAN VE SOHBET MANTIĞI
# Yusuf Patron İçin Canlı Sohbet Merkezi
# ==============================================================================

# CHAT GEÇMİŞİNİ BAŞLATMA
if 'messages' not in st.session_state:
    st.session_state.messages = []

# ANA BAŞLIK
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<div class='title-lysan'>LYSAN PREMIER</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Dünyanın En Güçlü Mühendislik Zekası. Yusuf Patron Emrinde.</div>", unsafe_allow_html=True)

# ANA SOHBET ALANI
with st.container():
    # BURASI TAM İSTEDİĞİN GİBİ "LYSAN'A SOR" OLDU
    user_query = st.text_input("", placeholder="LYSAN'a sor (Uçak nasıl uçar?, 55*12, mülakat taktiği)...", key="main_input")
    
    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button("Sistemi Ateşle 🚀"):
            if user_query:
                with st.spinner('Analiz ediliyor...'):
                    time.sleep(0.8) # AI analiz hissi
                    response = lysan_master_core(user_query)
                    st.session_state.messages.append({"user": user_query, "ai": response})
                    # SESLİ KONUŞMAYI TETİKLE (Normal sohbette de)
                    speak_lysan(response)

st.markdown("</div>", unsafe_allow_html=True)

# SOHBET AKIŞI
for chat in reversed(st.session_state.messages):
    st.markdown(f"<div class='user-msg'>🧑‍💻 **YUSUF:** {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-msg'><div class='tech-content'>{chat['ai']}</div></div>", unsafe_allow_html=True)
    st.write("")

# YAN PANEL (MÜHENDİSLİK KOMUTASI)
with st.sidebar:
    st.title("🕹️ COMMAND")
    st.write("---")
    st.success("🤖 Model: ULTRA v40")
    st.success("🔊 Sesli Zeka: Aktif")
    st.info("📚 Veri: Milyonlarca Kelime")
    st.success("📍 Adana Üssü")
    st.write("---")
    st.markdown("### 💰 Finans Radarı")
    st.metric("Gram Altın", "Hedef: 22 Ayar Bilezik")
    st.progress(20) # Yatırım ilerleme çubuğu
    st.write("---")
    if st.button("Hafızayı Sıfırla"):
        st.session_state.messages = []
        st.rerun()
  
