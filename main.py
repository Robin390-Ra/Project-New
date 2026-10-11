import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_preprocess_data(file_path: str) -> pd.DataFrame:
    """
    Loads raw outbreak data, handles missing values,
    and standardizes date formats.
    """
    df = pd.read_csv(file_path)
    print(f"Dataset successfully loaded. Shape: {df.shape}")

    # Impute missing state/province records
    df['Province/State'] = df['Province/State'].fillna('National')

    # Impute numerical columns with zero
    numeric_columns = ['Confirmed', 'Suspected', 'Recovered', 'Deaths']
    df[numeric_columns] = df[numeric_columns].fillna(0.0)

    # Parse date column using mixed format handling
    df['Date last updated'] = pd.to_datetime(
        df['Date last updated'], format='mixed', errors='coerce'
    )

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    return df


def generate_visualizations(df: pd.DataFrame, output_dir: str = 'outputs') -> None:
    """
    Generates and saves exploratory analysis charts to the specified directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style='whitegrid')

    # 1. Bar Chart: Top 10 Countries by Record Count
    plt.figure(figsize=(9, 5))
    top_countries = df['Country'].value_counts().head(10).index
    sns.countplot(
        data=df[df['Country'].isin(top_countries)],
        y='Country',
        order=top_countries,
        palette='viridis',
        hue='Country',
        legend=False
    )
    plt.title('Number of Records per Country (Top 10)', fontsize=14, weight='bold')
    plt.xlabel('Record Count')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_countries.png'), dpi=300)
    plt.close()
    print("Saved: top_countries.png")

    # 2. Boxplots: Distribution and Outlier Detection
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    sns.boxplot(y=df['Confirmed'], ax=axes[0, 0], color='skyblue')
    axes[0, 0].set_title('Confirmed Cases', weight='bold')

    sns.boxplot(y=df['Deaths'], ax=axes[0, 1], color='salmon')
    axes[0, 1].set_title('Deaths', weight='bold')

    sns.boxplot(y=df['Recovered'], ax=axes[1, 0], color='lightgreen')
    axes[1, 0].set_title('Recovered Cases', weight='bold')

    sns.boxplot(y=df['Suspected'], ax=axes[1, 1], color='gold')
    axes[1, 1].set_title('Suspected Cases', weight='bold')

    plt.suptitle('Outlier Detection Across Key Metrics', fontsize=16, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'boxplots.png'), dpi=300)
    plt.close()
    print("Saved: boxplots.png")

    # 3. Histograms with KDE: Case Distributions
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    sns.histplot(df['Confirmed'], kde=True, ax=axes[0, 0], color='red')
    axes[0, 0].set_title('Confirmed Distribution', weight='bold')

    sns.histplot(df['Deaths'], kde=True, ax=axes[0, 1], color='black')
    axes[0, 1].set_title('Deaths Distribution', weight='bold')

    sns.histplot(df['Recovered'], kde=True, ax=axes[1, 0], color='green')
    axes[1, 0].set_title('Recovered Distribution', weight='bold')

    sns.histplot(df['Suspected'], kde=True, ax=axes[1, 1], color='orange')
    axes[1, 1].set_title('Suspected Distribution', weight='bold')

    plt.suptitle('Distribution of Case Metrics', fontsize=16, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'distribution_plots.png'), dpi=300)
    plt.close()
    print("Saved: distribution_plots.png")

    # 4. Correlation Heatmap
    plt.figure(figsize=(7, 6))
    correlation_matrix = df[['Confirmed', 'Suspected', 'Recovered', 'Deaths']].corr()
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap='coolwarm',
        fmt='.2f',
        linewidths=0.5
    )
    plt.title('Correlation Heatmap', fontsize=14, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'), dpi=300)
    plt.close()
    print("Saved: correlation_heatmap.png")


def main():
    # Primary and fallback dataset locations
    data_path = os.path.join('data', '2019_nC0v_20200121_20200126 - SUMMARY.csv')
    if not os.path.exists(data_path):
        data_path = '2019_nC0v_20200121_20200126 - SUMMARY.csv'

    cleaned_df = load_and_preprocess_data(data_path)
    generate_visualizations(cleaned_df)
    print("\nEDA pipeline execution finished successfully.")


if __name__ == '__main__':
    main()
