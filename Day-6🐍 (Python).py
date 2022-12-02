#!/usr/bin/env python
# coding: utf-8

# # Assinging the variables

# In[1]:


x = 15
y = 4
z = 3


# In[2]:


x+y


# In[3]:


x-y


# In[4]:


x/y


# In[5]:


x*y


# In[6]:


2 * 2


# In[7]:


2 ** 2


# In[8]:


15*15*15*15


# In[9]:


x ** y


# In[10]:


x / y


# In[11]:



x // y


# In[12]:


import math
math.floor(x/y)


# In[13]:


math.ceil(x/y)


# # Python Identity Operators

# In[14]:


x = 10
y = 10
x is y


# In[15]:


x == y #comp.


# In[16]:


x = 100017
y = x
z = 100017


# In[17]:


x is y


# In[18]:


x is z


# In[19]:


id(x)


# In[20]:


id(y)


# In[21]:


id(z)


# In[22]:


x is z


# In[23]:


x == z


# In[24]:


x is not z


# # Membership Operator

# In[25]:


list1 = [1,2,3,4,5,6,7]

1 in list1


# In[26]:


10 in list1


# In[27]:


10 not in list1


# In[28]:


s1 = {1,2,3,4}
1 in s1


# In[29]:


st1 = 'Learn Data Science'
'data' in st1


# In[30]:


'Data' in st1


# # Python Bitwise Operators

# In[32]:


x = 1010 #10  ; 1011, 1100,1101,1110,1111
y = 0101 #5

x | y = 1111
x & y = 0000


# In[33]:


x = 10
y = 5

x |y


# In[34]:


x & y


# In[35]:


10 == 10


# In[36]:


10 >10


# In[37]:


10 >= 10


# In[38]:


10>4 and 10<3


# In[39]:


10>9 and 4<5


# In[40]:


10>4 or 10<3


# In[41]:


not(10>4 or 10<3)


# In[42]:


x = 10
x += 4


# In[43]:


x


# In[44]:


x = x+4


# In[45]:


x


# In[ ]:




