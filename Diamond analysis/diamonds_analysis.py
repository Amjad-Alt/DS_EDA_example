#library
import numpy as np
import pandas as pd 
import math 
import matplotlib.pyplot as plt 
import seaborn as sns 
import statsmodels.api as sm 


#data
jems = pd.read_csv('data/diamonds.csv')
#%%
# explore the data
jems.head()
jems.tail()
jems.info()
jems.sample()
#%%
#how many clarity of catiogary IF
len(jems[jems.clarity == 'IF'])
#%%
#proportion of the total 
len(jems[jems.clarity == 'IF'])/len(jems)
#%%
#the cheapest diamond
min(jems.price)
# %%
#range of diamond price
def getRange(l):
    low =min(l)
    high =max(l)
    return low,high

low, high = getRange(jems.price)

#%%
#mean in each catagory

jems.groupby(['cut','color'])['price'].mean()
# %%
# Plot shows diamond price described by carat
sns.scatterplot(x='carat', y='price',data=jems)

# %%
# log10 transformation to the price
jems['price_log10']=np.log10(jems.price)
# %%
#log10 transformation to the carat
jems['carat_log10']=np.log10(jems.carat)
# %%
#plot with the new values
sns.scatterplot(x='carat_log10', y='price_log10',data=jems)
# %%
#linear model
sns.lmplot(x="price_log10", y="carat_log10", data=jems,  line_kws={"color":"r","alpha":0.7,"lw":5})
plt.title("linear model")
