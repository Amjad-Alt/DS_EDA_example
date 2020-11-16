#title:
 "Chick Weight Analysis"
#author: 
  "Amjad Altuwayjiri"

import math 

import pandas as pd 
import numpy as np 
import seaborn as sns 
import statsmodels.api as sm 

from scipy import stats
from statsmodels.formula.api import ols
#%%
chickwts = pd.read_csv('data/Chick Weights.txt')

#Gitting to know the data 
chickwts.info()
chickwts.shape
chickwts.columns
chickwts.describe()
#%%
#Calculate the number of chickens in each groupe
chickwts.groupby(['feed']).value_counts()
#%%
## Descriptive Statisticst.

'''This study shows the effect of the type of food on the chicken wight.
 The type of food has been tested are:casein, horsebean, linseed, meatmeal, soybean and sunflower.'''

length = chickwts.groupby('feed').len()
avrage = chickwts.groupby('feed')['weight'].mean()
SD = chickwts.groupby('feed')['weight'].std()
chickwts_df = pd.concat([length, avrage, SD], axis=1)

print(chickwts_df)
#%%
## Plots

sns.pointplot(x="feed", y="weight", data=chickwts, join=False)

sns.boxplot(x="feed", y="weight", data=chickwts)
#%%
## Inferential Statistics

chickwts_lm = ols("weight ~ feed", data=chickwts)
results = chickwts.fit()
results.summary()

#%%
#1- way anova
aov_table = sm.stats.anova_lm(results, typ=2)

# explore anova results
print(aov_table)
