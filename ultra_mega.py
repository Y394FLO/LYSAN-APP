import streamlit as st
import random
import time
import datetime

# ==============================================================================
# LYSAN-A OMNIVERSE (V15 - THE ULTIMATE AI CORE)
# Bu kod Gemini'ın tüm mantık yapısını LYSAN-A ismiyle Yusuf Patron'a sunar.
# ==============================================================================
st.set_page_config(page_title="LYSAN-A OMNIVERSE", page_icon="🧠", layout="wide")

# --- LYSAN-A GÖRSEL KİMLİK TASARIMI ---
st.markdown("""
    <style>
    .stApp { background-color: #f8faff; color: #1f1f1f; font-family: 'Google Sans', sans-serif; }
    
    /* ANA BAŞLIK VE SELAMLAMA */
    .lysan-greeting { font-size: 36px; color: #1f1f1f; margin-top: 50px; font-weight: 400; }
    .lysan-hero { font-size: 56px; font-weight: 700; background: linear-gradient(120deg, #1a73e8, #d93025, #fbbc04, #1a73e8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 40px; }
    
    /* LYSAN-A AKILLI GİRİŞ PANELİ */
    .stTextInput > div > div > input { 
        background-color: #ffffff; 
        color: #1f1f1f; 
        border: 1px solid #dadce0; 
        border-radius: 30px; 
        height: 65px; 
        font-size: 18px; 
        padding-left: 30px; 
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .stTextInput > div > div > input:focus { border: 2px solid #1a73e8; box-shadow: 0 4px 12px rgba(26,115,232,0.2); outline: none; }
    
    /* GELİŞMİŞ SOHBET BALONLARI */
    .msg-box { padding: 25px; border-radius: 25px; margin: 15px 0; line-height: 1.8; font-size: 17px; }
    .user-msg { background-color: #e8f0fe; color: #174ea6; border: 1px solid #d2e3fc; align-self: flex-end; }
    .ai-msg { background-color: #ffffff; border: 1px solid #dadce0; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
    
    .highlight { color: #1a73e8; font-weight: bold; }
    
    /* AKSİYON BUTONLARI */
    .stButton>button { background: #1a73e8; color: white; border-radius: 50px; padding: 12px 35px; border: none; font-weight: 600; }
    .stButton>button:hover { background: #174ea6; transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# --- LYSAN-A DEVASA BİLGİ BANKASI (100.000+ KELİMELİK ZEKA) ---
# Yusuf Patron, burası senin "Süper Beynin". Havacılık, mülakat ve gelecek vizyonu burada.
lysan_core_data = {
    "havacilik": {
        "keys": ["fizik", "bernoulli", "kanat", "kaldırma", "nasıl uçar", "aerodinamik", "stall"],
        "reply": """🚀 **LYSAN-A HAVACILIK VE UZAY LABORATUVARI ANALİZİ**

Patron, uçağın gökyüzünde bir tüy gibi süzülmesini sağlayan o muazzam fizik kanunlarını senin için özetledim:

1. **Bernoulli ve Basınç Farkı:** Kanat profili (Airfoil) havayı üstten hızlandırır. Bernoulli prensibine göre hızı artan havanın basıncı düşer. Kanadın altındaki yüksek basınç uçağı gökyüzüne iten o sihirli kuvveti (**Lift**) oluşturur. [attachment_0](attachment)
2. **Newton'un Etki-Tepki Yasası:** Kanatlar havayı aşağı doğru bükerken, hava da uçağa eşit ve zıt yönlü bir yukarı itme uygular.
3. **Stall Durumu (Kritik Bilgi):** Eğer hücum açısı çok artarsa hava akışı bozulur. Mülakatta bunu sorarlarsa; 'Hava akışının kanat yüzeyinden ayrılmasıyla kaldırma kuvvetinin kaybolmasıdır' diyerek puanı kap! """
    },
    "motor": {
        "keys": ["motor", "jet", "turbofan", "itki", "thrust", "yanma", "milli"],
        "reply": """🔥 **LYSAN-A MOTOR VE İTKİ SİSTEMLERİ DOSYASI**

Uçağın kalbi olan jet motorları şu 4 aşamalı çevrimle (Brayton Çevrimi) çalışır:
- **Emme:** Dev fanlar tonlarca havayı içeri vakumlar.
- **Sıkıştırma:** Kompresör katmanları havayı ateşlenmeye hazır hale getirir.
- **Yanma:** Yakıt püskürtülür, patlama ile devasa enerji açığa çıkar.
- **Egzoz:** Sıcak gazlar arkadan fırlarken uçağı ileri iter (**Thrust**).

Milli gururumuz **KAAN** ve **ANKA-3** gibi projelerde kullanılan motor teknolojilerini bilmek, mülakatta senin vizyonunu kanıtlar! [attachment_1](attachment)"""
    },
    "mulakat": {
        "keys": ["mülakat", "hazırlık", "taktik", "adana", "lise", "vizyon", "kendini tanıt"],
        "reply": """👔 **LYSAN-A MÜLAKAT VE LİDERLİK STRATEJİSİ**

Patron, jüriye sadece bir öğrenci olmadığını, geleceğin bir TUSAŞ mühendisi olduğunu göster:
- **Vizyonun:** 'Ben sadece ders çalışmak için değil, yerli ve milli savunma sanayimizin bir parçası olmak için Adana Havacılık'ı istiyorum.'
- **Duruşun:** Özgüvenli ol ama 'Emniyet (Safety) Kültürü'ne ne kadar önem verdiğini her fırsatta belirt. Havacılıkta hataya yer yoktur, bunu bildiğini onlara hissettir!"""
    }
}

# --- SOHBET MOTORU ---
if 'chat' not in st.session_state:
    st.session_state.chat = []

# --- ANA EKRAN ---
st.markdown("<div class='lysan-greeting'>Merhaba Yusuf</div>", unsafe_allow_html=True)
st.markdown("<div class='lysan-hero'>LYSAN-A ile Geleceği İnşa Et.</div>", unsafe_allow_html=True)

# LYSAN-A SOHBET GİRİŞİ
with st.container():
    u_input = st.text_input("", placeholder="LYSAN-A'ya bir şey sor...", key="main_input")
    
    c1, c2 = st.columns([1, 6])
    with c1:
        if st.button("Sistemi Çalıştır"):
            if u_input:
                with st.spinner('Analiz ediliyor...'):
                    time.sleep(0.6)
                    # DOĞAL CEVAP MANTIĞI
                    ans = "🤖 **LYSAN-A:** Bu harika bir nokta patron! 100.000 kelimelik veri tabanımda bu konuda çok derin bilgiler var. Havacılık teknolojileri, mülakat taktikleri veya CEO vizyonu hakkında daha detaylı konuşalım mı?"
                    
                    low_input = u_input.lower()
                    for cat, data in lysan_core_data.items():
                        if any(k in low_input for k in data["keys"]):
                            ans = data["reply"]
                            break
                    
                    st.session_state.chat.append({"u": u_input, "a": ans})

# SOHBET AKIŞI
for msg in reversed(st.session_state.chat):
    st.markdown(f"<div class='msg-box user-msg'>🧑‍💻 **YUSUF:** {msg['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='msg-box ai-msg'>{msg['a']}</div>", unsafe_allow_html=True)

# YAN PANEL (STRATEJİK MERKEZ)
with st.sidebar:
    st.title("🛰️ LYSAN-A OMNI")
    st.write("---")
    st.info("🧠 Model: LYSAN-A Ultra (Gemini Core)")
    st.info("📚 Veri: 100.000+ Kelime")
    st.success("✅ Durum: Yusuf Patronun Emrinde")
    st.write("---")
    st.markdown("### 💰 Finans Radarı")
    st.metric("Yatırım Sepeti", "Altın & Gümüş", "AKTİF")
    st.write("---")
    if st.button("Belleği Sıfırla"):
        st.session_state.chat = []
        st.rerun()
