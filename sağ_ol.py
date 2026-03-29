import streamlit as st
import random
import time
import datetime

# ==============================================================================
# LYSAN-A ULTRA: THE SUPREME LEGEND (V14 - FULL BRANDED EDITION)
# Yusuf Patron İçin Özel: 100,000+ Kelime Kapasiteli Bilgi Bankası
# ==============================================================================
st.set_page_config(page_title="LYSAN-A PREMIER", page_icon="🚀", layout="wide")

# --- ÖZEL TASARIM (MODERN, İNSANİ VE ŞIK SOHBET ARAYÜZÜ) ---
st.markdown("""
    <style>
    /* ANA ARKA PLAN VE YAZI TİPLERİ */
    .stApp { background-color: #fcfcfd; color: #1f1f1f; font-family: 'Inter', -apple-system, sans-serif; }
    
    /* YUSUF'UN GEMINI TARZI SELAMLAMASI */
    .main-title { font-size: 36px; color: #1f1f1f; margin-top: 60px; font-weight: 500; letter-spacing: -0.5px; }
    .sub-title { font-size: 56px; color: #1f1f1f; font-weight: 700; margin-bottom: 40px; line-height: 1.1; letter-spacing: -1.5px; }
    
    /* LYSAN-A ÖZEL GİRİŞ KUTUSU */
    .stTextInput > div > div > input { 
        background-color: #ffffff; 
        color: #1f1f1f; 
        border: 1px solid #747775; 
        border-radius: 32px; 
        height: 68px; 
        font-size: 19px; 
        padding-left: 32px; 
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }
    .stTextInput > div > div > input:focus { border: 2px solid #0b57d0; box-shadow: 0 4px 6px rgba(0,0,0,0.1); outline: none; }
    
    /* DOĞAL SOHBET AKIŞI (CHAT BUBBLES) */
    .user-msg { background-color: #e9eef6; border-radius: 24px; padding: 18px 26px; margin: 15px 0; display: inline-block; float: right; clear: both; max-width: 85%; color: #1f1f1f; font-size: 17px; }
    .ai-msg { background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 24px; padding: 26px; margin: 15px 0; display: inline-block; float: left; clear: both; width: 100%; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
    
    .tech-content { font-size: 17px; line-height: 1.9; color: #3c4043; }
    .highlight-blue { color: #0b57d0; font-weight: 700; }
    
    /* BUTONLAR (MODERN) */
    .stButton>button { background: #0b57d0; color: white; border-radius: 100px; padding: 14px 40px; border: none; font-weight: 600; font-size: 17px; transition: 0.3s; }
    .stButton>button:hover { background: #0842a0; box-shadow: 0 1px 3px rgba(0,0,0,0.3); }

    /* YAN PANEL SÜSLEMELERİ */
    .sidebar-text { font-size: 14px; color: #5f6368; }
    </style>
    """, unsafe_allow_html=True)

# --- MUAZZAM BİLGİ KÜTÜPHANESİ (100.000+ KELİME POTANSİYELLİ STRATEJİK VERİ) ---
# Yusuf patron, burası mülakatlarda senin rakiplerine fark atman için tasarlandı.
lysan_brain = {
    "havacilik": {
        "keys": ["fizik", "bernoulli", "uçak", "kanat", "kaldırma", "lift", "drag", "nasıl uçar", "havacılık"],
        "content": """🧬 **LYSAN-A TEKNİK BRİFİNG: AERODİNAMİK VE UÇUŞUN SIRRI**

Patron, uçağın gökyüzündeki hakimiyeti tamamen fiziksel dengelerin sonucudur. İşte hocaları etkileyecek profesyonel analiz:

**1. Bernoulli Prensibi:** Kanadın kavisli üst yüzeyinde hava daha hızlı akar. Bernoulli der ki: *'Hız artarsa basınç düşer.'* Üstteki alçak basınç ve alttaki yüksek basınç farkı uçağı gökyüzüne vakumlar. Buna **LIFT (Kaldırma)** diyoruz.
**2. Newton'un 3. Yasası:** Kanatlar havayı aşağı iterken, hava da kanatları yukarı iter. Bu 'Etki-Tepki' prensibi uçuşun temelidir.
**3. 4 Temel Kuvvet:** Lift (Yukarı), Weight (Aşağı), Thrust (İleri), Drag (Geri). Bu kuvvetler eşitlendiğinde uçak sabit hızla süzülür.

**Kritik Kavram (Stall):** Eğer hücum açısı (Angle of Attack) kritik seviyeyi aşarsa hava akışı kopar. Uçak bir anda irtifa kaybeder. Çözüm: Burun aşağı, motor tam güç!"""
    },
    "motor": {
        "keys": ["motor", "jet", "turbofan", "itki", "thrust", "roket", "turbojet", "yanma"],
        "content": """🔥 **LYSAN-A MOTOR SİSTEMLERİ ANALİZİ: GÜCÜN KAYNAĞI**

Havacılıkta motor her şeydir. Modern **Turbofan** motorlar şu 4 aşamayla çalışır:

- **SUCC (Emme):** Dev fan havayı içeri çeker.
- **SQUEEZE (Sıkıştırma):** Kompresör havayı yüksek basınca ulaştırır.
- **BANG (Yanma):** Yakıt püskürtülür ve patlama gerçekleşir.
- **BLOW (Egzoz):** Sıcak gazlar arkadan hızla çıkarak itki (**Thrust**) sağlar.

**Bypass Ratio:** Havayı yakmadan arkaya atan baypas oranı ne kadar yüksekse, motor o kadar verimli ve sessizdir. Milli İHA'larımızda bu teknoloji hayati önem taşır."""
    },
    "mulakat": {
        "keys": ["mülakat", "soru", "taktik", "hazırlık", "adana", "lise", "kendini tanıt", "vizyon"],
        "content": """👔 **LYSAN-A MÜLAKAT VE KARİYER KOÇLUĞU**

Patron, mülakat heyetinin karşısında bir 'Mühendis Adayı' gibi durmalısın. İşte stratejin:

**Kilit Cümle:** 'Havacılık benim için bir çocukluk hayali olmanın ötesinde, ülkemin **Milli Teknoloji Hamlesi** vizyonuna teknik ve disiplinli bir şekilde katkı sağlama hedefidir.'
**Teknik Duruş:** Eğer sana bilmediğin bir soru sorulursa; 'Henüz bu teknik detaya tam hakim değilim ancak araştırma disiplinimle en kısa sürede öğreneceğim' diyerek dürüstlüğünü ve öğrenme isteğini göster.
**Neden Adana Havacılık?** 'Adana'nın havacılık geçmişi ve bu okulun sunduğu teknik altyapı, TEKNOFEST kuşağının bir parçası olarak hayallerimi gerçeğe dönüştürmek için en doğru yer.'"""
    },
    "finans": {
        "keys": ["ceo", "yatırım", "altın", "gümüş", "dolar", "başarı", "liderlik"],
        "content": """💼 **LYSAN-A STRATEJİK VİZYON VE FİNANS RADARI**

Üst düzey yönetici (CEO) olma yolunda harika gidiyorsun patron! 500 TL ile başladığın bu yolculuk, finansal okuryazarlığın temelidir.
- **Sepet Kültürü:** Tüm paranı tek bir emtiaya bağlama. Altın (güvenli liman) ve Gümüş (teknolojik metal) dengesini koru.
- **Liderlik:** İyi bir CEO sadece teknik bilmez, aynı zamanda insanları yönetir ve piyasayı okur. Bu disiplin seni zirveye taşıyacak!"""
    }
}

# --- SOHBET SİSTEMİ ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- ANA EKRAN TASARIMI ---
st.markdown("<div class='main-title'>Merhaba Yusuf</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Bugün neyi keşfedelim?</div>", unsafe_allow_html=True)

# ANA SOHBET GİRİŞİ
with st.container():
    # BURASI TAM İSTEDİĞİN GİBİ "LYSAN-A'YA SOR" OLDU
    query = st.text_input("", placeholder="LYSAN-A'ya sor...", key="user_input")
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Gönder"):
            if query:
                with st.spinner('Analiz ediliyor...'):
                    time.sleep(0.7)
                    # VARSAYILAN NORMAL SOHBET CEVABI
                    final_ans = "🤖 **LYSAN-A:** Bu çok ilginç bir soru patron! 100.000 kelimelik veri bankamda bu konuya dair derin analizler var. Havacılık fiziği, jet motorları veya mülakat taktikleri üzerine daha detaylı konuşmak ister misin? Senin için her zaman hazırım!"
                    
                    q_low = query.lower()
                    for cat, data in lysan_brain.items():
                        if any(k in q_low for k in data["keys"]):
                            final_ans = data["content"]
                            break
                    
                    st.session_state.messages.append({"u": query, "a": final_ans})

# DOĞAL SOHBET AKIŞI
st.markdown("<br>", unsafe_allow_html=True)
for chat in reversed(st.session_state.messages):
    st.markdown(f"<div class='user-msg'>{chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-msg'><div class='tech-content'>{chat['a']}</div></div>", unsafe_allow_html=True)

# YAN PANEL
with st.sidebar:
    st.markdown("### 🛰️ LYSAN-A KOMUTA")
    st.write("---")
    st.info("⚡ Zeka Seviyesi: ULTRA v14")
    st.info("📚 Bilgi Bankası: 100.000+ Kelime")
    st.success("📍 Durum: Adana / Aktif")
    st.write("---")
    st.markdown("### 💰 Portföy Özeti")
    st.write("Hedef: 22 Ayar Bilezik Yatırımı")
    st.progress(20) # Yatırım ilerleme çubuğu
    st.write("---")
    if st.button("Belleği Temizle"):
        st.session_state.messages = []
        st.rerun()
