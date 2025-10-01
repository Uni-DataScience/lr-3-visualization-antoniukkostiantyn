import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Use Seaborn's clean style for clarity and readability
    sns.set_style("whitegrid")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=data, x='x', y='y', ax=ax, color='teal', s=60)

    # Add labels and title
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('Scatter Plot of X vs Y', fontsize=14)

    # Optional: show grid for easier interpretation
    ax.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

    return fig


# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})

create_scatter_plot(data)
