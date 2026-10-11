# 2019-nCoV Early Outbreak Data Analysis & Visualisation

Ye repository COVID-19 (2019-nCoV) ke initial phase (21 January 2020 se 26 January 2020) ka Exploratory Data Analysis (EDA) cover karti hai.

## 📌 Project Overview
- **Dataset**: `2019_nC0v_20200121_20200126 - SUMMARY.csv`
- **Goal**: Initial phase me virus ke spread, confirmed cases, deaths, recovered, aur suspected metrics ka pattern aur distribution visualize karna.

## 🛠️ Key Data Preprocessing Steps
1. **Handling Missing Values**:
   - `Province/State` ke NaN records ko `"National"` label diya gaya.
   - `Confirmed`, `Suspected`, `Recovered`, aur `Deaths` ke missing records ko `0.0` se impute kiya gaya.
2. **Datetime Formatting**:
   - `Date last updated` ko standard datetime format me convert kiya gaya.

## 📊 Visualizations Included
- **Top Affected Countries**: Top 10 countries jisme sabse zyada reports record hui.
- **Outlier Detection**: Boxplots ke zariye high concentration cases ka analysis.
- **Metric Distributions**: Histograms aur KDE plots cases ke distribution dekhne ke liye.
- **Correlation Heatmap**: Metrics ke aapas ke relation ka correlation matrix.

## 🚀 How to Run

1. Repository clone karein:
   ```bash
   git clone [https://github.com/your-username/covid19-early-eda-project.git](https://github.com/your-username/covid19-early-eda-project.git)
   cd covid19-early-eda-project
