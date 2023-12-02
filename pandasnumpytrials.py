import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Machine Learning with Python and Scikit-Learn – Full Course
# https://www.youtube.com/watch?v=hDKCxebp88A&ab_channel=freeCodeCamp.org

medical_df = pd.read_csv('medical.csv')

# print(medical_df.info())
# print(medical_df.age.describe())
fig = px.histogram(medical_df,x='age',marginal='box',nbins=47,title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show()