# 🦠 2019-nCoV Early Outbreak Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-green.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

An exploratory data analysis (EDA) pipeline analyzing the initial trajectory of the novel coronavirus (2019-nCoV / COVID-19) outbreak using global summary records from **January 21, 2020, to January 26, 2020**.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Summary](#-dataset-summary)
- [Project Structure](#-project-structure)
- [Data Preprocessing](#-data-preprocessing)
- [Key Visualizations](#-key-visualizations)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [License](#-license)

---

## 📖 Project Overview

In late January 2020, reports of a novel coronavirus began surfacing globally. This project analyzes the earliest structured dataset tracking the epidemic to uncover:
- Regional reporting patterns across affected countries.
- Statistical distribution of confirmed cases, suspected cases, recoveries, and fatalities.
- Outlier identification across geographic jurisdictions.
- Cross-metric correlations during the initial phase of the outbreak.

---

## 📂 Dataset Summary

- **Source File**: `data/2019_nC0v_20200121_20200126 - SUMMARY.csv`
- **Observation Window**: January 21, 2020 – January 26, 2020
- **Primary Attributes**:
  - `Province/State`: Administrative division or region of report.
  - `Country`: Sovereign state or territory.
  - `Date last updated`: Timestamp of the official report update.
  - `Confirmed`: Number of confirmed positive cases.
  - `Suspected`: Number of suspected cases undergoing verification.
  - `Recovered`: Number of discharged/recovered individuals.
  - `Deaths`: Cumulative fatal outcomes recorded.

---

## 🗂️ Project Structure

```text
covid19-early-eda-project/
│
├── data/
│   └── 2019_nC0v_20200121_20200126 - SUMMARY.csv   # Raw dataset
│
├── outputs/                                         # Generated figures
│   ├── top_countries.png
│   ├── boxplots.png
│   ├── distribution_plots.png
│   └── correlation_heatmap.png
│
├── main.py                                          # Modular EDA execution script
├── covid_19_EDA.ipynb                               # Interactive Jupyter Notebook
├── requirements.txt                                 # Project dependencies
├── .gitignore                                       # Files excluded from git tracking
└── README.md                                        # Project documentation
