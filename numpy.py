#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a=np.array([1,2,3,4])


# In[2]:


a


# In[7]:


type(a)


# In[11]:


b=np.array([[1,2,3,4],[4,3,2,1]])


# In[13]:


b


# In[15]:


c=np.zeros((5,5))


# In[18]:


c


# In[22]:


d=np.full((3,2),56)


# In[24]:


d


# In[26]:


n1=np.arange(10,20)


# In[28]:


n1


# In[30]:


n2=np.arange(10,50,5)


# In[33]:


n2


# In[35]:


n4=np.arange(50,101)


# In[39]:


n4


# In[44]:


n5=np.random.randint(1,10000,10)


# In[45]:


n5


# In[49]:


n6=np.array([[1,2,3,4],[4,5,6,7]])
n6


# In[55]:


n6.shape=(4,2)
n6


# In[58]:


#vertical stack
n1=np.array([10,20,30])
n2=np.array([40,50,60])
np.vstack((n1,n2))


# In[59]:


#horizontal stack

n1=np.array([10,20,30])
n2=np.array([40,50,60])
np.hstack((n1,n2))


# In[61]:


n1=np.array([10,20,30,40,50,60])
n2=np.array([50,60,70,80,90])


# In[63]:


np.intersect1d(n1,n2)


# In[66]:


np.setdiff1d(n1,n2)


# In[68]:


np.setdiff1d(n2,n1)


# In[70]:


n1=np.array([10,20,30])
n2=np.array([40,50,60])
np.sum([n1,n2]) 


# In[72]:


np.sum([n1,n2],axis=0) # based on column wise addition


# In[75]:


np.sum([n1,n2],axis=1) # based on row wise addition


# In[76]:


n1=np.array([10,20,30])


# In[77]:


n1


# In[78]:


n1+5


# In[79]:


n1-5


# In[81]:


n1*10


# In[82]:


n1/5


# In[83]:


n1=np.array([10,20,30,40,50,60])


# In[85]:


n1


# In[87]:


np.mean(n1)


# In[89]:


np.median(n1)


# In[92]:


np.std(n1)


# In[93]:


np.save('my_numpy',n1)


# In[94]:


n2=np.load('my_numpy.npy')
n2


# In[ ]:




