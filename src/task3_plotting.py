import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Needed for 3D plotting

# 1D Line Plot
def plot_1d(data):
    """
    Plots a 1D sequence of values as a line plot.
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(data, marker='o', linestyle='-', color='blue')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('1D Line Plot')
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    return fig

# 2D Scatter Plot
def plot_2d(x, y):
    """
    Plots a 2D scatter plot showing the relationship between two variables.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y, color='green', s=50, alpha=0.7)
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('2D Scatter Plot')
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    return fig

# 3D Scatter Plot
def plot_3d(x, y, z):
    """
    Plots a 3D scatter plot representing three-dimensional data points.
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='red', s=50, alpha=0.7)
    ax.set_xlabel('X Dimension')
    ax.set_ylabel('Y Dimension')
    ax.set_zlabel('Z Dimension')
    ax.set_title('3D Scatter Plot')
    plt.tight_layout()
    plt.show()
    return fig

# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Create the plots
plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
