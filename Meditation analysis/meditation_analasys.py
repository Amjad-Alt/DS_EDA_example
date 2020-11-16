#the meditation case study

import numpy as np
import pandas as pd
from scipy.stats import sem

# %%
#import data
medi = pd.read_table('Expression.txt')
medi.head()
#%%
medi_melt = pd.melt(medi)
medi_melt
# %%
#tidy format
medi_melt['treatment'], medi_melt['gene'], medi_melt['time'] = medi_melt['variable'].str.split('_').str
# %%
medi_melt.drop('variable', axis=1)
#%%
#calculate statistic
#average the mean of the value
medi_mean = np.mean(medi_melt.value)
#%%
#n of observation in each group
medi_melt.groupby('gene').count()

#%%SEM The standard error of the mean
std_medi= np.std(medi_melt.value, ddof=1) / np.sqrt(np.size(medi_melt.value))
#%%
#CIerror The 95% CI error defined by the t distribution
se_medi = np.sqrt(medi_mean* (1 - medi_mean / len(medi_melt.value)))

#%%
#lower95 The upper 95% CI limit
CI_lower = medi_mean - 1.96 * std_medi

#%%
#upper95 The upper 95% CI limit
CI_upper = medi_mean + 1.96 * std_medi
# %%
