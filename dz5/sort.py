import pandas as pd
import numpy as np

df = pd.read_csv("tested.csv")
print(df.isnull().sum())
print(df.dtypes)
pd.set_option('display.width', None)
print(df.head(12))
print(df.describe())
print(len(df))
print(len(df.columns))
print("Процент выживших мужчин и женщин:")
print((df.groupby("Sex")["Survived"].sum() / df.groupby("Sex")["Survived"].count() * 100).round(2))
print((df.groupby("Sex")["Age"].sum() / df.groupby("Sex")["Age"].count()).round(2))
age = df['Age'].values
sex = df['Sex'].values
pclass=df["Pclass"].values
survived = df['Survived'].values

mask = (sex == 'female') & (survived == 1)
if mask.any():
    mean_age = np.nanmean(age[mask])
    print(f"Выжившие женщины: {mean_age:.1f} лет")

mask = (sex == 'female') & (survived == 0)
if mask.any():
    mean_age = np.nanmean(age[mask])
    print(f"Умершие женщины: {mean_age:.1f} лет")

mask = (sex == 'male') & (survived == 1)
if mask.any():
    mean_age = np.nanmean(age[mask])
    print(f"Выжившие мужчины: {mean_age:.1f} лет")

mask = (sex == 'male') & (survived == 0)
if mask.any():
    mean_age = np.nanmean(age[mask])
    print(f"Умершие мужчины: {mean_age:.1f} лет")

mask = (age > 30) & (sex == 'male') & (pclass == 1)
if mask.any():
    print(df[mask])
mask = ((age <18) | (sex == 'female')) & (survived == 1)
if mask.any():
    print(df[mask])