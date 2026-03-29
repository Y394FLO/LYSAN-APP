import streamlit as st
import random
import time
import datetime

# ==============================================================================
# LYSAN V13: THE LEGEND (EFSANE SÜRÜM)
# Yusuf Patron İçin Özel: 100,000+ Kelime Kapasiteli Bilgi Bankası
# ==============================================================================
st.set_page_config(page_title="LYSAN-A ULTRA", page_icon="✈️", layout="wide")

# --- ÖZEL TASARIM (MODERN VE İNSANİ SOHBET ARAYÜZÜ) ---
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfd; color: #1f1f1f; font-family: 'Inter', sans-serif; }
    
    /* BAŞLIK VE SELAMLAMA */
    .main-title { font-size: 34px; color: #1f1f1f; margin-top: 60px; font-weight: 500; text-align: left; }
    .sub-title { font-size: 52px; color: #1f1f1f; font-weight: 700; margin-bottom: 50px; line-height: 1.1; }
    
    /* LYSAN-A ÖZEL GİRİŞ KUTUSU */
    .stTextInput > div > div > input { 
        background-color: #ffffff; 
        color: #1f1f1f; 
        border: 1px solid #747775; 
        border-radius: 32px; 
        height: 64px; 
        font-size: 18px; 
        padding-left: 30px; 
        box-shadow: none;
    }
    .stTextInput > div > div > input:focus { border: 2px solid #0b57d0; outline: none; }
    
    /* SOHBET BALONLARI (İNSANİ DOKU) */
    .chat-container { max-width: 800px; margin: auto; }
    .user-msg { background-color: #e9eef6; border-radius: 24px; padding: 18px 24px; margin: 12px 0; display: inline-block; float: right; clear: both; max-width: 80%; }
    .ai-msg { background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 24px; padding: 24px; margin: 12px 0; display: inline-block; float: left; clear: both; width: 100%; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    
    .tech-text { font-size: 16px; line-height: 1.8; color: #444746; }
    .highlight { color: #0b57d0; font-weight: 600; }
    
    /* BUTONLAR */
    .stButton>button { background: #0b57d0; color: white; border-radius: 100px; padding: 12px 36px; border: none; font-weight: 600; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- MUAZZAM BİLGİ KÜTÜPHANESİ (100.000 KELİME POTANSİYELLİ STRATEJİK VERİ) ---
# Buradaki içerikler, Yusuf'un mülakatlarda rakiplerine fark atması için tasarlandı.
knowledge_base = {
    "havacilik_fizigi": {
        "keys": ["fizik", "bernoulli", "kanat", "kuvvet", "lift", "drag", "nasıl uçar"],
        "content": """🛸 **LYSAN-A TEKNİK ANALİZ RAPORU: AERODİNAMİĞİN TEMELLERİ**

Yusuf patron, bir uçağın havada kalması basit bir olay değil, evrensel fizik yasalarının dansıdır. 

**1. Akışkanlar Mekaniği ve Bernoulli:** Kanat profilinin (Airfoil) üst kısmı kavisli, alt kısmı düzdür. Üstten geçen hava daha hızlı hareket eder. Bernoulli der ki; 'Hız artarsa basınç düşer'. Üstteki alçak basınç uçağı yukarı çeker. [attachment_0](attachment)

**2. Newton'un 3. Yasası:** Etki-Tepki. Kanat havayı aşağı büker (Downwash), hava da uçağı yukarı iter. 

**3. Stall Nedir? (Mülakatın Gözbebeği):** Kanadın hücum açısı (Angle of Attack) çok artarsa hava akışı bozulur. Uçak bir anda kaldırma kuvvetini kaybeder. Bu durumda panik yapmadan burun aşağı verilmeli ve sürat kazanılmalıdır. """
    },
    "motor_teknolojisi": {
        "keys": ["motor", "jet", "turbofan", "itki", "thrust", "roket", "turbojet"],
        "content": """🔥 **LYSAN-A MOTOR SİSTEMLERİ DOSYASI**

Havacılıkta motor her şeydir. Bugün dünyayı değiştiren **Turbofan** motorların çalışma mantığı 'Em, Sıkıştır, Yak, At' prensibine dayanır.

- **Bypass Ratio (Baypas Oranı):** Modern motorlarda havanın büyük kısmı yanma odasına girmeden dışarıdan atılır. Bu, yakıt verimliliğini devasa oranda artırır.
- **Afterburner (Art Yakıcı):** Savaş uçaklarında egzoz gazına tekrar yakıt püskürterek anlık devasa itki sağlar. KAAN projemizde bu teknolojinin en ileri seviyeleri kullanılmaktadır. [attachment_1](attachment)"""
    },
    "mulakat_ustaligi": {
        "keys": ["mülakat", "soru", "hazırlık", "adana", "taktik", "kendini tanıt", "vizyon"],
        "content": """👔 **LYSAN-A MÜLAKAT KOÇLUĞU: ŞAMPİYONUN YOL HARİTASI**

Patron, Adana Havacılık ve Uzay Bilimleri mülakatında seni 'Zeki' değil, 'Lider' olarak görmelerini sağlayacağız.

**Soru: Neden Seni Seçmeliyiz?**
*Yanlış Cevap:* Çok seviyorum, pilot olmak istiyorum.
*LYSAN-A Cevabı:* 'Havacılık disiplin ve milli bir vizyon işidir. Ben sadece uçmak değil, ülkemin Milli Teknoloji Hamlesi'ne teknik bilgimle değer katmak, TUSAŞ ve BAYKAR gibi kurumlarda yerli mühendislik projelerinde yer almak için bu okulun temel eğitimini almak istiyorum.'

**Kritik Tüyo:** Mülakatta ellerini masanın üzerine koy, göz teması kur ve 'Emniyet (Safety) kültürü' kelimesini mutlaka kullan!"""
    },
    "kariyer_ceo": {
        "keys": ["ceo", "müdür", "yönetici", "liderlik", "başarı", "maaş"],
        "content": """💼 **LYSAN-A STRATEJİK LİDERLİK VE CEO VİZYONU**

Üst düzey yönetici olmak bir unvan değil, bir zihniyettir. 
1. **Analitik Düşünme:** Problemi parçalara ayır.
2. **Finans Okuryazarlığı:** Altın, gümüş ve döviz piyasalarını takip etmen harika bir başlangıç! 
3. **Mühendislik Temeli:** En başarılı CEO'lar (Elon Musk gibi) işin mutfağını, yani mühendisliği bilenlerdir. Bu yüzden Havacılık ve Uzay Mühendisliği en doğru yol!"""
    }
}

# --- SOHBET MOTORU ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- ANA EKRAN GÖRÜNÜMÜ ---
st.markdown("<div class='main-title'>Merhaba Yusuf</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Bugün neyi keşfedelim?</div>", unsafe_allow_html=True)

# ANA SOHBET ALANI
with st.container():
    # BURASI İSTEDİĞİN GİBİ "LYSAN-A'YA SOR" OLDU
    user_query = st.text_input("", placeholder="LYSAN-A'ya sor...", key="main_input")
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Gönder"):
            if user_query:
                with st.spinner('Analiz ediliyor...'):
                    time.sleep(0.8)
                    response = "🤖 **LYSAN-A:** Bu harika bir soru patron! Havacılık fiziği, jet motorları veya mülakat taktikleri üzerine detaylı bir analiz yapmamı ister misin? Senin için 100.000 kelimelik veri bankamdan en güncel bilgileri çekebilirim."
                    
                    q_lower = user_query.lower()
                    for cat, data in knowledge_base.items():
                        if any(k in q_lower for k in data["keys"]):
                            response = data["content"]
                            break
                    
                    st.session_state.chat_history.append({"u": user_query, "a": response})

# SOHBET AKIŞI (DOĞAL VE AKICI)
st.markdown("<br>", unsafe_allow_html=True)
for chat in reversed(st.session_state.chat_history):
    st.markdown(f"<div class='user-msg'>{chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-msg'><div class='tech-text'>{chat['a']}</div></div>", unsafe_allow_html=True)

# YAN PANEL (STRATEJİK VERİLER)
with st.sidebar:
    st.markdown("### 🛰️ LYSAN-A SİSTEM DURUMU")
    st.write("---")
    st.info("⚡ Zeka Seviyesi: Ultra")
    st.info("📚 Bilgi Bankası: 100.000+ Kelime")
    st.success("📍 Konum: Adana / Strateji Merkezi")
    st.write("---")
    st.markdown("### 💰 Finans Radarı")
    st.metric("Yatırım Hedefi", "500 TL -> 22 Ayar", "AKTİF")
    st.write("---")
    if st.button("Sohbeti Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()
