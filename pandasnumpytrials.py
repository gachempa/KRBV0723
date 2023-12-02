
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

# Machine Learning with Python and Scikit-Learn – Full Course
# https://www.youtube.com/watch?v=hDKCxebp88A&ab_channel=freeCodeCamp.org
# check data-retreive.py for commands to get data file 

medical_df = pd.read_csv('medical.csv')

# print(medical_df.info())
# print(medical_df.age.describe())
# basic commands to plot a graph
# fig = px.histogram(medical_df,x='age',marginal='box',nbins=47,title='Distribution of Age')
# fig.update_layout(bargap=0.1)
# fig.show()

# fig = px.scatter(medical_df,x='bmi',y='charges',color='smoker',
#                  opacity=0.5,hover_data=['sex'],title='BMI vs. Charges')
# fig=px.violin(medical_df,x='children',y='charges')
# fig.update_traces(marker_size=5)
# fig.show()

print(medical_df.charges.corr(medical_df.age))
print(medical_df.corr(numeric_only=True))

# Convert non-nums to numerical
smoker_values = {'no': 0, 'yes': 1}
smoker_numeric = medical_df.smoker.map(smoker_values)
# print(medical_df.charges.corr(smoker_numeric))

# fig=sns.heatmap(medical_df.corr(),cmap='Reds',annot=True)
# plt.title('Correlation Matrix')

# px.histogram(medical_df,x='smoker',color='sex',title='Smoker')

# non_smoker_df = medical_df[medical_df.smoker == 'no']

# loss in linear regression for ML
# def try_parameters(w,b):
#     ages = non
# fig = px.histogram(medical_df,x='age',marginal='box',nbins=47,title='Distribution of Age')
# fig.update_layout(bargap=0.1)
# fig.show()