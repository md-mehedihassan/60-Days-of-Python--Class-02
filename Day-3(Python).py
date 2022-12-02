#!/usr/bin/env python
# coding: utf-8

# # input function

# In[6]:


data = 'data science fun'


# In[7]:


type(data)


# In[8]:


data


# In[9]:


x = input()
y = input()


# In[10]:


x+y


# In[11]:


type(x)


# In[12]:


type(y)


# In[13]:


x = int(x)
y = int(y)


# In[14]:


x+y


# In[15]:


type(x+y)


# In[16]:


x  = int(input('Enter your 1st num: '))


# In[17]:


x


# In[18]:


y  = float(input('Enter your 2nd num: '))


# In[19]:


x+y


# In[27]:


data = '60 Days of python'


# In[28]:


type(data)


# In[29]:


len(data)


# In[30]:


import sys
sys.getsizeof(data)


# In[31]:


data.count('python')


# In[32]:


sub = 'Days of'


# In[33]:


data.count(sub)


# # Python String Methods

# In[34]:


data = '60 Days of python'
data.find('of')


# In[35]:


data.find('f')


# In[36]:


data.find('y' )


# In[37]:


data.find('y',6,10)


# In[38]:


data.find('y',6,14)


# In[39]:


data.index('y')


# In[40]:


data.index('y',6,13)


# In[41]:


data.index('ai')


# In[42]:


data.lower()


# In[43]:


data.upper()


# In[44]:


data.casefold()


# In[45]:


x = 'data SCIENCE is Fun'


# In[46]:


x.capitalize()


# In[47]:


x.swapcase()


# In[48]:


x.title()


# In[49]:


x.islower()


# In[50]:


x.upper()


# In[51]:


x.isupper()


# In[52]:


x.isdigit()


# In[53]:


x.encode()


# In[54]:


type(x.encode())


# In[55]:


x


# In[56]:


x.split()


# In[57]:


x.split()[0]


# In[58]:


x.split()[1]


# In[59]:


x.center(100)


# In[60]:


x.replace('data','AI')


# In[61]:


x = 10
y = 100
z = x*y

print('I have ',z,'taka')


# In[62]:


print('I have {} taka'.format(z))


# In[ ]:




