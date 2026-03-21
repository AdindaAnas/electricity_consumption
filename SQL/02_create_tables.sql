-- ======= ELECTRICITY BASE TABLE ===========

CREATE TABLE electricity_consumption (
    tahun INT NOT NULL,
    provinsi VARCHAR(100) NOT NULL,
    listrik_gwh FLOAT NOT NULL,

    PRIMARY KEY (tahun, provinsi)
);

-- Load dari CSV hasil cleaning
COPY electricity_consumption
FROM 'D:\Data_analyst\electricity_consumption\data\processed\listrik_clean.csv'
DELIMITER ','
CSV HEADER;

-- =========== POPULATION TABLE ============

CREATE TABLE population (
    tahun INT NOT NULL,
    provinsi VARCHAR(100) NOT NULL,
    population BIGINT NOT NULL,

    PRIMARY KEY (tahun, provinsi)
);

-- Load dari CSV hasil cleaning
COPY population
FROM 'D:\Data_analyst\electricity_consumption\data\processed\population_clean.csv'
DELIMITER ','
CSV HEADER;

-- ============== PDRB TABLE =============

CREATE TABLE pdrb (
    tahun INT NOT NULL,
    provinsi VARCHAR(100) NOT NULL,
    pdrb_miliar FLOAT NOT NULL,

    PRIMARY KEY (tahun, provinsi)
);

-- Load dari CSV hasil cleaning
COPY pdrb
FROM 'D:\Data_analyst\electricity_consumption\data\processed\pdrb_clean.csv'
DELIMITER ','
CSV HEADER;

-- ============ POVERTY TABLE ==============

CREATE TABLE poverty (
    tahun INT NOT NULL,
    provinsi VARCHAR(100) NOT NULL,
    poor_population BIGINT NOT NULL,

    PRIMARY KEY (tahun, provinsi)
);

-- Load dari CSV hasil cleaning
COPY poverty
FROM 'D:\Data_analyst\electricity_consumption\data\processed\poverty_clean.csv'
DELIMITER ','
CSV HEADER;

-- ======== FEATURE ENGINEERING TABLE ========
-- SOCIOECONOMIC + FEATURES

CREATE TABLE electricity_features AS
SELECT
    e.tahun,
    e.provinsi,
    e.listrik_gwh,
    p.population,
    d.pdrb_miliar,
    po.poor_population,

    -- Feature Engineering
    (e.listrik_gwh * 1000000.0 / p.population) AS electricity_per_capita,
    (e.listrik_gwh / d.pdrb_miliar) AS electricity_intensity,
    (po.poor_population * 1.0 / p.population) AS poverty_rate,
    (d.pdrb_miliar * 1000000000.0 / p.population) AS pdrb_per_capita

FROM electricity_consumption e
LEFT JOIN population p
    ON e.tahun = p.tahun AND e.provinsi = p.provinsi
LEFT JOIN pdrb d
    ON e.tahun = d.tahun AND e.provinsi = d.provinsi
LEFT JOIN poverty po
    ON e.tahun = po.tahun AND e.provinsi = po.provinsi

-- hanya ambil periode lengkap
WHERE e.tahun >= 2017
AND e.provinsi != 'INDONESIA';

-- ============= FORECAST TABLE =============
CREATE TABLE electricity_forecast (
    tahun INT PRIMARY KEY,
    listrik_gwh FLOAT NOT NULL
);

COPY electricity_forecast
FROM 'D:\Data_analyst\electricity_consumption\data\processed\forecast.csv'
DELIMITER ','
CSV HEADER;

-- ======= COMBINED (ACTUAL + FORECAST) =========
CREATE TABLE electricity_actual_vs_forecast AS
SELECT
    tahun,
    listrik_gwh,
    'Actual' AS type
FROM electricity_consumption
WHERE provinsi = 'INDONESIA'

UNION ALL

SELECT
    tahun,
    listrik_gwh,
    'Forecast' AS type
FROM electricity_forecast;