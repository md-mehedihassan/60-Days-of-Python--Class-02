#!/usr/bin/env python
# coding: utf-8

# # Basic Notebook

# In[2]:


"data science"


# In[7]:


"Hello World & welcome to 60 Days of Python."


# In[8]:


var="Hello World"
print(var)


# In[9]:


var="Hello World"
print("var")


# In[13]:


var="Hello World"
print(var)
print("My Sentence is " + var)


# In[14]:


id(var)


# In[15]:


import sys


# In[16]:


sys.getsizeof(var)


# In[17]:


x=100


# In[18]:


x


# In[19]:


y=100


# In[20]:


y


# In[21]:


id(x)


# In[22]:


id(y)


# In[23]:


x=1000
Y=1000
id(x)


# In[24]:


id(Y)


# In[25]:


x,y,z=10,100,1000


# In[26]:


x


# In[27]:


z


# In[28]:


y


# In[29]:


x,y,z=10,1000


# In[30]:


X = 1
x = 2


# In[31]:


X


# In[32]:


x


# In[33]:


VARSITYID = 1001
varsity_id = 1001


# In[34]:


VARSITYID


# In[35]:


arsity_id


# In[36]:


varsity_id


# Local vs Global

# In[37]:


x = 1000 #global

def func1():
    x = 500 #local
    print('My Num is : ',x)
func1()


# In[44]:


x = 1000 #global

def func1():
    x = 500 #local
    print('My Num is : ',x)
func1()
print('My Num is : ',x)


# In[1]:


def func1():
    global x
    x = 500 #local
    print('My Num is : ',x)
func1()
print('My Num is : ',x)


# # input function
