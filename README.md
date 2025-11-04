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
Jumlah Baris : 1000 records
Jumlah Fitur : 10

Dataset ini berisi informasi pelanggan seperti:
- Data demografi (gender dan usia).
- Informasi layanan (Fiber Optik, internet service, dan DSL).
- Informasi kontrak & pembayaran (jenis kontrak).
- Informasi biaya (MonthlyCharges, TotalCharges).
- Label target: Churn (Yes/No).

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
  - Support Vector Machine
- Mengevaluasi dan memilih model terbaik berdasarkan metrik performa.
- Menggunakan Hyperparameter Tuning untuk mencari parameter terbaik

### 4. Deployment
- Menyimpan model terbaik (`best_model.pkl`) bersama encoder dan scaler.
- Membangun API prediksi menggunakan **FastAPI**.
- Membuat antarmuka pengguna (UI) sederhana untuk input data pelanggan.

## Result
### 1. Exploratory Data Analysis
Dalam analisis data churn pelanggan, langkah pertama yang penting adalah memahami karakteristik target label yang digunakan. Target label ini akan menjadi acuan utama dalam membangun model prediksi, sehingga distribusinya perlu diperhatikan. Distribusi label yang tidak seimbang dapat mempengaruhi performa model, karena model cenderung lebih "condong" pada kelas yang dominan. Oleh karena itu, kita perlu menganalisis terlebih dahulu bagaimana proporsi data churn dalam dataset ini.

<img width="600" height="400" alt="churn_label" src="https://github.com/user-attachments/assets/fe7dbade-79ac-4937-9207-6a79a0fcba09" />

Berdasarkan diagram di atas, dapat dilihat bahwa dari total 1000 pelanggan, sebanyak 88.3% pelanggan tercatat churn ("Yes"), sementara hanya 11.7% pelanggan yang tidak churn ("No"). Hal ini menunjukkan bahwa data yang digunakan sangat tidak seimbang (imbalanced), di mana jumlah pelanggan yang churn jauh lebih banyak dibandingkan dengan yang tidak churn. Kondisi ini perlu mendapat perhatian khusus, terutama ketika membangun model prediksi. Jika tidak ditangani, model berisiko bias terhadap kelas mayoritas (churn), sehingga akurasi mungkin terlihat tinggi tetapi kemampuan mendeteksi pelanggan yang tidak churn menjadi sangat rendah. lalu langkah selanjutnya adalah mengecek apakah terdapat missing value atau tidak.

<img width="277" height="282" alt="image" src="https://github.com/user-attachments/assets/1bc519cb-888d-4830-9ef2-84f3d4018895" />

Dari hasil analisis, terlihat bahwa hampir seluruh kolom tidak memiliki missing value, kecuali pada kolom InternetService yang memiliki 297 nilai kosong (hampir 30% dari total data). Mengabaikan atau menghapus data sebanyak ini berpotensi menyebabkan hilangnya informasi penting dan menurunkan kualitas dataset. Oleh karena itu, strategi yang dipilih adalah mengganti nilai kosong tersebut dengan kategori baru, yaitu "No Internet Service". Pendekatan ini dipandang logis karena pelanggan yang tidak memiliki layanan internet memang relevan untuk dimasukkan ke dalam kategori tersendiri, bukan dianggap sebagai data hilang. Setelah memahami distribusi label target dan missing value pada data, langkah berikutnya adalah melihat hubungan antara variabel numerik dengan label churn. Korelasi ini membantu mengidentifikasi apakah ada hubungan yang cukup kuat antara fitur numerik dengan kemungkinan seorang pelanggan melakukan churn.

<img width="541" height="432" alt="e1774cf9-0092-4e23-ad13-5f5491e3b22d" src="https://github.com/user-attachments/assets/b8512b28-7d69-4e12-9b9c-e6f1c02e1e82" />

Dari korelasi tersebut, Tenure adalah faktor paling berpengaruh terhadap churn (pelanggan baru lebih rawan churn). Selain mencari bagaimana korelasi antar fitur numerik dengan label, hal yang sama dilakukan pada fitur kategorikal seperti ContractType.

<img width="638" height="258" alt="image" src="https://github.com/user-attachments/assets/0eca1c01-8ea2-4b39-9461-34978aff76a5" />

Berdasarkan hasil analisis menggunakan Cramér’s V, diperoleh nilai sebesar 0,37 antara variabel ContractType dengan potensi Churn. Nilai ini menunjukkan adanya korelasi sedang antara jenis kontrak yang dipilih pelanggan dengan kemungkinan mereka melakukan churn. Dari tabel kontingensi terlihat bahwa:
- Pelanggan dengan kontrak Month-to-Month memiliki proporsi churn yang jauh lebih tinggi (511 churn dibandingkan 0 yang bertahan).
- Sebaliknya, pelanggan dengan kontrak One-Year (71 bertahan, 218 churn) dan Two-Year (46 bertahan, 154 churn) cenderung lebih stabil dibandingkan kontrak bulanan.
Temuan ini menjadikan dugaan bahwa pelanggan dengan kontrak jangka panjang lebih loyal dan memiliki kemungkinan churn yang lebih rendah, sedangkan pelanggan kontrak bulanan lebih fleksibel sehingga lebih mudah untuk berhenti berlangganan. Dengan demikian, ContractType dapat dianggap sebagai salah satu fitur penting dalam memprediksi churn.

### Data Prerpocessing
- Dataset dilakukan normalisasi agar model lebih memahami data dengan skala
- kemudian dataset dilakukan split data dengan perbandingan 70:30
- selanjutnya imbalance data dilakukan dengan metode oversampling menggunakan SMOTE.

### Modeling & Evaluation
- Model yang digunakan adalah Random Forest, XGBoost, dan SVM
- Diberlakukan tuning parameter menggunakan GridSearchCV untuk ketiga model algoritma.
- Best parameter yang didapat setelah melakukan tuning sebagai berikut:
  - Random Forest (max_depth:10 dan n_estimators:50) dengan best score 100%
  - XGBoost (learning_rate:0.01 dan max_depth:5) dengan best score 99%
  - SVM (C:100, gamma:scale, kernel:rbf) dengan best score 99%

Dari hasil tuning didapat bahwa Random Forest memiliki accuracy yang sangat akurat, dan Random Forest dipilih untuk melakukan Evaluasi dan pengujian ROC - AUC dengan hasil yang terbilang sempurna. setelah itu untuk melihat fitur mana yang berperan penting pada model algoritma Random Forest, digunakan Feature Importance dari model bawaan RF, hasil yang didapat sebagai berikut

<img width="837" height="547" alt="image" src="https://github.com/user-attachments/assets/985749fd-0d14-4fd2-bcc3-8d4ce7be17fa" />

Berdasarkan hasil analisis Feature Importance menggunakan model Random Forest, terlihat bahwa variabel yang paling berpengaruh dalam memprediksi churn adalah Tenure, TechSupport, dan ContractType, dengan skor pentingnya masing-masing berada pada urutan teratas. Hal ini menunjukkan bahwa lama berlangganan (Tenure) menjadi indikator kuat dalam menentukan kecenderungan pelanggan untuk bertahan atau berhenti. Semakin lama pelanggan bertahan, kecenderungan churn semakin rendah. Selain itu, fitur TechSupport juga berperan penting. Pelanggan yang mendapatkan dukungan teknis cenderung lebih puas dan loyal, sehingga peluang churn lebih rendah. Sementara itu, ContractType juga sangat berpengaruh, sejalan dengan hasil uji Cramér’s V sebelumnya, di mana pelanggan dengan kontrak jangka panjang (One-Year atau Two-Year) memiliki risiko churn lebih kecil dibandingkan dengan kontrak bulanan. Fitur lain seperti InternetService, MonthlyCharges, dan TotalCharges memiliki kontribusi menengah terhadap prediksi churn, menunjukkan bahwa biaya dan jenis layanan juga memengaruhi keputusan pelanggan, meskipun tidak sekuat faktor kontrak dan dukungan teknis. Sementara itu, fitur Age dan Gender memiliki pengaruh yang relatif sangat kecil terhadap churn, sehingga dapat dianggap kurang signifikan dalam model ini.

Secara keseluruhan, temuan ini menegaskan perlu fokus ke pelanggan dengan kontrak bulanan karena memiliki resiko berhenti berlangganan paling tinggi.
