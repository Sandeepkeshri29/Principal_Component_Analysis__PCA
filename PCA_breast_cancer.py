#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from sklearn.datasets import load_breast_cancer


# In[13]:


cancer_dataset=load_breast_cancer()


# In[14]:


cancer_dataset.keys()


# In[15]:


print(cancer_dataset.DESCR)


# In[17]:


df=pd.DataFrame(cancer_dataset['data'],columns=cancer_dataset['feature_names'])


# In[18]:


df.head()


# In[19]:


## Standardization
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()


# In[21]:


scaler.fit(df)


# In[22]:


scaler_data=scaler.transform(df)


# In[24]:


scaler_data


# In[25]:


##  Applying PCA Algorithms
from sklearn.decomposition import PCA


# In[26]:


pca=PCA(n_components=2)


# In[28]:


data_pca=pca.fit_transform(scaler_data)


# In[29]:


data_pca


# In[30]:


pca.explained_variance_


# In[31]:


plt.figure(figsize=(8,6))
plt.scatter(data_pca[:,0],data_pca[:,1],c=cancer_dataset['target'],cmap='plasma')
plt.xlabel('First principal component')
plt.ylabel('Second Principal Component')


# In[ ]:




