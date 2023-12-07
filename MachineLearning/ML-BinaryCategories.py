# check data-retreive.py and pandasnumpytrials.py for some basics
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

# settign default style for charts
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

medical_df = pd.read_csv('medical.csv')

non_smoker_df=medical_df[medical_df.smoker=='no']

# Convert non-nums to numerical
smoker_values = {'no': 0, 'yes': 1}
smoker_numeric = medical_df.smoker.map(smoker_values)
# print(medical_df.charges.corr(smoker_numeric))
medical_df['smoker_code']=smoker_numeric

sex_codes = {'female': 0, 'male': 1}
medical_df['sex_code'] = medical_df.sex.map(sex_codes)

enc=preprocessing.OneHotEncoder()
enc.fit(medical_df[['region']])
enc.categories_
print(enc.categories_)
one_hot=enc.transform(medical_df[['region']]).toarray()

medical_df[['northeast', 'northwest', 'southeast', 'southwest']] = one_hot

# print(medical_df)

model=LinearRegression()

# inputs=non_smoker_df[['age','bmi','children']]
# targets=non_smoker_df.charges
inputs=medical_df[['age','bmi','children','smoker_code','sex_code', 
                   'northeast', 'northwest', 'southeast', 'southwest']]
targets=medical_df.charges
model=model.fit(inputs,targets)
print("coeff:",model.coef_)
print("intcpt:",model.intercept_)

# print(model.predict(np.array([[23],[37],[61]])))
predictions=model.predict(inputs)
def rmse(targets,predictions):
    return np.sqrt(np.mean(np.square(targets - predictions)))
# print(rmse(targets,predictions))
print("rmse loss =",rmse(targets,predictions))

sns.barplot(data=medical_df,x='region',y='charges')
plt.show()

# fig = px.scatter_3d(non_smoker_df, x='age', y='bmi', z='charges')
# fig.update_traces(marker_size=3, marker_opacity=0.5)
# fig.show()

