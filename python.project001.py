#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')


# In[5]:


df.shape


# In[6]:


df.head(10)


# In[7]:


df.info()


# In[8]:


# drop blank coloum
df.drop(['Status','unnamed1'],axis =1,inplace=True)


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


pd.isnull(df)


# In[12]:


pd.isnull(df).sum()


# In[14]:


df.dropna(inplace=True)


# In[15]:


df.shape


# In[16]:


# change data type
df['Amount']=df['Amount'].astype('int')


# In[17]:


df['Amount'].dtype


# In[20]:


df.columns


# In[23]:


# rename columns
df.rename(columns={'Marital_Status':'shaadi'})


# In[24]:


df.describe()


# In[35]:


# use describe for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory data Analysis

# In[40]:


ax=sns.countplot(x='Gender',data = df)


# In[43]:


ax=sns.countplot(x='Gender',data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[45]:


sales_gen=df.groupby(['Gender'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending= False)
sns.barplot(x = 'Gender',y= 'Amount',data=sales_gen)


# # Age

# In[46]:


sns.countplot(data = df,x= 'Age Group',hue='Gender')


# In[52]:


ax = sns.countplot(data=df,x='Age Group',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[53]:


sales_Age=df.groupby(['Age Group'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending= False)
sns.barplot(x = 'Age Group',y= 'Amount',data=sales_Age)


# # State

# In[58]:


# total number of order top 10 state
sales_state=df.groupby(['State'], as_index =False)['Orders'].sum().sort_values(by='Orders',ascending= False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Orders',data=sales_state)


# In[59]:


sales_state=df.groupby(['State'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending= False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Amount',data=sales_state)

# From above graphs we can see that unexpectedly most of the orders are from uttar pradesh, Maharashtar and Karnataka respectively but total sales/amount is from Up,Maharashtra,Karnataka
# # Marital_Status

# In[64]:


ax = sns.countplot(x= 'Marital_Status',data = df)
sns.set(rc={'figure.figsize':(7,5)})
for bar in ax.containers:
    ax.bar_label(bars)


# In[69]:


sales_Marital_Status=df.groupby(['Marital_Status','Gender'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending= False)

sns.set(rc={'figure.figsize':(7,5)})
sns.barplot(x='Marital_Status',y='Amount',data=sales_Marital_Status,hue = 'Gender')


# # Occupation

# In[75]:


ax = sns.countplot(x ='Occupation', data =df)
sns.set(rc={'figure.figsize':(7,7)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[77]:


sales_state=df.groupby(['Occupation'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending= False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='Occupation',y='Amount',data=sales_state)


# # Product_Category

# In[98]:


ax = sns.countplot(x ='Product_Category', data =df)
sns.set(rc={'figure.figsize':(13,7)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[87]:


sales_state=df.groupby(['Product_Category'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending= False).head(10)

sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(x='Product_Category',y='Amount',data=sales_state)


# In[99]:


sales_state=df.groupby(['Product_ID'], as_index =False)['Orders'].sum().sort_values(by='Orders',ascending= False).head(10)

sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(x='Product_ID',y='Orders',data=sales_state)


# # Conclusion :
# Married woman age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from food , clothing and Electronics category.