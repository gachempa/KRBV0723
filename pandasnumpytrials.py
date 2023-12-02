
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

from sklearn.linear_model import LinearRegression

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

# print(medical_df.charges.corr(medical_df.age))
# sns.heatmap(medical_df.corr(numeric_only=True),cmap='Reds',annot=True)
# plt.title('Corr Matrix')
# plt.show()

non_smoker_df=medical_df[medical_df.smoker=='no']

# Convert non-nums to numerical
smoker_values = {'no': 0, 'yes': 1}
smoker_numeric = medical_df.smoker.map(smoker_values)
# print(medical_df.charges.corr(smoker_numeric))

model=LinearRegression()

inputs=non_smoker_df[['age']]
targets=non_smoker_df.charges
model.fit(inputs,targets)
# print(model.predict(np.array([[23],[37],[61]])))
predictions=model.predict(inputs)
def rmse(targets,predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))
# print(rmse(targets,predictions))

w=model.coef_
b=model.intercept_

def estimate_charges(age, w, b):
    return w * age + b

def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges
    predictions = estimate_charges(ages, w, b)
    
    plt.plot(ages, predictions, 'r', alpha=0.9)
    plt.show
    plt.scatter(ages, target, s=8,alpha=0.8)
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.legend(['Prediction', 'Actual']);
    plt.show
    
    loss = rmse(target, predictions)
    print("RMSE Loss: ", loss)

try_parameters(w,b)