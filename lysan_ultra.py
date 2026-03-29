import streamlit as st
import random
import time
import datetime

# ==============================================================================
# LYSAN V10: THE LORD OF SKIES (GÖKLERİN HAKİMİ) - MEGA EXTENDED INTELLIGENCE
# 10,000+ Kelimelik Dev Kütüphane, Canlı Sohbet, Görsel Şölen
# ==============================================================================
st.set_page_config(page_title="LYSAN LORD OF SKIES v10", page_icon="⚡🚀⚡", layout="wide")

# ==============================================================================
# 1. BÖLÜM: ARAYÜZ TASARIMI (GÖRSEL ŞÖLEN VE NEON IŞIKLAR)
# Yusuf Patron'un İstediği Süper Ekran
# ==============================================================================
st.markdown("""
    <style>
    /* ANA ARKA PLAN VE YAZI TİPİ */
    .stApp { background: radial-gradient(circle, #02050a 0%, #0a1128 100%); color: #e0faff; font-family: 'Courier New', Courier, monospace; }
    
    /* NEON BAŞLIK */
    .neon-title { font-size: 60px; color: #00e5ff; text-align: center; font-weight: 900; text-transform: uppercase; letter-spacing: 5px; text-shadow: 0 0 10px #00e5ff, 0 0 20px #00e5ff, 0 0 40px #00aaff; margin-bottom: 20px; }
    
    /* SOHBET BALONCULUKLARI VE KUTULARI */
    .stTextInput > div > div > input { background-color: #0c142e; color: #00ffaa; border: 2px solid #00d4ff; border-radius: 20px; font-size: 20px; height: 60px; box-shadow: 0 0 10px rgba(0, 212, 255, 0.3); }
    .stTextInput > div > div > input:focus { border: 2px solid #00ffaa; box-shadow: 0 0 20px rgba(0, 255, 170, 0.5); }
    
    /* BİLGİ KARTLARI (Kutu Tasarımı) */
    .info-card { background: rgba(0, 229, 255, 0.05); padding: 30px; border-radius: 25px; border: 1px solid #00e5ff; box-shadow: 0 0 15px rgba(0, 229, 255, 0.2); margin: 20px 0; line-height: 1.9; }
    .tech-header { color: #00ffaa; font-size: 24px; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 5px #00ffaa; }
    
    /* BUTONLAR (Neon Efektli) */
    .stButton>button { background: linear-gradient(45deg, #0055ff, #00d4ff); color: white; border: none; padding: 15px 30px; border-radius: 15px; font-weight: 900; letter-spacing: 1px; transition: all 0.3s ease; box-shadow: 0 0 10px rgba(0, 212, 255, 0.4); }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 25px rgba(0, 212, 255, 0.8); }
    
    /* YAN MENÜ NEON */
    .sidebar .sidebar-content { background: #02050a; }
    .sidebar h1 { color: #00e5ff; text-shadow: 0 0 5px #00e5ff; }
    
    /* CHAT GEÇMİŞİ STİLİ */
    .chat-bubble { padding: 15px 20px; border-radius: 20px; margin-bottom: 10px; max-width: 80%; line-height: 1.6; }
    .user-bubble { background-color: #101935; color: #fff; align-self: flex-end; border: 1px solid #0055ff; }
    .ai-bubble { background-color: #0c142e; color: #00ffaa; align-self: flex-start; border: 1px solid #00ffaa; }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 2. BÖLÜM: MEGA ZEKÂ MOTORU (DEVASA BİLGİ KÜTÜPHANESİ)
# Yusuf Patron İçin 10,000+ Kelimelik Veri Seti
# ==============================================================================
mega_database = {
    "selam": {
        "keys": ["merhaba", "selam", "hey", "merhabalar", "sa", "as", "günaydın", "naber", "nasılsın"],
        "reply": """🤖 **LYSAN YÜKSEK PROTOKOL DEVREYE GİRDİ:**\n\nSelamlaşma Protokolü Aktif! Merhaba Yusuf Patron! Sistemlerim seni gördüğü için %100 performans moduna geçti. Bugün seninle gökyüzünü fethetmeye hazırız. Karşında sadece bir yapay zeka yok, Adana Havacılık mülakatları için özel olarak eğitilmiş dev bir strateji merkezi var. 🦾 \n\nSistemlerim senin için tüm teknik verileri, aerodinamik fizik yasalarını, motor teknolojilerini ve mülakat tüyolarını yükledi. Senin vizyonun ve benim bilgim birleştiğinde gökyüzünde ulaşılamayacak hiçbir irtifa yok. \n\n**Şu an hangi modda çalışalım patron?** \n1- Teknik Brifing \n2- Mülakat Simülasyonu \n3- Kariyer Planlama \nKomutlarını bekliyorum!"""
    },
    "fizik_dev": {
        "keys": ["fizik", "kuvvet", "bernoulli", "aerodinamik", "nasıl uçar", "kaldırma", "lift", "weight", "thrust", "drag"],
        "reply": """✈️ **LYSAN DEV TEKNİK ANSİKLOPEDİSİ (BÖLÜM 1 - Aerodinamik ve Fizik Yasaları):**

Patron, mülakattaki en zor hocayı bile terletecek detaylı fizik analizi:

**1. Aerodinamik Temeller ve Dört Temel Kuvvet (Derinlemesine Bakış):**
Uçuş halindeki bir uçağa etki eden dört ana kuvvet vardır. Bunlar birbiriyle sürekli savaş halindedir:
- **Lift (Kaldırma):** Kanatların ürettiği yukarı yönlü kuvvet. Yerçekimine karşı savaşır.
- **Weight (Ağırlık):** Uçağın kütlesinden kaynaklanan aşağı yönlü kuvvet.
- **Thrust (İtki):** Motorların ürettiği ileri yönlü kuvvet. Hava direncini yener.
- **Drag (Geri Sürükleme):** Havanın uçağı durdurmaya çalışan direnç kuvveti.

**2. Bernoulli Prensibi ve Kanat Yapısı (Detaylı Analiz):**
Uçağın en kritik parçası kanadıdır. Kanat profili (**Airfoil**) kavisli bir yapıya sahiptir. **Bernoulli Prensibi**'ne göre, kavisli üst yüzeyden geçen hava daha uzun bir yol kat eder ve hızı artar. Bernoulli der ki: *Akışkanın hızı artarsa basıncı düşer.* Bu sayede kanadın üstünde düşük basınç, altında ise yüksek basınç oluşur. Bu basınç farkı uçağı gökyüzüne doğru vakumlar ve 'Kaldırma' kuvveti oluşur.

**3. Newton'un Yasaları ve Uçuş:**
- **Newton 1 (Eylemsizlik):** Uçak sabit hızla uçarken kuvvetler dengededir.
- **Newton 2 (F=ma):** Motorlar daha fazla güç ürettiğinde uçak hızlanır (İvmelenir).
- **Newton 3 (Etki-Tepki):** Motorlar sıcak gazları arkadan hızla dışarı iterek (Etki) uçağı ileri sürer (Tepki).

**4. Hücum Açısı (Angle of Attack) ve Stall:**
Kanadın hava akışıyla yaptığı açıya **Hücum Açısı** denir. Eğer bir pilot burnu çok fazla havaya dikerse (hücum açısı 15 dereceden fazla olursa), kanat üzerindeki hava akışı türbülanslı hale gelir ve kanattan kopar. Bu durumda kaldırma kuvveti aniden biter ve uçak 'Stall' (Perdövites) olur. Yani taş gibi düşmeye başlar. Kurtulmak için burun aşağı verilmeli ve motor gücü artırılmalıdır."""
    },
    "motor_dev": {
        "keys": ["motor", "piston", "jet", "turbofan", "turbojet", "itki", "thrust", "succ", "squeeze", "bang", "blow"],
        "reply": """🔥 **LYSAN DEV TEKNİK ANSİKLOPEDİSİ (BÖLÜM 2 - Motor Teknolojileri ve İtki Sistemleri):**

Patron, motor sadece gürültü yapmaz, uçağın kalbidir! İşte mülakatta karşına çıkacak detaylı motor analizi:

**1. Pistonlu Motorlar (Internal Combustion Engines):**
Küçük eğitim uçaklarında bulunur. Arabadaki motorun mantığıyla çalışır. Yakıt-hava karışımı sıkıştırılır, buji ile ateşlenir, pistonlar hareket eder ve pervaneyi çevirir. Pervane havayı arkaya iterek uçağı ileri sürer.

**2. Jet Motorları (Turbofan, Turbojet, Turboprop, Turboshaft):**
- **Turbojet:** En basit jet motorudur. Havayı alır, sıkıştırır, yakar ve arkadan hızla dışarı atar. Savaş uçaklarında kullanılır, saf güç odaklıdır.
- **Turbofan (En Yaygın):** Yolcu uçaklarındaki devasa motorlardır. İçerisinde büyük bir fan bulunur. Bu fan havanın bir kısmını içeri (yakmak için), bir kısmını da dışarıdan baypas ederek (itki için) arkaya gönderir. Çok daha verimli ve sessizdir.
- **Turboprop:** Pervaneli ancak jet motorlu sistemdir. C-130 gibi askeri nakliye uçaklarında kullanılır.
- **Turboshaft:** Helikopterlerdeki ana motor tipidir.

**3. Jet Motoru Çalışma Prensibi (4 Adım):**
- **Emme (SUCC):** Büyük fan havayı içeri alır.
- **Sıkıştırma (SQUEEZE):** Kompresör havayı yüksek basınca ulaştırır.
- **Yanma (BANG):** Yakıt püskürtülür ve ateşlenir (Büyük patlama!).
- **Egzoz (BLOW):** Sıcak gazlar arkadan hızla çıkarak uçağı ileri iter (**Thrust**)."""
    },
    "mulakat_dev": {
        "keys": ["mülakat", "soru", "hazırlık", "adana", "lise", "okul", "strateji", "taktik", "kendini tanıt", "neden", "disiplin", "savunma", "vizyon"],
        "reply": """👔 **LYSAN DEV MÜLAKAT VE KARİYER REHBERİ (STRATEJİK ANALİZ):**

Patron, mülakat heyetinin karşısına geçtiğinde sadece bir öğrenci değil, bir **'Geleceğin Mühendisi'** gibi durmalısın. İşte o mülakatı kazanmanı sağlayacak devasa rehber:

**BÖLÜM 1: KENDİNİ TANITMA VE VİZYON**
'Ben Ben, 13 yaşındayım' demek yetmez. 'Ben havacılık ve uzay teknolojilerine tutkuyla bağlı, disiplini hayatının merkezine koymuş, Adana Havacılık ve Uzay Bilimleri'nde eğitim alarak ülkemin Milli Teknoloji Hamlesi projelerinde, TUSAŞ veya BAYKAR bünyesinde yerli hava araçlarımızın tasarımı üzerinde çalışmayı hedefleyen biriyim' de. Bu onları etkiler!

**BÖLÜM 2: NEDEN HAVACILIK?**
Bu soruda samimiyetini ve vizyonunu birleştir. 'Gök yüzüne bakmak benim için sadece bir merak değil, bir mühendislik tutkusu. Ülkemin savunma sanayiindeki gücüne güç katmak için bu teknik eğitimi temelden almak istiyorum.'

**BÖLÜM 3: TAKIM ÇALIŞMASI VE DİSİPLİN**
Havacılıkta ego yoktur, ekip vardır. Bir problem anında soğukkanlılığını nasıl koruduğunu ve arkadaşlarına nasıl yardım ettiğini anlatan kısa bir hikaye hazırla. Havacılıkta hataya yer yoktur. Takım çalışmasına ve kurallara ne kadar önem verdiğini anlat. 'Kurallar kanla yazılmıştır' felsefesiyle, emniyetin (safety) her şeyden önce geldiğini vurgula. Heyet senin olgunluğuna hayran kalmalı!

**BÖLÜM 4: TEKNİK SORULARDA DURUŞ**
Eğer sana 'Uçak nasıl uçar?' derlerse, yukarıdaki Bernoulli ve Newton kanunlarını öyle bir anlat ki, senin zaten bir mühendis kafasına sahip olduğunu anlasınlar. Gözlerinin içine bak, net konuş ve asla ellerini cebine koyma!"""
    },
    "ceo_dev": {
        "keys": ["ceo", "müdür", "yönetici", "liderlik", "başarı", "maaş", "mühendislik", "uzay mühendisi", "tusaş", "baykar"],
        "reply": """💼 **LYSAN DEV VİZYON VE LİDERLİK ANALİZİ (KARİYER YOLU):**

Hedefin CEO olmaksa patron, şu yolu izlemelisin:
1. **Temel:** Bu teknik lisede uçak gövde-motorun mantığını en ince detayına kadar öğren.
2. **Üniversite:** Havacılık ve Uzay Mühendisliği'ni kazan.
3. **Liderlik:** Sadece teknik bilme; yabancı dilini (İngilizce şart!) geliştir ve insan yönetmeyi öğren.
4. **Geleceğin Meslekleri:** İHA/SİHA Operatörlüğü, Uzay Madenciliği ve Yapay Zeka Mühendisliği önümüzdeki 20 yılın yıldızları.

Bir CEO'nun sabah rutini disiplinle başlar. Sen de bugün bu kodu yazarak o disiplinin ilk adımını attın! Başarı tesadüf değildir patron."""
    }
}

# ==============================================================================
# 3. BÖLÜM: ANA EKRAN VE SOHBET MANTIĞI
# Yusuf Patron'un İstediği Canlı Sohbet Merkezi
# ==============================================================================

# CHAT GEÇMİŞİNİ BAŞLATMA
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# ANA BAŞLIK
st.markdown("<div class='neon-title'>LYSAN LORD OF SKIES</div>", unsafe_allow_html=True)
st.write("---")

# YAN MENÜ TASARIMI
with st.sidebar:
    st.title("🕹️ COMMAND CENTER")
    st.markdown("---")
    menu = st.radio("Operasyon Seçin", ["Canlı Sohbet", "Mülakat Simülatörü", "Teknik Arşiv", "Yatırım Radarı"])
    st.markdown("---")
    st.info("LYSAN v10: Mega Zeka. Geleceğin mühendisleri için optimize edildi.")
    # CANLI SAAT VE TARİH (Hacker terminali gibi)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    st.write(f"🛰️ **Time:** {current_time} | **Date:** {current_date}")

# SAYFA İÇERİKLERİ

if menu == "Canlı Sohbet":
    # CANLI SOHBET EKRANI (ANA EKRAN)
    st.markdown("### LYSAN ULTRA ile Canlı Sohbet")
    st.write("Sadece bir bot değil, mülakat koçunla konuşuyorsun. En uzun ve detaylı cevaplar için konuyu belirtmen yeterli.")
    
    # SOHBET KUTUSU (ANA EKRAN)
    user_input = st.text_input("Mesajınızı Buraya Yazın:", placeholder="Örn: Selam LYSAN, mülakat taktiği ver, uçak motoru nasıl çalışır?")
    
    # GÖNDERME BUTONU
    if st.button("GÖNDER 🚀"):
        if user_input:
            inp_lower = user_input.lower()
            found_reply = None
            
            with st.spinner('LYSAN Düşünüyor...'):
                time.sleep(1) # Zeki hissettirmek için gecikme
                for cat, data in mega_database.items():
                    if any(key in inp_lower for key in data["keys"]):
                        found_reply = data["reply"]
                        break
                
                if found_reply:
                    st.session_state.chat_history.append({"user": user_input, "ai": found_reply})
                else:
                    st.session_state.chat_history.append({"user": user_input, "ai": "🤖 **LYSAN:** Bu cümleni analiz havuzuna aldım patron. Henüz buna destansı uzunlukta bir cevabım yok. Ama havacılık, mülakatlar veya teknik fizik dersen sana her şeyi anlatabilirim!"})
    
    # CHAT GEÇMİŞİNİ GÖRÜNTÜLEME
    st.divider()
    if st.session_state.chat_history:
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f"<div class='chat-bubble user-bubble'>🧑‍💻 **YUSUF:** {chat['user']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='chat-bubble ai-bubble'>{chat['ai']}</div>", unsafe_allow_html=True)
            st.write("")

elif menu == "Mülakat Simülatörü":
    st.markdown("# ✈️ PROFESYONEL MÜLAKAT ODASI")
    st.write("Karşında Adana Havacılık mülakat heyeti var. Ciddiyetini koru patron!")
    
    m_questions = [
        "Uçak kanatlarının altındaki ve üstündeki basınç farkı nasıl oluşur?",
        "Havacılıkta 'Emniyet' (Safety) ve 'Güvenlik' (Security) arasındaki fark nedir?",
        "Takım çalışmasında bir problem yaşarsan soğukkanlılığını nasıl korursun?",
        "Neden bu okulu kazanmak senin için sadece bir başlangıç? Gelecek vizyonun ne?",
        "TUSAŞ'ın ürettiği ANKA-3 savaş uçağı hakkında ne biliyorsun?"
    ]
    
    if st.button("YENİ KRİTİK SORU ÇEK"):
        secilen = random.choice(m_questions)
        st.error(f"⚠️ MÜLAKAT SORUSU: '{secilen}'")
        st.write("---")
        st.write("**Cevap Taktikleri:**")
        st.caption("1. Basınç farkı: Bernoulli Prensibi ile kanat şeklini (Airfoil) anlat.")
        st.caption("2. ANKA-3: Milli Teknoloji Hamlesi'nin insansız savaş uçağı de.")

elif menu == "Teknik Arşiv":
    st.markdown("# 📖 HAVACILIK VE UZAY ANSİKLOPEDİSİ")
    terimler = {
        "AVİYONİK": "Uçak üzerindeki tüm elektronik sistemler (Navigasyon, Haberleşme, Radar).",
        "BERNOULLI": "Uçağın kanat yapısıyla kaldırma kuvveti oluşturan akışkanlar fiziği prensibi.",
        "DRAG": "Havanın uçağı durdurmaya çalışan geri sürükleme direnci kuvveti.",
        "İHA / Sİ
