Siap, ini aku buatin **README.md lengkap + business questions khas data analyst** yang sudah disesuaikan dengan project kamu 👇

---

# Electricity Consumption Analysis in Indonesia (2011–2030)

## Project Overview

Project ini bertujuan untuk menganalisis pola konsumsi listrik di Indonesia berdasarkan data provinsi dan nasional, serta memahami faktor-faktor sosioekonomi yang memengaruhinya.

Analisis dilakukan dalam tiga tahap utama:

1. **Exploratory Data Analysis (EDA)** – memahami distribusi dan tren konsumsi listrik
2. **Socioeconomic Analysis** – menghubungkan konsumsi listrik dengan faktor ekonomi & demografi
3. **Forecasting** – memprediksi konsumsi listrik nasional hingga tahun 2030

---

## Objectives

* Menganalisis distribusi konsumsi listrik antar provinsi
* Mengidentifikasi wilayah dengan konsumsi listrik tertinggi
* Mengukur pertumbuhan konsumsi listrik (YoY & CAGR)
* Membandingkan konsumsi listrik Jawa vs luar Jawa
* Mengelompokkan provinsi berdasarkan pola konsumsi dan pertumbuhan
* Menganalisis pengaruh faktor sosioekonomi terhadap konsumsi listrik
* Memprediksi konsumsi listrik nasional di masa depan

---

## Business Questions (Data Analyst Perspective)

### Descriptive Analysis

* Provinsi mana yang memiliki konsumsi listrik tertinggi di Indonesia?
* Bagaimana distribusi konsumsi listrik antar provinsi?
* Apakah terdapat ketimpangan konsumsi listrik antar wilayah?

### Trend Analysis

* Bagaimana tren konsumsi listrik nasional dari tahun ke tahun?
* Apakah terdapat penurunan atau lonjakan signifikan pada periode tertentu?
* Bagaimana pertumbuhan Year-over-Year (YoY) konsumsi listrik?

### Regional Analysis

* Bagaimana perbandingan konsumsi listrik antara Jawa dan luar Jawa?
* Apakah wilayah luar Jawa menunjukkan pertumbuhan yang lebih cepat?

### Growth Analysis

* Provinsi mana yang memiliki pertumbuhan konsumsi listrik tercepat (CAGR)?
* Apakah terdapat pola “catch-up growth” di wilayah dengan konsumsi rendah?

### Segmentation (Clustering)

* Bagaimana segmentasi provinsi berdasarkan konsumsi dan pertumbuhan listrik?
* Apa karakteristik dari masing-masing cluster (high growth, mature, dll)?

### Socioeconomic Analysis

* Apakah konsumsi listrik berkorelasi dengan jumlah penduduk?
* Bagaimana hubungan antara konsumsi listrik dan PDRB?
* Apakah wilayah dengan tingkat kemiskinan tinggi memiliki konsumsi listrik lebih rendah?
* Apakah electricity intensity mencerminkan efisiensi ekonomi?

### Forecasting

* Bagaimana proyeksi konsumsi listrik nasional hingga tahun 2030?
* Seberapa akurat model dalam memprediksi tren konsumsi listrik?
* Apakah permintaan listrik akan terus meningkat di masa depan?

---

## Project Structure

```
electricity_consumption/
│
├── data/
│   ├── raw_data/
│   └── processed/
│       ├── listrik_clean.csv
│       ├── population_clean.csv
│       ├── pdrb_clean.csv
│       ├── poverty_clean.csv
│       └── forecast.csv
│
├── notebooks/
│   ├── 01_electricity_consumption_insights_(2011–2024).ipynb
│   ├── 02_socioeconomic_drivers_of_electricity_(2017–2024).ipynb
│   └── 03_electricity_demand_forecasting.ipynb
│
├── scripts/
│   └── clean_data.py
│
├── sql/
│   ├── 01_create_database.sql
│   └── 02_create_tables.sql
│
├── .venv/
├── .vscode/
└── README.md
```

---

## Data Pipeline

1. **Raw Data Collection**

   * Data listrik, populasi, PDRB, dan kemiskinan dari BPS

2. **Data Cleaning (Python)**

   * Standardisasi nama provinsi
   * Penanganan pemekaran Papua
   * Konversi tipe data
   * Output ke folder `processed/`

3. **Data Storage (SQL)**

   * Load ke PostgreSQL menggunakan `COPY`
   * Relasi berdasarkan `tahun` dan `provinsi`

4. **Feature Engineering**

   * Electricity per Capita
   * Electricity Intensity
   * Poverty Rate
   * PDRB per Capita

5. **Analysis & Modeling**

   * EDA (Seaborn, Matplotlib)
   * Clustering (K-Means)
   * Forecasting (ARIMA)

---

## Key Insights

* Konsumsi listrik **didominasi oleh Pulau Jawa**
* Terdapat **ketimpangan konsumsi listrik antar wilayah**
* Wilayah luar Jawa menunjukkan **pertumbuhan lebih cepat**
* Terdapat pola **catch-up growth** di provinsi berkembang
* Konsumsi listrik nasional menunjukkan **tren meningkat**
* Forecast menunjukkan **permintaan listrik akan terus naik hingga 2030**

---

## Limitations

* Data tahun **2016 tidak tersedia**
* Model forecasting **tidak mempertimbangkan faktor eksternal**
* Data bersifat agregat provinsi (tidak granular sektor)

---

## Tools & Technologies

* **Python** (Pandas, NumPy, Seaborn, Matplotlib)
* **Machine Learning** (Scikit-learn, ARIMA - statsmodels)
* **SQL (PostgreSQL)**
* **Jupyter Notebook**
* **Git & GitHub**

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/username/electricity_consumption.git
cd electricity_consumption
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Data Cleaning

```bash
python scripts/clean_data.py
```

### 4. Run Analysis

Buka folder `notebooks/` dan jalankan notebook sesuai urutan:

1. EDA
2. Socioeconomic Analysis
3. Forecasting

---

## Future Improvements

* Menambahkan variabel:

  * Industri
  * Urbanisasi
  * Infrastruktur listrik
* Menggunakan model forecasting yang lebih advanced (Prophet, LSTM)
* Analisis per sektor (rumah tangga, industri, dll)