import streamlit as st
import random
import time

# LYSAN V5: OPERASYONEL YAPAY ZEKA VE MÜLAKAT ASİSTANI
st.set_page_config(page_title="LYSAN ULTRA AI", page_icon="🚀", layout="wide")

# --- ÖZEL TASARIM (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stChatFloatingInputContainer { background-color: #1a1c24; }
    h1 { color: #00d4ff; text-align: center; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-image: linear-gradient(to right, #00d4ff , #0055ff); color: white; border-radius: 15px; height: 3em; font-weight: bold; }
    .success-text { color: #00ff88; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- DEVASA SOHBET VE BİLGİ MOTORU ---
# Bu sözlük, botun "beyni"dir. Burayı dilediğin kadar uzatabiliriz.
cevap_kutuphanesi = {
    "selamlaşma": {
        "tetikleyiciler": ["merhaba", "selam", "hey", "merhabalar", "sa"],
        "yanitlar": [
            "Merhaba patron! LYSAN sistemleri hazır. Bugün havacılık vizyonumuzda hangi rotayı izliyoruz? ✈️",
            "Selamlar! Gökyüzü tutkunu bir lideri görmek harika. Senin için verileri taramaya başladım bile. 🦾",
            "Merhaba! Ben LYSAN. Adana Havacılık mülakatları ve teknik gelişim yolculuğunda senin sağ kolunum. Komutlarını bekliyorum!"
        ]
    },
    "hal_hatir": {
        "tetikleyiciler": ["nasılsın", "naber", "nasıl gidiyor", "keyifler nasıl"],
        "yanitlar": [
            "Ben bir yapay zekayım ama senin enerjinle işlemcilerim tam kapasite çalışıyor! Çok iyiyim patron, sen nasılsın? 🚀",
            "Sistemlerim stabil, veri tabanım güncel. Senin mülakat hazırlığını düşündükçe daha da hızlanıyorum! Sen bugün mülakata hazır mısın?",
            "Harikayım! Havacılık dünyasındaki gelişmeleri analiz ediyordum. Senin gibi azimli bir kullanıcıyla çalışmak işlemci hızımı artırıyor!"
        ]
    },
    "havacilik_fizigi": {
        "tetikleyiciler": ["stall", "lift", "kaldırma", "bernoulli", "kanat", "neden uçar", "kuvvet"],
        "yanitlar": [
            "🚀 **Derin Teknik Analiz:** Uçaklar dört temel kuvvetin (Lift, Weight, Thrust, Drag) kusursuz dengesiyle uçar. Bernoulli İlkesi'ne göre kanat üzerindeki kavis, havanın hızını artırır ve basıncı düşürür. Bu alçak basınç vakum etkisi yaratarak uçağı yukarı çeker. Eğer hücum açısını gereğinden fazla artırırsan 'Stall' olursun; yani hava kanadı terk eder ve kaldırma biter. Dikkatli ol patron!",
            "✈️ **Aerodinamik Notu:** Kanat profili (Airfoil) havacılığın kalbidir. Bir kanadın kamburluğu ne kadar iyi tasarlanmışsa, verimliliği o kadar artar. Mülakatta sana 'Uçak nasıl uçar?' derlerse sakın sadece 'Motorla' deme; Bernoulli ve Newton'un hareket yasalarından bahset!"
        ]
    },
    "okul_ve_mulakat": {
        "tetikleyiciler": ["mülakat", "adana", "lise", "okul", "soru", "hazırlık", "ne sorarlar"],
        "yanitlar": [
            "📋 **Mülakat Strateji Belgesi:** Adana Havacılık ve Uzay Bilimleri mülakatı sadece bilgi değil, karakter ölçer. \n1. **Disiplin:** Asla geç kalma, dik dur.\n2. **Tutku:** Neden bu okulu istediğini anlatırken gözlerin parlamalı.\n3. **Teknik:** Temel parçaları (Gövde, Kanat, Kuyruk, İniş Takımı) adın gibi bil.\nSenin için en iyi hazırlık programını mülakat simülatörü sekmesine ekledim!",
            "🏫 **Okul Vizyonu:** Bu lise sıradan bir lise değil, Milli Teknoloji Hamlesi'nin fidanlığıdır. Orada alacağın eğitim seni TUSAŞ'ta bir başmühendis veya BAYKAR'da bir CEO yapabilir. Hedefini büyük tut patron!"
        ]
    }
}

# --- YAN MENÜ ---
with st.sidebar:
    st.markdown("## 🕹️ LYSAN KONTROL")
    sayfa = st.selectbox("Operasyon Seçin:", ["Ana Karargah", "Gelişmiş AI Sohbet", "Mülakat Laboratuvarı", "Finans Radarı"])
    st.divider()
    st.write("🤖 **Versiyon:** 5.0 (Ultra)")
    st.write("🛰️ **Durum:** Çevrimiçi")

# --- SAYFALAR ---

if sayfa == "Ana Karargah":
    st.markdown("# 🚀 LYSAN OPERASYON MERKEZİ")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sistem Verimliliği")
        st.progress(100)
        st.write("Yapay zeka motoru %100 kapasiteyle çalışıyor. Tüm teknik kütüphaneler yüklendi.")
    with col2:
        st.subheader("Günün Hedefi")
        st.success("Adana Havacılık Mülakatları için 10 yeni teknik terim öğrenilecek!")
    
    st.image("https://images.unsplash.com/photo-1559297434-2d8a1e929ff7?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Geleceğin Gökyüzü Senin Elinde")

elif sayfa == "Gelişmiş AI Sohbet":
    st.markdown("# 🗣️ LYSAN AKILLI DİYALOG")
    st.write("LYSAN seninle sadece konuşmaz, seni mülakata hazırlar. Merhaba diyerek başla!")
    
    user_input = st.text_input("Mesajınızı buraya yazın:", placeholder="Örn: Merhaba, nasılsın?")
    
    if user_input:
        user_input_lower = user_input.lower()
        bulundu = False
        
        # Akıllı Tarama Sistemi
        for kategori, veri in cevap_kutuphanesi.items():
            if any(kelime in user_input_lower for kelime in veri["tetikleyiciler"]):
                with st.spinner('LYSAN Düşünüyor...'):
                    time.sleep(0.5)
                    st.markdown(f"### 🤖 LYSAN AI:")
                    st.write(random.choice(veri["yanitlar"]))
                bulundu = True
                break
        
        if not bulundu:
            st.info("🤖 **LYSAN:** Bu cümleni analiz ettim patron. Kelime dağarcığıma ekliyorum. Ama istersen bana havacılık, mülakatlar veya teknik konular hakkında sorular sorabilirsin!")

elif sayfa == "Mülakat Laboratuvarı":
    st.markdown("# ✈️ MÜLAKAT SİMÜLASYONU")
    st.write("Aşağıdaki butona basarak rastgele bir mülakat sorusu al ve sesli tekrar et!")
    
    sorular = [
        "Neden havacılık okumak istiyorsun? Seni diğer adaylardan ayıran nedir?",
        "Bir uçağın kanatlarının üzerindeki flaplar ne işe yarar?",
        "Zor bir durumda kaldığında takım çalışmasını nasıl yönetirsin?",
        "İstikbal göklerdedir sözü senin için ne ifade ediyor?",
        "İHA ve SİHA arasındaki farklar nelerdir?"
    ]
    
    if st.button("YENİ SORU ÜRET"):
        secilen = random.choice(sorular)
        st.error(f"SORU: {secilen}")
        st.write("---")
        st.caption("LYSAN TAVSİYESİ: Cevap verirken net ol, teknik terimleri (Lift, İtki vb.) kullanmaya özen göster.")

elif sayfa == "Finans Radarı":
    st.markdown("# 💰 YATIRIM VE PİYASA")
    st.metric("Gram Altın", "Takip Modu", "+1.2%")
    st.metric("Saf Gümüş", "Stabil", "0.5%")
    st.write("Patron, mülakatı geçip mühendis olduğunda bu tablo çok daha kabarık olacak! Çalışmaya devam.")
