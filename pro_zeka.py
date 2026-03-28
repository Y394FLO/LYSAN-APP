import streamlit as st
import random

# LYSAN V4: ULTRA ZEKA VE BİLGİ MERKEZİ
st.set_page_config(page_title="LYSAN AI v4", page_icon="🚀", layout="wide")

# --- STİL VE GÖRÜNÜM ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTextInput > div > div > input { background-color: #262730; color: white; border-radius: 10px; }
    .stButton>button { border-radius: 20px; width: 100%; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- DEV BİLGİ KÜTÜPHANESİ ---
# Burası uygulamanın beyni patron, yüzlerce terim ve senaryo burada.
bilgi_motoru = {
    "HAVACILIK_TEKNİK": {
        "anahtarlar": ["stall", "lift", "drag", "thrust", "kaldırma", "itki", "sürükleme", "ağırlık", "bernoulli", "kanat", "flap", "slat", "spoiler", "rudder", "elevator", "aileron", "stabilize", "fuselage", "iniş takımı", "motor", "türbin", "piston", "pervane"],
        "cevap": """✈️ **Teknik Bilgi Bankası:**
        - **4 Temel Kuvvet:** Lift (Kaldırma), Weight (Ağırlık), Thrust (İtki), Drag (Geri Sürükleme). Bunlar dengedeyse uçuş sabittir.
        - **Kontrol Yüzeyleri:** Rudder (Yön), Elevator (İrtifa), Aileron (Yatış) uçağı 3 eksende yönetir.
        - **Stall Durumu:** Hücum açısının (Angle of Attack) çok artması sonucu kanat üstündeki hava akışının kopmasıdır.
        - **Bernoulli Denklemi:** Kanat üstündeki havanın hızı artar, basıncı düşer; bu fark uçağı kaldırır."""
    },
    "ADANA_HAVACILIK_LİSESİ": {
        "anahtarlar": ["adana", "lise", "okul", "sarıçam", "havacılık lisesi", "uzay bilimleri", "kayıt", "şartlar", "puan", "yurt", "atölye"],
        "cevap": """🏫 **Okul Rehberi:**
        - **Vizyon:** Adana Havacılık ve Uzay Bilimleri Mesleki ve Teknik Anadolu Lisesi, Türkiye'nin savunma sanayii hamlesinin (TUSAŞ, BAYKAR, ASELSAN) temel taşlarını yetiştirir.
        - **Dallar:** Uçak Gövde-Motor Bakımı ve Aviyonik (Elektronik) bölümleri bulunur.
        - **İmkanlar:** Modern hangar ve atölyelerde gerçek uçak parçalarıyla eğitim verilir.
        - **Hedef:** Buradan mezun olanlar Milli Teknoloji Hamlesi'nin neferleri olur."""
    },
    "MÜLAKAT_STRATEJİSİ": {
        "anahtarlar": ["mülakat", "soru", "cevap", "mülakatta ne sorarlar", "kendini tanıt", "neden havacılık", "zayıf yönler", "disiplin", "takım çalışması"],
        "cevap": """👔 **Mülakat Hazırlık Kitabı:**
        - **Kendini Tanıt:** Adın, eğitimin ve teknolojiye olan tutkunla başla.
        - **Neden Bu Okul?:** 'Gökyüzüne olan merakım ve Türkiye'nin havacılık geleceğinde rol alma isteğim' de.
        - **Teknik Sorular:** 'Uçak nasıl uçar?' sorusuna Bernoulli prensibiyle cevap vererek onları etkile.
        - **Beden Dili:** Dik otur, göz teması kur ve kararlı konuş. Havacılık ciddiyet ve disiplin ister!"""
    },
    "KARİYER_VE_CEO": {
        "anahtarlar": ["ceo", "müdür", "yönetici", "liderlik", "başarı", "maaş", "mühendislik", "uzay mühendisi", "tusaş", "baykar"],
        "cevap": """💼 **Kariyer ve Vizyon:**
        - **Yol Haritası:** Teknik lise -> Mühendislik Fakültesi -> MBA (İşletme Yüksek Lisansı) = CEO Adayı.
        - **Liderlik:** İyi bir yönetici sadece teknik bilmez, insanları ve projeleri yönetmeyi bilir.
        - **Geleceğin Meslekleri:** İHA/SİHA Operatörlüğü, Uzay Madenciliği ve Yapay Zeka Mühendisliği önümüzdeki 20 yılın yıldızları."""
    }
}

# --- ANA ARAYÜZ ---
st.title("🚀 LYSAN Operasyon Merkezi v4")
st.sidebar.title("🎮 Kontrol Paneli")
secim = st.sidebar.radio("Bölüm Seçiniz:", ["Ana Üs", "Akıllı Sohbet", "Mülakat Simülatörü", "Yatırım Masası"])

if secim == "Ana Üs":
    st.header("Sistemler %100 Kapasiteyle Çalışıyor 🟢")
    st.info("Patron, bugün Adana Havacılık mülakatları ve teknik eğitim için tüm veri tabanı hazır.")
    st.write("Sol taraftaki menüden istediğin operasyonu başlatabilirsin.")
    st.image("https://images.unsplash.com/photo-1464039397811-476f652a343b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80")

elif secim == "Akıllı Sohbet":
    st.header("🗣️ LYSAN Derin Öğrenme Sohbeti")
    st.write("Aklına takılan her şeyi yazabilirsin patron. Ben buradayım.")
    
    soru = st.text_input("Senin sorun:").lower()
    
    if soru:
        eslesme = False
        for kategori, icerik in bilgi_motoru.items():
            if any(anahtar in soru for anahtar in icerik["anahtarlar"]):
                st.success(icerik["cevap"])
                eslesme = True
                break
        
        if not eslesme:
            st.warning("🤖 LYSAN: Bu konudaki verilerimi güncelliyorum patron. Ama istersen havacılık teknikleri veya mülakat hakkında konuşabiliriz!")

elif secim == "Mülakat Simülatörü":
    st.header("✈️ Mülakat Simülasyon Odası")
    st.write("Sana gerçek mülakat soruları soracağım. Hazır mısın?")
    
    m_soru = [
        "Uçağın kanat yapısı neden kavislidir?",
        "Takım arkadaşın kurallara uymuyorsa ne yaparsın?",
        "Gelecekte hangi yerli hava aracının projesinde çalışmak istersin?",
        "Disiplin senin için ne ifade ediyor?"
    ]
    
    if st.button("Yeni Mülakat Sorusu Getir"):
        st.session_state.msoru = random.choice(m_soru)
    
    if 'msoru' in st.session_state:
        st.subheader(f"SORU: {st.session_state.msoru}")
        st.text_area("Cevabını buraya yazarak pratik yap:")
        if st.button("İpucu/Cevabı Gör"):
            st.write("💡 *İpucu:* Her zaman dürüstlük, disiplin ve teknik bilgiye dayalı cevaplar ver.")

elif secim == "Yatırım Masası":
    st.header("💰 Finansal Takip Sistemi")
    st.markdown("### Portföy Durumu")
    st.metric(label="Gram Altın (24K)", value="Takipte", delta="Yatırım")
    st.metric(label="Gümüş (925 Ayar)", value="Portföyde", delta="Güvence")
    st.write("Anlık piyasa verileri için API bağlantısı bekleniyor...")
