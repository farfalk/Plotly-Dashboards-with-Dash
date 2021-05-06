#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:

from matplotlib.axis import XAxis
import plotly.offline as pyo
import plotly.graph_objects as go
import numpy as np

# Define a data variable

x: np.ndarray = np.random.randn(1000)
y: np.ndarray = np.random.rand(1000)

data: list = [ go.Scatter(x=x, y=y, mode="markers") ]


# Define the layout

layout: go.Layout = go.Layout(  title="Exercise 1",
                                xaxis={ "title": "x) normal distribution" },
                                yaxis={ "title": "y) uniform distribution" },
                                hovermode="closest"
                                )


# Create a fig from data and layout, and plot the fig

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="1-02E-ScatterplotExercises/my_solution1.html")