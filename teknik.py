import streamlit as st

st.set_page_config(page_title="LYSAN: Havacılık", page_icon="🚀")
st.title("🚀 LYSAN OPERASYON MERKEZİ")

menu = st.sidebar.radio("MENÜ", ["ANA SAYFA", "TEKNİK SORU-CEVAP", "PİYASA"])

if menu == "ANA SAYFA":
    st.header("Hoş Geldin Patron! 🦾")
    st.info("LYSAN Sistemleri %100 Kapasiteyle Çalışıyor.")

elif menu == "TEKNİK SORU-CEVAP":
    st.header("🔍 Teknik Bilgi Bankası")
    soru = st.text_input("Bir terim yazın (Örn: Stall, Lift, Kanat):").lower()
    if soru:
        if "stall" in soru:
            st.success("Cevap: Uçağın kaldırma kuvvetini kaybedip havada tutunamamasıdır.")
        elif "lift" in soru:
            st.success("Cevap: Kanat altı ve üstündeki basınç farkıyla oluşan kaldırma kuvvetidir.")
        elif "kanat" in soru:
            st.success("Cevap: Taşıma kuvveti üreten ana aerodinamik parçadır.")
        else:
            st.warning("Bu terimi henüz öğrenmedim patron!")

elif menu == "PİYASA":
    st.header("💰 Yatırım Takibi")
    st.write("Gram Altın ve Gümüş verileri burada görünecek.")
