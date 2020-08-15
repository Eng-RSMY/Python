#!/usr/bin/env python
# coding: utf-8

# In[192]:


# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# data input
n_groups = 16
percent_ir = (0.410952704,0.327795041,0.347090044,0.492881577,0.486983795,0.391465854,0.44630815,0.362072343,0.367450303,0.456664548,0.462270765,0.360664399,0.446189949,0.438397144,0.458136068,0.468936573)
percent_fb = (0.503236026,0.47212886,0.372742801,0.416387034,0.433176512,0.508492872,0.436381063,0.58850222,0.570629739,0.505368369,0.510940556,0.614305056,0.523596897,0.527007792,0.50268107,0.479990542)
percent_eb = (0.005793166,0.007356205,0.009272816,0.005082261,0.007178951,0.013334603,0.013487146,0.011752416,0.0097491,0.01207883,0.016899745,0.018128983,0.028420572,0.030421461,0.035677853,0.046107466)
percent_dv = (0,0,0.000152513,9.77358E-05,0,9.52472E-05,0,0,0.000117106,0,0.000147596,9.90655E-05,0,0,0.000104627,8.86682E-05)
percent_ar = (0.070694727,0.089764728,0.177464617,0.059683988,0.061613522,0.076324729,0.086776435,0.033690259,0.049858009,0.021897295,0.007896388,0.005118383,0,0.00277436,0.001909445,0.001714252)
percent_ot = (0.009323376,0.102955165,0.093277208,0.025867405,0.011047221,0.010286694,0.017047205,0.003982763,0.002195743,0.003990959,0.00184495,0.001684113,0.001792582,0.001399242,0.001490937,0.003162499)

# create plot
fig, ax = plt.subplots()
bar_width = 20
index = bar_width*12*np.arange(n_groups)
opacity = 1
plt.figure(figsize=(30,8))


# plot the bar for each green card category
rects1 = plt.bar(index - 3*bar_width, 100*np.array(percent_ir), bar_width, align='center',
alpha=opacity,
color='blue',
label='Immediate relatives of U.S. citizens')

rects2 = plt.bar(index - 2*bar_width, 100*np.array(percent_fb), bar_width, align='center',
alpha=opacity,
color='green',
label='Family-sponsored preferences')

rects3 = plt.bar(index - bar_width, 100*np.array(percent_eb), bar_width, align='center',
alpha=opacity,
color='red',
label='Employment-based preferences')

rects4 = plt.bar(index, 100*np.array(percent_dv), bar_width, align='center',
alpha=opacity,
color='brown',
label='Diversity')

rects5 = plt.bar(index + bar_width, 100*np.array(percent_ar), bar_width, align='center',
alpha=opacity,
color='orange',
label='Refugees and asylees')

rects6 = plt.bar(index + 2*bar_width, 100*np.array(percent_ot), bar_width, align='center',
alpha=opacity,
color='black',
label='Others')


#plot the results
matplotlib.rc('font', size= 20)
plt.ylabel('Percentage')
plt.title('Percentage of Each Green Card Type Per Fiscal Year from 2003 to 2018')
plt.xlabel('Fiscal Year')
plt.ylim(0, 70)

plt.xticks(index, (2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018))
plt.legend(bbox_to_anchor=(.5, -.1), loc='upper center', ncol=7)

plt.tight_layout()
#plt.show()


# In[106]:


X = np.arange(16)
print(X)

index = np.arange(n_groups)
print(index)


# In[ ]:




