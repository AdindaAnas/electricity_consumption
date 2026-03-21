import pandas as pd
import glob
import os

# ===============================
# PATH CONFIGURATION
# ===============================

RAW_PATH = "data/raw_data/"
OUTPUT_PATH = "data/processed/"

# Provinsi baru hasil pemekaran Papua
PROVINSI_BARU = [
    "PAPUA BARAT DAYA",
    "PAPUA SELATAN",
    "PAPUA TENGAH",
    "PAPUA PEGUNUNGAN"
]

# ===============================
# MERGE PROVINSI PEMEKARAN PAPUA
# ===============================

PAPUA_MAPPING = {
    "PAPUA SELATAN": "PAPUA",
    "PAPUA TENGAH": "PAPUA",
    "PAPUA PEGUNUNGAN": "PAPUA",
    "PAPUA BARAT DAYA": "PAPUA BARAT"
}

def merge_papua_provinces(df, value_column):

    # Rename provinsi hasil pemekaran
    df["provinsi"] = df["provinsi"].replace(PAPUA_MAPPING)

    # Agregasi setelah merge
    df = (
        df
        .groupby(["tahun", "provinsi"], as_index=False)
        .agg({value_column: "sum"})
    )

    return df

# ===============================
# STANDARDISASI NAMA PROVINSI
# ===============================

PROVINCE_MAPPING = {
    "KEPULAUAN BANGKA BELITUNG": "KEP. BANGKA BELITUNG",
    "KEPULAUAN RIAU": "KEP. RIAU"
}

def standardize_province(df):

    df["provinsi"] = df["provinsi"].replace(PROVINCE_MAPPING)

    return df

# ===============================
# CLEAN ELECTRICITY DATA
# ===============================

def clean_listrik(file_path):

    filename = os.path.basename(file_path)
    tahun = int(filename.split("_")[-1].split(".")[0])

    df = pd.read_csv(file_path)

    # Hapus header tambahan
    df = df.iloc[2:].copy()

    # Set nama kolom
    df.columns = ["provinsi", "listrik_gwh"]

    # Drop NaN
    df = df.dropna(subset=["provinsi"])
    
    # Cleaning provinsi
    df["provinsi"] = (
        df["provinsi"]
        .astype(str)
        .str.upper()
        .str.strip()
    )
    # Standardisasi nama provinsi
    df = standardize_province(df)

    # Convert numeric
    df["listrik_gwh"] = (
        pd.to_numeric(df["listrik_gwh"], errors="coerce")
    )

    df["tahun"] = tahun

    df = df[["tahun", "provinsi", "listrik_gwh"]]

    return df


# ===============================
# CLEAN POPULATION DATA
# ===============================

def clean_population(file_path):

    filename = os.path.basename(file_path)
    tahun = int(filename.split("_")[-1].split(".")[0])

    df = pd.read_csv(file_path)

    # Rename kolom
    df = df.rename(columns={
        "Provinsi": "provinsi",
        "Jumlah Penduduk (Ribu)": "population_thousand"
    })

    df = df[["provinsi", "population_thousand"]]

    # Drop NaN
    df = df.dropna(subset=["provinsi"])

    # Clean provinsi
    df["provinsi"] = (
        df["provinsi"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # Standardisasi nama provinsi
    df = standardize_province(df)

    # Convert numeric
    df["population"] = (
        pd.to_numeric(df["population_thousand"], errors="coerce") * 1000
    )

    # Buang baris yang bukan data
    df = df[df["population"].notna()]

    # Hilangkan floating error
    df["population"] = df["population"].round().astype("Int64")

    df["tahun"] = tahun

    df = df[[
        "tahun",
        "provinsi",
        "population"
    ]]

    return df

# ===============================
# CLEAN PDRB DATA
# ===============================

def clean_pdrb(file_path):

    filename = os.path.basename(file_path)
    # tahun = int(filename.split("_")[1].split(".")[0])
    tahun = int(filename.split("_")[-1].split(".")[0])

    df = pd.read_csv(file_path)

    # Rename kolom
    df = df.rename(columns={
        "Provinsi": "provinsi",
        "Produk Domestik Bruto/Produk Domestik Regional Bruto Atas Dasar Harga Berlaku (Rp)": "pdrb_miliar"
    })

    # Ambil kolom penting
    df = df[["provinsi", "pdrb_miliar"]]

    # Hapus baris kosong
    df = df.dropna(subset=["provinsi"])

    # Cleaning provinsi
    df["provinsi"] = (
        df["provinsi"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # Standardisasi nama provinsi
    df = standardize_province(df)

    # Convert numeric
    df["pdrb_miliar"] = (
        pd.to_numeric(df["pdrb_miliar"], errors="coerce")
    )

    # Buang baris yang bukan data (footnote BPS)
    df = df[df["pdrb_miliar"].notna()]

    df["tahun"] = tahun

    df = df[[
        "tahun",
        "provinsi",
        "pdrb_miliar"
    ]]

    return df


# ===============================
# CLEAN POVERTY DATA
# ===============================

def clean_poverty(file_path):

    filename = os.path.basename(file_path)
    # tahun = int(filename.split("_")[2].split(".")[0])
    tahun = int(filename.split("_")[-1].split(".")[0])

    # Skip header BPS
    df = pd.read_csv(file_path, skiprows=5, header=None)

    # Ambil kolom provinsi dan jumlah miskin
    df = df[[0, 7]]

    df.columns = [
        "provinsi",
        "poor_population_thousand"
    ]

    # Hapus baris kosong
    df = df.dropna(subset=["provinsi"])

    # Cleaning provinsi
    df["provinsi"] = (
        df["provinsi"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # Standardisasi nama provinsi
    df = standardize_province(df)

    # Convert numeric (ribu -> orang)
    df["poor_population"] = (
        pd.to_numeric(df["poor_population_thousand"], errors="coerce") * 1000
    )

    # Hilangkan floating point error
    df["poor_population"] = (
        df["poor_population"]
        .round()
        .astype("Int64")
    )

    df["tahun"] = tahun

    df = df[[
        "tahun",
        "provinsi",
        "poor_population"
    ]]

    return df

# ===============================
# MAIN PIPELINE
# ===============================

def main():

    # ===============================
    # ELECTRICITY
    # ===============================

    listrik_files = glob.glob(os.path.join(RAW_PATH, "listrik_*.csv"))

    listrik_df = pd.concat(
        [clean_listrik(file) for file in listrik_files],
        ignore_index=True
    )
    
    listrik_df = merge_papua_provinces(listrik_df, "listrik_gwh")

    listrik_df = listrik_df[
        ~((listrik_df["provinsi"]=="KALIMANTAN UTARA") & (listrik_df["tahun"]<2013))
    ]

    listrik_df = listrik_df.dropna(subset=["listrik_gwh"])

    listrik_df = listrik_df.sort_values(
        ["provinsi", "tahun"]
    ).reset_index(drop=True)

    listrik_df.to_csv(
        OUTPUT_PATH + "listrik_clean.csv",
        index=False
    )


    # ===============================
    # POPULATION
    # ===============================

    population_files = glob.glob(os.path.join(RAW_PATH, "jumlah_penduduk_*.csv"))

    population_df = pd.concat(
        [clean_population(file) for file in population_files],
        ignore_index=True
    )

    population_df = merge_papua_provinces(population_df, "population")

    population_df = population_df.sort_values(
        ["provinsi", "tahun"]
    ).reset_index(drop=True)

    population_df.to_csv(
        OUTPUT_PATH + "population_clean.csv",
        index=False
    )


    # ===============================
    # PDRB
    # ===============================

    pdrb_files = glob.glob(os.path.join(RAW_PATH, "pdrb_*.csv"))

    pdrb_df = pd.concat(
        [clean_pdrb(file) for file in pdrb_files],
        ignore_index=True
    )

    pdrb_df = merge_papua_provinces(pdrb_df, "pdrb_miliar")

    pdrb_df["pdrb_miliar"] = pdrb_df["pdrb_miliar"].round(2)

    pdrb_df = pdrb_df.sort_values(
        ["provinsi", "tahun"]
    ).reset_index(drop=True)

    pdrb_df.to_csv(
        OUTPUT_PATH + "pdrb_clean.csv",
        index=False
    )


    # ===============================
    # POVERTY
    # ===============================

    poverty_files = glob.glob(os.path.join(RAW_PATH, "penduduk_miskin_*.csv"))

    poverty_df = pd.concat(
        [clean_poverty(file) for file in poverty_files],
        ignore_index=True
    )

    poverty_df = merge_papua_provinces(poverty_df, "poor_population")

    poverty_df = poverty_df.sort_values(
        ["provinsi", "tahun"]
    ).reset_index(drop=True)

    poverty_df.to_csv(
        OUTPUT_PATH + "poverty_clean.csv",
        index=False
    )


    # ===============================
    # SUMMARY
    # ===============================

    print("Cleaning selesai")
    print("Files saved in:", OUTPUT_PATH)


if __name__ == "__main__":
    main()