import numpy as np
import pandas as pd
import plotly.express as px


def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Create scatter plot
    fig = px.scatter(
        df,
        x='x',
        y='y',
        color='y',  # optional: color points based on y value
        size='y',  # optional: scale marker size by y value
        hover_data={'x': True, 'y': True},  # show x and y on hover
        labels={'x': 'X Axis', 'y': 'Y Axis'},  # axis labels
        title='Interactive Scatter Plot with Plotly'
    )

    # Show plot in web environment
    fig.show()
    return fig


# Example data
df = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})

create_interactive_plotly(df)
