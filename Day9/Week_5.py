#!/usr/bin/env python
# coding: utf-8

# # Introduction to Strings

# In[1]:


a='My Name is Kshitiz'
print(a)


# In[3]:


a="My Name is Kshitiz"
print(a)


# In[4]:


a='''My 
Name is 
Kshitiz'''   # Printing a multiline string
print(a)


# In[7]:


s="Kshitiz"
for i in range(len(s)):
    print(s[i], "Index number=",i)


# In[11]:


s='''My 
Name is 
Kshitiz'''
for i in range(len(s)):
    print(s[i], "Index number=",i)


# In[ ]:


# Above the blank spaces in outpur represents the "\n" character. 

