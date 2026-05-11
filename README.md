# 🔌 Electricity Consumption in Indonesia — Analysis & Forecasting

Proyek ini menganalisis pola konsumsi listrik di Indonesia berdasarkan data provinsi dan nasional, mengintegrasikan variabel sosioekonomi, serta membangun model forecasting untuk memperkirakan permintaan listrik ke depan.

---

## 📁 Struktur Notebook

| No. | Notebook | Deskripsi |
|-----|----------|-----------|
| 01 | `01_electricity_consumption_insights__2011_2024_.ipynb` | Eksplorasi pola konsumsi listrik per provinsi (2011–2024) |
| 02 | `02_socioeconomic_drivers_of_electricity__2017_2024_.ipynb` | Analisis faktor sosioekonomi terhadap konsumsi listrik (2017–2024) |
| 03 | `03_electricity_demand_forecasting.ipynb` | Forecasting konsumsi listrik nasional menggunakan ARIMA (2025–2030) |

---

## 📊 Notebook 01 — Electricity Consumption Insights (2011–2024)

### Tujuan
Mengeksplorasi pola konsumsi listrik di Indonesia berdasarkan data per provinsi dan nasional selama periode **2011–2024**.

### Analisis yang Dilakukan
- Distribusi konsumsi listrik antar provinsi
- Identifikasi **Top 10 Provinsi** dengan konsumsi listrik tertinggi
- Tren konsumsi listrik **nasional** dari waktu ke waktu
- **Year-over-Year (YoY)** growth konsumsi listrik nasional
- **CAGR** per provinsi untuk mengukur pertumbuhan jangka panjang
- Perbandingan regional: **Jawa vs Luar Jawa**
- **Segmentasi provinsi** menggunakan K-Means Clustering

### Dataset
- **Sumber:** `data/processed/listrik_clean.csv`
- **Variabel utama:**
  - `provinsi` — nama provinsi
  - `tahun` — tahun observasi
  - `listrik_gwh` — konsumsi listrik (GWh)
- **Cakupan:** 34 provinsi + agregasi nasional, 2011–2024
- **Catatan:** Data tahun 2016 tidak tersedia

### Key Findings
- **Pulau Jawa mendominasi** konsumsi listrik, dengan Jawa Barat sebagai provinsi tertinggi
- Konsumsi listrik nasional menunjukkan **tren meningkat** secara konsisten, dengan sedikit penurunan di tahun 2020
- Setelah 2020, pertumbuhan **kembali stabil di kisaran 5–7%** per tahun
- **Maluku Utara** memiliki CAGR tertinggi (~17%), diikuti provinsi-provinsi di Sulawesi
- Hasil clustering menghasilkan 3 segmen provinsi:
  - 🟢 **High Growth Regions** — pertumbuhan cepat (~10.97%), konsumsi menengah, didominasi luar Jawa
  - 🟡 **Moderate Growth Regions** — pertumbuhan stabil (~7.04%), konsumsi menengah
  - 🔴 **Mature High-Demand Regions** — konsumsi tertinggi, pertumbuhan lebih lambat (~4.42%), didominasi Jawa

---

## 📊 Notebook 02 — Socioeconomic Drivers of Electricity (2017–2024)

### Tujuan
Mengintegrasikan data konsumsi listrik dengan indikator sosioekonomi untuk memahami **faktor-faktor yang memengaruhi permintaan listrik** antar provinsi.

### Analisis yang Dilakukan
- Integrasi dataset: listrik + populasi + PDRB + kemiskinan (2017–2024)
- **Feature engineering:** electricity per capita, electricity intensity, poverty rate, PDRB per capita
- **Correlation analysis** (heatmap) antar variabel
- Scatter plot: PDRB vs konsumsi listrik (skala asli & log)
- Scatter plot: populasi vs konsumsi listrik
- Scatter plot: PDRB per kapita vs konsumsi listrik per kapita
- Scatter plot: poverty rate vs electricity per capita

### Dataset
- **Sumber:**
  - `data/processed/listrik_clean.csv`
  - `data/processed/population_clean.csv`
  - `data/processed/pdrb_clean.csv`
  - `data/processed/poverty_clean.csv`
- **Variabel tambahan:**
  - `population` — jumlah penduduk provinsi
  - `pdrb_miliar` — PDRB provinsi (miliar rupiah)
  - `poor_population` — jumlah penduduk miskin
- **Cakupan:** 272 observasi provinsi–tahun (2017–2024)

### Key Findings
- Konsumsi listrik berkorelasi **sangat kuat** dengan populasi (r = 0.90) dan PDRB (r = 0.91)
- Konsumsi per kapita berkorelasi positif dengan **PDRB per kapita** (r = 0.68)
- **Tingkat kemiskinan** berkorelasi negatif dengan konsumsi listrik per kapita (r = −0.49)

---

## 📊 Notebook 03 — Electricity Demand Forecasting

### Tujuan
Membangun model **ARIMA** untuk memproyeksikan konsumsi listrik nasional Indonesia hingga tahun **2030** berdasarkan data historis 2011–2024.

### Tahapan Analisis
1. Load & preprocessing data konsumsi listrik nasional
2. Penanganan missing data tahun 2016 dengan **linear interpolation**
3. **Stationarity Test** (ADF Test) — hasilnya: data tidak stasioner (p-value = 0.994), sehingga digunakan `d=1`
4. **Walk-Forward Validation** untuk evaluasi model
5. Fitting model **ARIMA(1,1,1)** pada keseluruhan data
6. Forecasting **6 tahun ke depan** (2025–2030)

### Dataset
- **Sumber:** `data/processed/listrik_clean.csv`
- **Output:** `data/processed/forecast.csv`

### Model Performance
| Metrik | Nilai |
|--------|-------|
| MAE    | ~7.700 GWh |
| RMSE   | ~7.800 GWh |
| Error relatif | ~2–3% dari nilai aktual |

### Hasil Forecasting
Konsumsi listrik nasional diproyeksikan **terus meningkat**:

| Tahun | Proyeksi Konsumsi |
|-------|-------------------|
| 2025  | ~316.000 GWh |
| 2030  | ~368.000 GWh |

> ⚠️ Hasil forecasting hanya berdasarkan pola historis dan tidak memasukkan faktor eksternal seperti kebijakan energi, perubahan teknologi, atau kondisi ekonomi makro. Hasil sebaiknya diinterpretasikan sebagai **indikasi tren potensial**.

---

## 🗂️ Struktur Direktori

```
electricity_consumption/
│
├── data/
│   ├── raw/                    
│   └── processed/
│       ├── listrik_clean.csv
│       ├── population_clean.csv
│       ├── pdrb_clean.csv
│       ├── poverty_clean.csv
│       └── forecast.csv
│
├── notebooks/
│   ├── 01_electricity_consumption_insights__2011_2024_.ipynb
│   ├── 02_socioeconomic_drivers_of_electricity__2017_2024_.ipynb
│   └── 03_electricity_demand_forecasting.ipynb
│
├── sql/
│   ├── 01_create_database.sql
│   └── 02_create_tables.sql
│
├── notebooks/
│   └── clean_data.py
│
└── README.md
```

---

## 📦 Data Sources

Seluruh data mentah bersumber dari **Badan Pusat Statistik (BPS) Indonesia** — [bps.go.id](https://www.bps.go.id).

---

## 🛠️ Tools & Libraries

- **Python** — pandas, numpy, matplotlib, seaborn
- **Machine Learning** — scikit-learn (KMeans, StandardScaler, metrics)
- **Time Series** — statsmodels (ARIMA, ADF Test, ACF/PACF)

---

## ⚠️ Data Limitations

- Data tahun **2016 tidak tersedia**; pada notebook 01 dibiarkan kosong, pada notebook 03 diisi dengan linear interpolation khusus untuk kebutuhan time series
- Analisis sosioekonomi (notebook 02) difokuskan pada **2017–2024** karena keterbatasan ketersediaan data indikator ekonomi
- Model forecasting menggunakan data terbatas (14 titik historis), sehingga hasil perlu diinterpretasikan secara hati-hati
