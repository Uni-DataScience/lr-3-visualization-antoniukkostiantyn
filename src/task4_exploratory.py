import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    print("===== Descriptive Statistics =====")
    descriptive_stats = df.describe().T  # transpose for readability
    descriptive_stats['median'] = df.median()
    descriptive_stats['mode'] = df.mode().iloc[0]  # first mode if multiple
    descriptive_stats['variance'] = df.var()
    print(descriptive_stats)

    print("\n===== Outlier Detection (Boxplots) =====")
    # Boxplots for each column
    fig, axes = plt.subplots(1, len(df.columns), figsize=(5 * len(df.columns), 5))
    if len(df.columns) == 1:
        axes = [axes]  # make it iterable if only one column
    for i, col in enumerate(df.columns):
        sns.boxplot(y=df[col], ax=axes[i], color='skyblue')
        axes[i].set_title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

    print("\n===== Correlation Analysis =====")
    corr_matrix = df.corr()
    print(corr_matrix)

    # Heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title('Correlation Matrix Heatmap')
    plt.show()

    # Insights summary
    print("\n===== Insights =====")
    for col in df.columns:
        # Check for extreme outliers using z-score > 3
        outliers = df[np.abs(stats.zscore(df[col])) > 3]
        print(f"{col}: {len(outliers)} potential outlier(s)")

    print("\nCorrelation insights:")
    high_corr = corr_matrix[(corr_matrix.abs() > 0.7) & (corr_matrix.abs() < 1)]
    if not high_corr.empty:
        print("High correlations detected between variables:")
        print(high_corr.dropna(how='all', axis=0).dropna(how='all', axis=1))
    else:
        print("No very strong correlations detected.")


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})

perform_eda(df)
