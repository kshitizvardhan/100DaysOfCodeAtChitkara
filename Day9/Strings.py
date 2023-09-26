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

>>>
M Index number= 0
y Index number= 1
  Index number= 2
                          # Above the blank spaces in outpur represents the "\n" character.
 Index number= 3
N Index number= 4
a Index number= 5
m Index number= 6
e Index number= 7
  Index number= 8
i Index number= 9
s Index number= 10
  Index number= 11
                         # Above the blank spaces in outpur represents the "\n" character.
 Index number= 12
K Index number= 13
s Index number= 14
h Index number= 15
i Index number= 16
t Index number= 17
i Index number= 18
z Index number= 19


