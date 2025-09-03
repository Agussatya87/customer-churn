# 📊 Customer Churn Prediction
Proyek ini membangun model Machine Learning untuk memprediksi Customer Churn (apakah pelanggan akan berhenti berlangganan atau tidak) menggunakan dataset pelanggan. Aplikasi akhir disajikan dalam bentuk FastAPI dan dapat menerima input data untuk melakukan prediksi secara real-time.

## 🔎 Project Overview
Customer churn, atau berhentinya pelanggan dari layanan berlangganan, merupakan tantangan strategis yang berdampak langsung pada stabilitas dan pertumbuhan perusahaan telekomunikasi.  Oleh karena itu, memahami dan mengantisipasi perilaku churn menjadi kunci dalam menjaga stabilitas bisnis dan meningkatkan profitabilitas jangka panjang. Proyek ini bertujuan untuk memprediksi churn pelanggan menggunakan data historis pelanggan dari industri telekomunikasi. Dengan model ini, perusahaan dapat:
- Mengidentifikasi pelanggan berisiko tinggi untuk churn.
- Mengambil langkah preventif (misalnya promo atau diskon).
- Meningkatkan retensi pelanggan dan profitabilitas jangka panjang.

## 📊 Dataset
Dataset yang digunakan dalam proyek ini berasal dari Kaggle:

🔗 [Telecom Customer Churn Dataset (Kaggle)](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis) 

Dataset ini berisi informasi pelanggan seperti:
- Data demografi (gender dan usia).
- Informasi layanan (Fiber Optik, internet service, dan DSL).
- Informasi kontrak & pembayaran (jenis kontrak).
- Informasi biaya (MonthlyCharges, TotalCharges).
Label target: Churn (Yes/No).

## 🛠️ Workflow Project

Proyek ini mengikuti alur kerja berikut untuk membangun sistem prediksi churn pelanggan:

### 1. Exploratory Data Analysis (EDA)
- Memahami distribusi data.
- Mengidentifikasi pola churn.
- Mengidentifikasi Korelasi antar fitur dengan target 
- Menggali insight dari perilaku pelanggan.

### 2. Data Preprocessing
- Encoding variabel kategorikal.
- Normalisasi fitur numerik.
- Menangani nilai yang hilang (missing values).

### 3. Modeling
- Melatih beberapa algoritma seperti:
  - XGBoost
  - Random Forest
- Mengevaluasi dan memilih model terbaik berdasarkan metrik performa.
- Menggunakan Hyperparameter Tuning untuk mencari parameter terbaik

### 4. Deployment
- Menyimpan model terbaik (`best_model.pkl`) bersama encoder dan scaler.
- Membangun API prediksi menggunakan **FastAPI**.
- Membuat antarmuka pengguna (UI) sederhana untuk input data pelanggan.

