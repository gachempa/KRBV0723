
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

from sklearn.linear_model import LinearRegression
# check data-retreive.py and pandasnumpytrials.py for some basics

medical_df = pd.read_csv('medical.csv')

non_smoker_df=medical_df[medical_df.smoker=='no']

# Convert non-nums to numerical
smoker_values = {'no': 0, 'yes': 1}
smoker_numeric = medical_df.smoker.map(smoker_values)
# print(medical_df.charges.corr(smoker_numeric))

model=LinearRegression()

inputs=non_smoker_df[['age']]
targets=non_smoker_df.charges
model.fit(inputs,targets)
print("coeff:",model.coef_)
print("intcpt:",model.intercept_)

# print(model.predict(np.array([[23],[37],[61]])))
predictions=model.predict(inputs)
def rmse(targets,predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))
# print(rmse(targets,predictions))
rmse(targets,predictions)

w=model.coef_
b=model.intercept_

def estimate_charges(age, w, b):
    return w * age + b

def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges
    predictions = estimate_charges(ages, w, b)
    
    plt.plot(ages, predictions, 'r', alpha=0.9)
    plt.scatter(ages, target, s=8,alpha=0.8)
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.legend(['Prediction', 'Actual'])
    plt.show()
    
    loss = rmse(target, predictions)
    print("RMSE Loss: ", loss)
    # print(input("Chart Ok? Press any key to continue"))

try_parameters(w,b)