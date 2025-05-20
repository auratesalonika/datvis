import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Smart Farming", layout="wide")
st.title("📊 Dashboard Data Sensor Pertanian - Smart Farming")

# Upload file CSV
uploaded_file = st.file_uploader("Unggah dataset CSV dari Kaggle", type="csv")

if uploaded_file:
    # Baca data
    df = pd.read_csv(uploaded_file)
    
    # Tampilkan data awal
    st.subheader("🔍 Tinjauan Data")
    st.dataframe(df.head())

    # Info dataset
    st.markdown("""
    **Fitur Penting:**
    - Temperature
    - Humidity
    - Soil Moisture
    - Light Intensity
    - Rainfall
    - Pressure
    - Soil Temperature
    - Target: Crop Yield
    """)

    # Visualisasi hubungan antar fitur
    st.subheader("📈 Korelasi Antar Variabel")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

    # Visualisasi tren fitur utama
    st.subheader("🌡️ Tren Suhu, Kelembaban, dan Curah Hujan")
    cols = st.multiselect("Pilih fitur untuk dianalisis:", ["Temperature", "Humidity", "Rainfall", "Soil Moisture", "Light Intensity"], default=["Temperature", "Humidity"])

    if cols:
        fig2, ax2 = plt.subplots()
        df[cols].plot(ax=ax2)
        plt.xlabel("Index Waktu")
        plt.ylabel("Nilai Sensor")
        plt.title("Tren Sensor")
        st.pyplot(fig2)

    # Analisis prediktif sederhana
    st.subheader("📊 Hubungan Sensor dengan Hasil Panen")
    selected_x = st.selectbox("Pilih variabel sensor:", ["Temperature", "Humidity", "Soil Moisture", "Rainfall", "Light Intensity", "Pressure", "Soil Temperature"])

    fig3, ax3 = plt.subplots()
    sns.scatterplot(x=df[selected_x], y=df["CropYield"], ax=ax3)
    ax3.set_xlabel(selected_x)
    ax3.set_ylabel("Crop Yield")
    ax3.set_title(f"Hubungan antara {selected_x} dan Crop Yield")
    st.pyplot(fig3)

    # Narasi Data Storytelling
    st.subheader("📝 Narasi Data Storytelling")
    st.markdown(f"""
    - Dari visualisasi heatmap, terlihat bahwa fitur **{selected_x}** memiliki hubungan tertentu terhadap hasil panen (**CropYield**).
    - Berdasarkan grafik scatter, kita bisa mengamati apakah semakin tinggi/lrendah nilai {selected_x}, maka hasil panen ikut berubah atau tidak.
    - Data sensor yang dikumpulkan melalui perangkat IoT ini bisa menjadi dasar untuk pengambilan keputusan seperti irigasi, pemupukan, atau prediksi hasil panen secara akurat.

    **Kesimpulan:**
    Dengan menganalisis data sensor secara berkala dan menghubungkannya dengan hasil panen, petani dapat meningkatkan efisiensi pertanian berbasis data.
    """)
else:
    st.info("Silakan unggah file CSV dataset sensor pertanian dari Kaggle untuk mulai.")
