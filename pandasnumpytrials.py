import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

medical_df = pd.read_csv('medical.csv')

# print(medical_df.info())
print(medical_df.describe())