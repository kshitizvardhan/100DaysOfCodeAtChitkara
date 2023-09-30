#!/usr/bin/env python
# coding: utf-8

# # Introduction to 2-D List

# In[1]:


li=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


# In[7]:


li[2][2] 
# First Bracket Represents the rows.
# Second Bracket Represents the Columns.


# In[8]:


li[3][2]


# In[9]:


# Replacing a new number
li[3][2]=20
li # Lists are mutable.


# ## How 2-D Lists are Stored?

# In[25]:


li=[[1,2,3,4],[5,6,7,8]]


# In[26]:


li[0]


# In[27]:


type(li[0])


# In[28]:


id(li)


# In[29]:


id(li[0])


# In[30]:


id(li[1])


# In[31]:


print(id(li[0]))
li[0][2]=10
print(li)
print(id(li[0]))


# In[ ]:




