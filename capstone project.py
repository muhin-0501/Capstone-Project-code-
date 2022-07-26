#!/usr/bin/env python
# coding: utf-8

# # Project Objective
# 
#   The dataset contains data on mobile phones that have been released . The data set includes many features of the phone. It also includes the financial features of the phones. We will reach some results by analyzing and visualizing this data. I hope it helps to all.

# # 

# # Setup
# 
# Let's start our analysis by Importing and uploading the data set

# In[65]:


import numpy as np 
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 
import matplotlib.pyplot as plt, seaborn as sns, plotly.express as px, plotly.figure_factory as ff


# # Importing the dataset

# In[66]:


df=pd.read_csv("phones_data_m.csv")


# In[67]:


df


# # 

# 
# # Analysis the Dataset

# # 

# In[68]:


df.info()


# In[69]:


df.dtypes


# In[70]:


df.shape


# In[71]:


df.columns


# # 

# # Missing Data
# 
#   Checking the missing values in the data set?

# In[72]:


df.isnull().values.any()


# In[73]:


df.isna().sum().sort_values(ascending=False)


# In[74]:


df.lowest_price.mode()[0]
df.lowest_price.fillna(df.lowest_price.mode()[0],inplace=True)
df.highest_price.mode()[0]
df.highest_price.fillna(df.highest_price.mode()[0],inplace=True)
df.os.mode()[0]
df.os.fillna(df.os.mode()[0],inplace=True)
df.memory_size.mode()[0]
df.memory_size.fillna(df.memory_size.mode()[0],inplace=True)
df.battery_size.mode()[0]
df.battery_size.fillna(df.battery_size.mode()[0],inplace=True)
df.screen_size.mode()[0]
df.screen_size.fillna(df.screen_size.mode()[0],inplace=True)
df.isna().sum()


# # 

# # Exploratory Data Analysis[EDA]
# 

# In[39]:


fig=df.hist(figsize=(20,20),color='#add8e6')
plt.show()


# # Bar Chart
# 
# 
#  Bar graphs are used to compare things between different groups or to track changes over time. In this Bar graphs showing tha average lowest price by phone brands and average highest price by phone brands

# In[40]:


plt.figure(figsize=(10,6))
plt.title("Average lowest price by phone brands")
sns.barplot(x=df.index, y=df['lowest_price'])
plt.ylabel("lowest_price ")


# In[41]:


plt.figure(figsize=(10,6))
plt.title("Average highest price by phone brands")
sns.barplot(x=df.index, y=df['highest_price'])
plt.ylabel("highest_price ")


# # 

# # Scatter Plots
# 
# 
# In a scatter plot, the values of 2 variables are plotted as points on a 2-dimensional grid. 

# In[59]:


sns.scatterplot(x=df['best_price'],
               y=df['screen_size'])


# In[43]:


sns.regplot(x=df['sellers_amount'],
               y=df['best_price'])


# # 

# #   Line Chart
# 
# 
# Line graphs are used to track changes over short and long periods of time. When smaller changes exist, line graphs are better to use than bar graphs. Line graphs can also be used to compare changes over the same period of time for more than one group

# In[44]:


plt.figure(figsize=(16,6))
sns.lineplot(data=df)


# In[45]:


plt.figure(figsize=(14,6))
plt.title("Battery power by products")
sns.lineplot(data=df['battery_size'], label="Battery Size")


# In[46]:


plt.figure(figsize=(14,6))
plt.title("Price of the Product")
sns.lineplot(data=df['lowest_price'], label="Lowest Price")
sns.lineplot(data=df['highest_price'], label= "Highest price")
sns.lineplot(data=df['best_price'], label= "Best price")


# # 

# # When most of the phones were released? 

# In[47]:


df = df.copy(True)
df['release_date'].value_counts(normalize=True).sort_values(ascending=False)


# In[48]:


df['release_date'].value_counts()
df['release_date'].hist()
plt.xlabel('Year')
plt.ylabel('Number of releases')
plt.show()


# # 

# # Which brands are popular? 

# In[56]:


df1 = df.copy(True)
df1 = df.groupby('brand_name').count()
df1 = df1.sort_values('model_name', ascending=False)


# In[58]:


px.bar(x = df1.index, y = df1.model_name, color_discrete_sequence=['orange'], 
       labels={'x': 'Brand', 'y': 'Phones amount'})

