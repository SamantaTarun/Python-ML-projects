#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[10]:


s1=pd.Series([1,2,3,4,5]) # series object is 1D labeled array


# In[11]:


s1


# In[12]:


type(s1)


# In[13]:


s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[14]:


s1


# In[15]:


#creating series with dictionary
pd.Series({'a':10,'b':20,'c':30})


# In[16]:


pd.Series({'a':10,'b':20,'c':30},index=['b','c','d','a'])


# In[17]:


s1=pd.Series([1,2,3,4,5,6,7,8,9])


# In[18]:


s1[3]


# In[19]:


s1[0:4]


# In[20]:


s1[-3::1]


# In[24]:


s1=pd.Series([1,2,3,4,5,6,7,8,9])
s2=pd.Series([10,20,30,40,50,60,70,80,90])


# In[25]:


s1+s2


# In[26]:


s1*10-s2


# In[27]:


s1-100


# In[28]:


s1*5


# In[29]:


s1/10


# In[31]:


s1=pd.Series([1,2,3,4,5,6,7,8,9])
s2=pd.Series([10,20,30,40,50,60,70,80,90])


# In[32]:


s1+s2


# In[34]:


#data frame comprises of rows and column
import pandas as pd
pd.DataFrame({'Name':['Anne','Bob','Matt'],'Marks':[75,12,82]})


# In[36]:


iris=pd.read_csv('C:/Users/TARUN SAMANTA/Desktop/Compressed/iris.csv')


# In[41]:


iris.head() # first 5 records


# In[39]:


iris.tail()  # last 5 records


# In[42]:


iris.head(15)  # first 15 records


# In[44]:


iris.shape  #no of rows and columns


# In[47]:


iris.describe() #mean,sd,min,max


# In[49]:


iris.iloc[0:3,0:2] #first 3 rows and 2 columns


# In[51]:


iris.iloc[5:11,2:] # last index exvclusive


# In[54]:


iris.loc[5:11,('SepalWidthCm','PetalLengthCm','Species')]


# In[55]:


#axis=1 means column
#axis=0 means rows

iris.drop("Species",axis=1)


# In[59]:


iris.drop([5,6,7],axis=0) # deleting rows 5,6,7


# In[60]:


iris.head()


# In[61]:


iris.min()


# In[62]:


iris.max()


# In[63]:


iris.mean()


# In[64]:


iris.median()


# In[65]:


iris.std() # standard deviation


# In[66]:


iris.head()


# In[70]:


iris['Species'].value_counts()


# In[72]:


iris.sort_values(by='PetalWidthCm')   #sorting all details w.r.t PetalWidthCm column


# In[ ]:




