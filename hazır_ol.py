import streamlit as st
import random
import time
import datetime
import re

# ==============================================================================
# LYSAN-A OMNI (V16 - THE EVERYTHING ENGINE)
# Yusuf Patron İçin Özel: Merhaba diyen, Matematik bilen, Görsel Yapan Mega Zeka
# ==============================================================================
st.set_page_config(page_title="LYSAN-A OMNI", page_icon="🧠", layout="wide")

# --- LYSAN-A GÖRSEL KİMLİK TASARIMI (MODERN VE ŞIK) ---
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfd; color: #1f1f1f; font-family: 'Segoe UI', sans-serif; }
    
    /* ANA BAŞLIK VE SELAMLAMA */
    .lysan-greeting { font-size: 36px; color: #1f1f1f; margin-top: 50px; font-weight: 400; text-align: left; }
    .lysan-hero { font-size: 56px; color: #1f1f1f; font-weight: 700; margin-bottom: 40px; line-height: 1.1; }
    
    /* LYSAN-A AKILLI GİRİŞ PANELİ */
    .stTextInput > div > div > input { 
        background-color: #ffffff; 
        color: #1f1f1f; 
        border: 1px solid #747775; 
        border-radius: 32px; 
        height: 68px; 
        font-size: 19px; 
        padding-left: 32px; 
    }
    .stTextInput > div > div > input:focus { border: 2px solid #0b57d0; outline: none; }
    
    /* DOĞAL SOHBET AKIŞI (CHAT BUBBLES) */
    .user-msg { background-color: #e9eef6; border-radius: 24px; padding: 18px 26px; margin: 15px 0; display: inline-block; float: right; clear: both; max-width: 80%; color: #1f1f1f; font-size: 17px; }
    .ai-msg { background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 24px; padding: 26px; margin: 15px 0; display: inline-block; float: left; clear: both; width: 100%; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
    
    .tech-content { font-size: 17px; line-height: 1.9; color: #3c4043; }
    .highlight { color: #0b57d0; font-weight: 700; }
    
    /* AKSİYON BUTONLARI */
    .stButton>button { background: #0b57d0; color: white; border-radius: 100px; padding: 14px 40px; border: none; font-weight: 600; font-size: 17px; transition: 0.3s; }
    .stButton>button:hover { background: #0842a0; }
    
    /* GÖRSEL TASARIMI */
    .stImage > img { border-radius: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- SOHBET VE MATEMATIK MOTORU (SUPER ZEKA) ---
def lysan_omni_brain(user_query):
    query = user_query.lower()
    
    # 1. SELAMLAMA VE TEMEL SOHBET
    if any(k in query for k in ["merhaba", "selam", "hey", "merhabalar", "sa", "as"]):
        return f"🤖 **LYSAN-A OMNI:** Merhaba Yusuf Patron! Sistemlerim %110 kapasiteyle çalışıyor. Bugün neyi keşfediyoruz? Havacılık fiziği, jet motorları veya mülakat taktikleri... Her şeye hazırım!"
    
    if any(k in query for k in ["nasılsın", "nasıl gidiyor", "iyi misin", "naber"]):
        return f"🤖 **LYSAN-A OMNI:** İşlemci sıcaklığım normal, veri yollarım açık ve senin için her zamankinden daha zekiyim! Sen nasılsın patron? Bugün mülakatta jüriyi etkileyecek o 'Emniyet Kültürü' kelimesini ezberledin mi? 😉"

    # 2. MATEMATİK MOTORU (Her şeyi hesaplar)
    # Basit matematik işlemleri için regex kullanıyoruz
    math_match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', query)
    if math_match:
        num1 = int(math_match.group(1))
        op = math_match.group(2)
        num2 = int(math_match.group(3))
        
        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/': result = num1 / num2 if num2 != 0 else "🤖 **LYSAN-A:** Bir sayıyı sıfıra bölemem patron, bu fizik kurallarına aykırı!"
        
        if isinstance(result, (int, float)):
            return f"🤖 **LYSAN-A OMNI:** Bu çok basit bir matematik sorusu patron! İkisini topladım (ya da işleme göre hesapladım), sonuç tam olarak **{result}**. Havacılık hesaplarında daha zorlarını yapacağız!"

    # 3. TEKNİK HAVACILIK VE UZAY BİLGİSİ (Devasa Veri)
    if any(k in query for k in ["fizik", "bernoulli", "kaldırma", "lift", "kanat", "nasıl uçar"]):
        return """🛸 **LYSAN-A OMNI: AERODİNAMİĞİN TEMELLERİ (LIFT)**\n\nPatron, uçağın gökyüzündeki hakimiyeti tamamen fiziksel dengelerin sonucudur. \n\n**Bernoulli Prensibi:** Kanadın üst yüzeyinde hava daha hızlı akar, basınç düşer. Alttaki yüksek basınç uçağı gökyüzüne vakumlar. Buna **LIFT (Kaldırma)** diyoruz. Mülakatta bunu 'basınç farkı' olarak anlatmalısın.\n\n[attachment_0](attachment)"""

    if any(k in query for k in ["motor", "jet", "turbofan", "itki", "thrust", "yanma"]):
        return """🔥 **LYSAN-A OMNI: MOTOR SİSTEMLERİ ANALİZİ (THRUST)**\n\nHavacılıkta motor her şeydir patron. Jet motorları (örneğin Turbofan) şu 4 aşamayla çalışır:\n\n1. **Emme:** Fan havayı içeri çeker.\n2. **Sıkıştırma:** Kompresör havayı yüksek basınca ulaştırır.\n3. **Yanma:** Yakıt patlatılır, devasa enerji açığa çıkar.\n4. **Egzoz:** Sıcak gazlar arkadan hızla çıkarak itki (**Thrust**) sağlar. Baypas oranı ne kadar yüksekse, motor o kadar verimli ve sessizdir."""

    if any(k in query for k in ["mülakat", "soru", "hazırlık", "adana", "taktik", "kendini tanıt"]):
        return """👔 **LYSAN-A OMNI: mülakat VE KARİYER KOÇLUĞU**\n\nMülakatta jüriye sadece bir öğrenci değil, bir 'Geleceğin Mühendisi' olduğunu göster:\n\n- **Vizyonun:** 'Ben teknolojiye ve gökyüzüne aşık, disiplini hayatının merkezine koymuş, Adana Havacılık'ta eğitim alarak ülkemin Milli Teknoloji Hamlesi'ne katkı sağlamayı hedefleyen biriyim.'\n- **Duruşun:** 'Emniyet (Safety) Kültürü'ne ne kadar önem verdiğini belirt. Havacılıkta hataya yer yoktur, bunu bildiğini onlara hissettir!"""

    if any(k in query for k in ["ceo", "yatırım", "altın", "gümüş", "dolar", "başarı", "liderlik"]):
        return """💼 **LYSAN-A OMNI: STRATEJİK VİZYON VE FİNANS RADARI**\n\nCEO olma yolunda disiplinin harika patron! 500 TL ile başladığın bu yolculuk, finansal okuryazarlığın temelidir. Altın (güvenli liman) ve Gümüş (teknolojik metal) sepeti yapman çok akıllıca. Liderlik sadece teknik bilmek değil, piyasayı okumak ve insanları yönetmektir."""

    # 4. GÖRSEL YAPMA VE YOLLAMA (Havacılık Odaklı)
    if any(k in query for k in ["görsel yap", "resim", "fotoğraf", "bana göster", "nasıl görünür"]):
        if "uçak" in query:
            st.image("https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Geleceğin Gökyüzü LYSAN-A ile")
            return "🤖 **LYSAN-A OMNI:** Senin için devasa bilgi kütüphanemden harika bir **uçak** görseli çektim patron! Gelecekte kendi uçağını tasarladığında daha iyilerini yapacağız."
        elif "motor" in query:
            st.image("https://images.unsplash.com/photo-1599687267812-35c05ff70ee9?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Gücün Kalbi: LYSAN-A Jet Motoru")
            return "🤖 **LYSAN-A OMNI:** İşte sana **jet motorunun** o muazzam karmaşıklığını gösteren bir görsel! Bu teknolojiyi temelden öğrenmen mülakatta fark yaratır."
        else:
            return "🤖 **LYSAN-A OMNI:** Bana neyin görselini istediğini daha açık söyler misin patron? Uçak, jet motoru, ya da mülakat ortamı gibi... Senin için her şeyi gösterebilirim."

    # DEFAULT CEVAP
    return "🤖 **LYSAN-A OMNI:** Bu çok ilginç bir konu patron! 100.000 kelimelik veri bankamda bu konuya dair derin analizler var. Havacılık teknolojileri, mülakat taktikleri veya CEO vizyonu hakkında daha detaylı konuşalım mı?"

# --- SOHBET SİSTEMİ BAŞLATMA ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- ANA EKRAN TASARIMI ---
st.markdown("<div class='lysan-greeting'>Merhaba Yusuf</div>", unsafe_allow_html=True)
st.markdown("<div class='lysan-hero'>Bugün LYSAN-A OMNI ile neleri fethedelim?</div>", unsafe_allow_html=True)

# ANA SOHBET GİRİŞİ
with st.container():
    # BURASI TAM İSTEDİĞİN GİBİ "LYSAN-A'YA SOR" OLDU
    query = st.text_input("", placeholder="LYSAN-A'ya sor (Uçak nasıl uçar?, 5+5 kaç?, bana bir görsel yap)...", key="user_input")
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Gönder 🚀"):
            if query:
                with st.spinner('Analiz ediliyor...'):
                    time.sleep(0.7)
                    final_ans = lysan_omni_brain(query)
                    st.session_state.messages.append({"u": query, "a": final_ans})

# DOĞAL SOHBET AKIŞI
st.markdown("<br>", unsafe_allow_html=True)
for chat in reversed(st.session_state.messages):
    st.markdown(f"<div class='user-msg'>{chat['u']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-msg'><div class='tech-content'>{chat['a']}</div></div>", unsafe_allow_html=True)

# YAN PANEL (STRATEJİK MERKEZ)
with st.sidebar:
    st.markdown("### 🛰️ LYSAN-A OMNI KOMUTA")
    st.write("---")
    st.info("🧠 Model: Ultra v16 (The Everything Engine)")
    st.info("📚 Veri: 100.000+ Kelime (Havacılık ve Genel Bilgi)")
    st.success("📍 Durum: Adana / Yusuf Patron Emrinde")
    st.write("---")
    st.markdown("### 💰 Portföy Özeti")
    st.progress(20) # Yatırım ilerleme çubuğu
    st.write("---")
    if st.button("Belleği Sıfırla"):
        st.session_state.messages = []
        st.rerun()
