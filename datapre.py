#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn


# In[2]:


import numpy as np
from sklearn.model_selection import train_test_split


# In[3]:


import pandas as pd


# In[4]:


data = pd.read_csv("CustomerSurvivaleng.csv")


# In[18]:


Y_pred = data['churn']


# In[20]:


data = data.drop(labels="churn",axis=1)


# In[22]:


data = data.drop(labels="ID",axis=1)


# In[24]:


X_fea = data


# In[27]:


Y_pred = list(Y_pred)


# In[38]:


X = np.array(X_fea)


# In[59]:


X_train,X_test,y_train,y_test = train_test_split(X,Y_pred)


# In[60]:


import csv


# In[61]:


with open("X_train.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(["plan","duration","data","change","contract","corp","month"])
    #写入多行用writerows
    writer.writerows(X_train)
#plan	duration	data	change	contract	corp	month


# In[62]:


with open("X_test.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(["plan","duration","data","change","contract","corp","month"])
    #写入多行用writerows
    writer.writerows(X_test)
#plan	duration	data	change	contract	corp	month


# In[67]:


y_train = np.reshape(y_train,(3731,1))


# In[68]:


with open("y_train.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(["churn"])
    #写入多行用writerows
    writer.writerows(y_train)
#plan	duration	data	change	contract	corp	month


# In[70]:


y_test = np.reshape(y_test,(1244,1))


# In[71]:


with open("y_test.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(["churn"])
    #写入多行用writerows
    writer.writerows(y_test)
#plan	duration	data	change	contract	corp	month


# In[ ]:




