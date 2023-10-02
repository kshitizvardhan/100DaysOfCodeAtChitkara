#!/usr/bin/env python
# coding: utf-8

# # Local and Global Variables

# In[2]:


s=10
def func():
    s=20 
    
func()
print(s)


# In[3]:


s=10
def func():
    global s
    print(s)
    s=20 
    print(s)
    
func()
print(s)


# # Creating String Variables

# In[7]:


a="Hello there"
print(a)
print(type(a))


# # Creating Numeric Variables

# In[6]:


a=10
b=20.4
print(a)
print(b)
print(type(a))
print(type(b))


# # Creating Boolean Variables

# In[8]:


is_student=True
in_college=True
in_school=False
print(is_student)
print(in_school)
print(type(is_student))
print(type(in_school))


# # Implicit Conversion-- Arithmetic Operation

# In[10]:


a=10
print(type(a))
b=10.34
print(type(b))
sum=a+b
print(sum)
print(type(sum)) # Python interpreter itself converts the type to float.


# # Explicit Conversion-- TypeCasting int(), float(), bool(), str()

# In[12]:


a="The sum is "
print(type(a))
b=45
print(type(b))
sum= a+str(b)
print(sum)
print(type(sum))


# In[20]:


a=1
b=0
print(bool(a))
print(bool(b))


# # print() function

# In[24]:


print("Hello", "Mr.Jack", "How", "are", "you", sep=",")
print('\n')
print("Hello", "Mr.Jack","\n" "How", "are", "you",)
print("\n")
print("Hello", "Mr.Jack","\t" "How", "are", "you",)


# # Python Operators

# ## Arithmetic Operators

# In[25]:


a=10
b=20
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)


# ## Relational Operators

# In[26]:


a=10
b=20
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)


# ## Logical Operators

# In[35]:


a=True
b=False
print(a and b)
print(a or b)
print(not a)
print(not b)


# ## Bit-wise Operators

# In[36]:


a=True
b=False
print(a & b)
print(a | b)


# 
