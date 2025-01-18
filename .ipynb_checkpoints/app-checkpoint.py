import streamlit as st
import numpy as np
import pickle

# Load model pickle
with open('decision_tree_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Judul aplikasi
st.title("Aplikasi Prediksi Penyakit Jantung")

# Input dari pengguna
age = st.number_input("Usia pasien:", min_value=1, max_value=120, value=50)
sex = st.selectbox("Jenis kelamin:", ["Laki-laki", "Perempuan"], index=0)
cp = st.selectbox("Jenis nyeri dada:", ["Typical angina (0)", "Atypical angina (1)", "Non-anginal pain (2)", "Asymptomatic (3)"], index=0)
trestbps = st.number_input("Tekanan darah saat istirahat (mmHg):", min_value=50, max_value=200, value=125)
chol = st.number_input("Kadar kolesterol serum (mg/dL):", min_value=100, max_value=400, value=200)
fbs = st.selectbox("Gula darah puasa > 120 mg/dL:", ["Tidak", "Ya"], index=0)
restecg = st.selectbox("Hasil EKG setelah istirahat:", ["Normal (0)", "Abnormal (1)", "Hypertrophy (2)"], index=0)
thalach = st.number_input("Detak jantung maksimum (bpm):", min_value=60, max_value=220, value=150)
exang = st.selectbox("Mengalami angina setelah berolahraga:", ["Tidak", "Ya"], index=0)
oldpeak = st.number_input("Depresi segmen ST (mm):", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
slope = st.selectbox("Kemiringan segmen ST:", ["Menanjak (0)", "Datar (1)", "Menurun (2)"], index=1)
ca = st.number_input("Jumlah pembuluh darah utama yang diwarnai:", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thalasemia:", ["Normal (1)", "Cacat Tetap (2)", "Cacat Reversibel (3)"], index=0)

# Encode inputs
sex_encoded = 1 if sex == "Laki-laki" else 0
cp_encoded = [0, 1, 2, 3][cp.index(cp)]
fbs_encoded = 1 if fbs == "Ya" else 0
restecg_encoded = [0, 1, 2][restecg.index(restecg)]
exang_encoded = 1 if exang == "Ya" else 0
slope_encoded = [0, 1, 2][slope.index(slope)]
thal_encoded = [1, 2, 3][thal.index(thal)]

# Masukkan semua data ke dalam array
data_input = np.array([[age, sex_encoded, cp_encoded, trestbps, chol, fbs_encoded, restecg_encoded,
                        thalach, exang_encoded, oldpeak, slope_encoded, ca, thal_encoded]])

# Tombol untuk prediksi
if st.button("Prediksi"):
    prediction = model.predict(data_input)[0]
    if prediction == 1:
        st.error("Hasil prediksi: Berisiko terkena penyakit jantung.")
    else:
        st.success("Hasil prediksi: Tidak berisiko terkena penyakit jantung.")