# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:27:44 2022

@author: Sunshine
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#dataset_url = 'https://www.kaggle.com/crawford/80-cereals'
df = pd.read_csv("C:/Users/Sunshine/Desktop/CEM/Continued_Education/Python/Data/cereal.csv")
print(df.head(20))
print(df.info())
print(df.columns)

corr = df.corr()
sns.heatmap(corr)

#how do certain nutrients affect the rating?
sns.lmplot(x='rating', y='calories', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='protein', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='fat', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='sodium', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='fiber', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='carbo', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='sugars', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='potass', data=df, truncate=True)
plt.show()
sns.lmplot(x='rating', y='vitamins', data=df, truncate=True)
plt.show()

#who has the highest ratings?
df_rating_sorted = df.sort_values('rating', ascending=False)
print(df_rating_sorted[['name', 'rating']].head(10))

#brand ratings
avg_rating = df.groupby('mfr')['rating'].mean()
avg_rating.plot(kind='bar')
plt.title('Ratings of Brands')
plt.ylabel('Average Rating')
plt.xlabel('Brand')
plt.show()

#which cereal has the least amount of sugar
df_rating_sorted = df.sort_values('sugars', ascending=True)
print(df_rating_sorted[['name', 'sugars']].head(10))

#which cereal has the greatest amont of protein
df_rating_sorted = df.sort_values('protein', ascending=False)
print(df_rating_sorted[['name', 'protein']].head(10))

#how many hot and cold? 
print(df['name'][df['type'] == 'C'].count())
print(df['name'][df['type'] == 'H'].count())
#who makes the hot and whats the name?
print(df[['name', 'mfr']][df['type'] == 'H'])

#lets see where cereals are located on the shelves
df.groupby('mfr').describe().unstack()

cat_df = pd.DataFrame({'name': df['name'], 
                        'mfr': df['mfr'], 
                       'shelf': df['shelf']}, 
                       columns = ['name','mfr', 'shelf'])
mfr_shelf_df2 = cat_df.groupby(['mfr','shelf'])['name'].aggregate('count').unstack()
mfr_shelf_df3 = mfr_shelf_df2.fillna(0)
fig, ax = plt.subplots(figsize=(10, 5))
mfr_shelf_df3.plot(kind='bar', ax=ax, stacked='True', grid=False)
ax.set(xlabel='Manufacturer' , ylabel = 'Frequency',title='Number of cereals on each shelf (by manufacturer type')


#comparing the nutrients with hot cereal vs cold cereal 
hotCereals = df[['calories','protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins']][df["type"] == "H"]
coldCereals = df[['calories','protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins']][df["type"] == "C"]
nutrient_type_df = df.groupby('type')[['calories','protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins']].mean().fillna(0)
nutrient_type_df.plot(kind='bar', stacked=True)
plt.title('Comparison of Nutrients in Cold vs Hot Cereal')
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.xticks(rotation=0, ha='center')
plt.ylabel('Frequency')
plt.xlabel('Nutrients')


