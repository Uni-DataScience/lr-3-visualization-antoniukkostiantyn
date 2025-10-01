import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of categorical data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    # Count frequency of each category
    counts = collections.Counter(data)

    # Extract categories and their frequencies
    categories = list(counts.keys())
    frequencies = list(counts.values())

    # Create bar chart
    fig, ax = plt.subplots()
    colors = ['skyblue', 'salmon', 'lightgreen']  # distinct colors for bars
    ax.bar(categories, frequencies, color=colors)

    # Add labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Categories')

    # Optional: display values on top of bars
    for i, freq in enumerate(frequencies):
        ax.text(i, freq + 0.5, str(freq), ha='center')

    plt.show()
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
