#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:

import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd


# Create a pandas DataFrame from 2010YumaAZ.csv
df: pd.DataFrame = pd.read_csv('data/2010YumaAZ.csv')
days: list = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# Use a for loop (or list comprehension to create traces for the data list)
data: list = [  go.Scatter(  x=df.loc[df['DAY']==day]['LST_TIME'],
                            y=df.loc[df['DAY']==day]['T_HR_AVG'],
                            mode='markers+lines',
                            name=day)
                for day in days]

# Define the layout

layout: go.Layout = go.Layout(title = 'Temperature data (2010 data, Yuma AZ)')

# Create a fig from data and layout, and plot the fig

fig: go.Figure = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='1-03E-LineChartExercises/my_solution.html')