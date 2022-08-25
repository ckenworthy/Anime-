#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages


# In[2]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ttest_ind


# In[3]:


#load  data


# In[4]:


anime=pd.read_csv(r"C:\Users\camke\Downloads\anime (3)\anime.csv")


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


## playing around with bang (!) symbol


# In[9]:


#! dir

## shows me which directory I am working in


# In[10]:


get_ipython().system(' ping google.com')

## just pings the outside site of google


# In[11]:


get_ipython().system(' dir ..')

## goes back 1 directory from the one I am working


# In[12]:


get_ipython().system(' dir ..\\..')

## goes back 2 directories from where I am working


# In[13]:


## back to coursework


# In[14]:


anime.head()


# Is a Rating Score of 6.2 Different from the Mean in this Dataset?# 

# In[15]:


anime.score.hist()


# In[16]:


anime.score.mean()


# ## Does Anime that is Still Airing Differ in Popularity from Anime that is No Longer Airing?

# In[17]:


anime.status.unique()


# # check for assumptions for Finished Airing and Currently Airing

# In[18]:


anime.popularity[anime.status == 'Finished Airing'].hist()
## histogram of anime popularity after if finishes its original run


# looks like popularity goes down after an anime has finished producing episodes

# In[19]:


anime.popularity[anime.status == 'Currently Airing'].hist()
## histogram of anime popularity that is in its original run


# In[20]:


## looks like popularity is up and down during an anime's original air


# 
# ## run an independent t-test

# In[21]:


ttest_ind(anime.popularity[anime.status == 'Currently Airing'], anime.popularity[anime.status == 'Finished Airing'])


# ## there appears to be a significant difference

# ### look at the means

# In[22]:


anime.popularity[anime.status == 'Currently Airing'].mean()


# In[23]:


anime.popularity[anime.status == 'Finished Airing'].mean()


# ### anime that is currently airing is way more popular than anime that is finished airing

# # Does the Source of the Anime Influence the Type of Anime?

# In[27]:


anime.source.unique()


# # create contingency table

# In[31]:


crosstab = pd.crosstab(anime['source'], anime['type'])


# In[32]:


crosstab


# In[33]:


stats.chi2_contingency(crosstab)


# In[34]:


## we can see that the source does influence the type


# # How do the Variables about Popularity / Ranking Relate to Each Other?

# In[35]:


## make a df of the variables we are examing


# In[36]:


anime3 = anime[['score', 'scored_by', 'rank', 'popularity', 'members', 'favorites']]


# In[37]:


anime3.head()


# correlation matrix

# In[38]:


anime3.corr(method='pearson')


# enhance interpretaion and visuals

# In[39]:


anime3.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)
## coolwarm palette


# In[40]:


anime3.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('viridis'), axis=1)
## viridis palette


# In[41]:


## members and scored_by are positively correlated
## favorites and scored_by are positively correlated
## favorites and members are positively correlated
## these 3 variables seem to be all related
## interesting note popularity and scored_by are not correlated


# In[ ]:




