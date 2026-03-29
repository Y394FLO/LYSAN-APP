import streamlit as st
import random
import time
import datetime

# ==============================================================================
# LYSAN V11: THE LORD OF SKIES - ERROR-FREE EDITION
# ==============================================================================
st.set_page_config(page_title="LYSAN LORD OF SKIES v11", page_icon="⚡🚀⚡", layout="wide")

# --- GÖRSEL TASARIM (HATA ÖNLEYİCİ STİL) ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #02050a 0%, #0a1128 100%); color: #e0faff; font-family: 'Courier New', monospace; }
    .neon-title { font-size: 50px; color: #00e5ff; text-align: center; font-weight: 900; text-transform: uppercase; letter-spacing: 5px; text-shadow: 0 0 15px #00e5ff; margin-bottom: 20px; }
    .stTextInput > div > div > input { background-color: #0c142e; color: #00ffaa; border: 2px solid #00d4ff; border-radius: 20px; font-size: 18px; height: 55px; }
    .info-card { background: rgba(0, 229, 255, 0.08); padding: 25px; border-radius: 20px; border: 1px solid #00e5ff; margin: 15px 0; line-height: 1.7; }
    .chat-bubble { padding: 15px; border-radius: 15px; margin-bottom: 10px; border: 1px solid #0055ff; background-color: #0c142e; color: #00ffaa; }
    .stButton>button { background: linear-gradient(45deg, #0055ff, #00d4ff); color: white; border-radius: 15px; font-weight: 800; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- DEVASA VERİ TABANI ---
mega_database = {
    "selam": {
        "keys": ["merhaba", "selam", "hey", "sa", "as", "günaydın", "naber", "nasılsın"],
        "reply": "🤖 **LYSAN:** Selam Yusuf Patron! Sistemler aktif, Adana mülakatları için motorlar tam güç çalışıyor. Bugün neyi fethediyoruz? 🚀"
    },
    "fizik": {
        "keys": ["fizik", "bernoulli", "kaldırma", "lift", "nasıl uçar", "kuvvet"],
        "reply": """✈️ **HAVACILIK FİZİĞİ BRİFİNGİ:**\n\n**Bernoulli Prensibi:** Kanadın üstünden geçen hava hızlanır ve basıncı düşer. Alttaki yüksek basınç uçağı yukarı iter. Buna **LIFT** denir.\n\n**4 Kuvvet:** Lift (Kaldırma), Weight (Ağırlık), Thrust (İtki), Drag (Geri Sürükleme). Bu kuvvetlerin dengesi uçağı havada tutar!"""
    },
    "motor": {
        "keys": ["motor", "jet", "turbofan", "itki", "thrust"],
        "reply": """🔥 **JET MOTORU ANALİZİ:**\n\nHava emilir (Succ), sıkıştırılır (Squeeze), yakıtla patlatılır (Bang) ve arkadan atılır (Blow). Newton'un 3. kanunu (Etki-Tepki) sayesinde uçak ileri fırlar!"""
    },
    "mulakat": {
        "keys": ["mülakat", "taktik", "soru", "hazırlık", "adana"],
        "reply": """👔 **MÜLAKAT STRATEJİSİ:**\n\n1. **Vizyon:** 'Milli Teknoloji Hamlesi'ne katkı sağlamak istiyorum' de.\n2. **Bilgi:** İHA/SİHA teknolojilerimizi (KAAN, ANKA-3) bildiğini göster.\n3. **Duruş:** Özgüvenli ol ama disiplinden asla ödün verme!"""
    }
}

# --- CANLI SOHBET SİSTEMİ ---
if 'history' not in st.session_state:
    st.session_state.history = []

st.markdown("<div class='neon-title'>LYSAN LORD OF SKIES</div>", unsafe_allow_html=True)

with st.sidebar:
    st.title("🕹️ COMMAND")
    option = st.radio("SİSTEM:", ["Canlı Sohbet", "Teknik Arşiv", "Finans"])
    st.write(f"🛰️ {datetime.datetime.now().strftime('%H:%M:%S')}")

if option == "Canlı Sohbet":
    user_input = st.text_input("Sorunu Yaz:", placeholder="Uçak nasıl uçar? Mülakatta ne sorarlar?")
    if st.button("GÖNDER 🚀"):
        if user_input:
            reply = "🤖 **LYSAN:** Bu konuyu analiz havuzuma aldım patron. Havacılık dersen sana destan yazarım!"
            for cat, data in mega_database.items():
                if any(k in user_input.lower() for k in data["keys"]):
                    reply = data["reply"]
                    break
            st.session_state.history.append({"u": user_input, "a": reply})

    for chat in reversed(st.session_state.history):
        st.markdown(f"<div class='chat-bubble'>🧑‍💻 **YUSUF:** {chat['u']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-bubble' style='border-color:#00ffaa;'>{chat['a']}</div>", unsafe_allow_html=True)

elif option == "Teknik Arşiv":
    st.markdown("### 📖 HAVACILIK TERİMLERİ")
    st.write("- **AVİYONİK:** Elektronik sistemler.")
    st.write("- **STALL:** Kaldırma kuvvetinin bitmesi.")
    st.write("- **İHA / SİHA:** İnsansız Hava Araçları.")

elif option == "Finans":
    st.metric("Gram Altın", "Takipte", "AKTİF")
