import streamlit as st

# LYSAN GÖRSEL ARAYÜZ
st.set_page_config(page_title="LYSAN: Havacılık", page_icon="🚀")
st.title("🚀 LYSAN OPERASYON MERKEZİ")
st.markdown("---")

menu = st.sidebar.radio("MENÜ", ["ANA SAYFA", "TEKNİK", "PİYASA", "MÜLAKAT"])

if menu == "ANA SAYFA":
    st.header("Hoş Geldin Patron! 🦾")
    st.info("LYSAN Sistemleri %100 Kapasiteyle Çalışıyor.")
    st.write("Adana Havacılık ve Uzay Bilimleri için her şey hazır.")
elif menu == "TEKNİK":
    st.header("🔍 Aerodinamik Analiz")
    st.success("Lift (Kaldırma) kuvveti analiz ediliyor...")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Airfoil_lift.svg/500px-Airfoil_lift.svg.png")
elif menu == "PİYASA":
    st.header("💰 Finansal Veri")
    st.metric("Gram Altın", "📈 Yükselişte")
    st.metric("Gümüş", "🛡️ Stabil")
elif menu == "MÜLAKAT":
    st.header("✈️ Mülakat Hazırlık")
    st.warning("Soru: Stall nedir?")
    st.write("> Cevap: Uçağın kaldırma kuvvetini kaybedip düşüşe geçmesidir.")
  
