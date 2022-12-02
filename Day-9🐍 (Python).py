#!/usr/bin/env python
# coding: utf-8

# In[1]:


data= "python"


# In[2]:


data[0]


# In[3]:


data[-1]


# In[4]:


for x in data:
    print(x)


# In[5]:


for x in data:
    print("x")


# In[6]:


for x in data:
    print(x,"x")


# In[7]:


range(10)


# In[11]:


for x in range (len(data)):
    print(x,"x")


# In[12]:


len(data)


# In[13]:


for x in range (6):
    print(x,"x")


# In[14]:


for x in range (len(data)):
    print(data[x])


# In[15]:


for x in range (6):
    print(data[x])


# In[1]:


data= "i love data science so much"
for x in range (len(data)):
    print(data[x])


# In[17]:


data.split()


# In[18]:


data= "i love data science so much"
data.split()
for x in range (len(data)):
    print(data[x])


# In[19]:


data= "i love data science so much"
data= data.split()
for x in range (len(data)):
    print(data[x])


# In[20]:


data= "i love data science so much"
data= data.split()
for x in range (len(data)):
    print(data[x],x)


# In[21]:


data[1]


# In[22]:


n=[2,3,4,55,60,77,100]
total=0
for x in n:
    total=total+ x
    print(total,x)


# In[23]:


n=[2,3,4,55,60,77,100]
total=0
for x in n:
    total=total+ x
    print(total)


# In[24]:


n=[2,3,4,55,60,77,100]
total=0
for x in n:
    total=total+ x
print(total)


# In[27]:


n=[2,3,4,55,60,77,100]
total=0
for x in n:
    total=total+ x
print( "total" ,total)


# In[28]:


for x in range(10):
    print("data science",x)


# In[29]:


for x in range(5,10):
    print("data science",x)


# In[30]:


for x in range(5,10,2):
    print("data science",x)


# In[31]:


for x in range(500,100,-20):
    print("data science",x)


# In[32]:


for x in range(500,100,-20):
    print(x)


# In[ ]:




