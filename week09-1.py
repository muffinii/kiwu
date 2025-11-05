import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
# print(df.info())
# print(df.describe())
# print(df.tail())
# print(df['body_mass_g'].describe())
# print(df[df["body_mass_g"] >= 55.0])
print(df[df['bill_length_mm'] >= 55.0])
# plt.plot()
# plt.show()