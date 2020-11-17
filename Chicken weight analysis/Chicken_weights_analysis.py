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
chicken_weights = pd.read_table("data/Chick Weights.txt")
#Gitting to know the data 
chicken_weights.info()
chicken_weights.shape
chicken_weights.columns
chicken_weights.describe()
#%%
#Calculate the number of chickens in each groupe
chicken_weights['feed'].value_counts()
#%%
## Descriptive Statisticst.
'''This study shows the effect of the type of food on the chicken wight.
 The type of food has been tested are:casein, horsebean, linseed, meatmeal, soybean and sunflower.'''
#%%
#calculate the mean and standerd diveation 
chickwts_df = chicken_weights.groupby(['feed']).agg({'weight':['mean','std']})

print(chickwts_df)
#%%
## Plots shows the mean of the weights of each type of feed

sns.pointplot(x="feed", y="weight", data=chicken_weights, join=False)

sns.boxplot(x="feed", y="weight", data=chicken_weights)
#%%
## Inferential Statistics

model = ols("weight ~ feed", data=chicken_weights)
results = chicken_weights.fit()
results.summary()

#%%
#1- way anova
aov_table = sm.stats.anova_lm(results, typ=2)
print(aov_table)
