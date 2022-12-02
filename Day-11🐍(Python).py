#!/usr/bin/env python
# coding: utf-8

# # Nested Loop

# In[6]:


rows=4
#outer loop
for x in range(rows):
    #inner loop
    for y in range(rows):
        print('#', end= ' ')
    print('')


# In[7]:


rows=4
#outer loop
for x in range(rows):
    #inner loop
    for y in range(rows):
        print('#', end= ' ')
        print('')


# In[8]:


rows=4
#outer loop
for x in range(rows):
    #inner loop
    for y in range(x):
        print('#', end= ' ')
    print('')


# In[9]:


rows=4
#outer loop
for x in range(1,rows+1):
    #inner loop
    for y in range(1,x+1):
        print('#', end= ' ')
    print('')


# In[10]:


num=[1,2,3,4,5]
#outer loop
for ele in num:
    #inner
    index=0
    while index<len(num):
        print(num[index],end=' ')
        index=index+1
        print('')


# In[11]:


num=[1,2,3,4,5]
#outer loop
for ele in num:
    #inner
    index=0
    while index<len(num):
        print(num[index],end=' ')
        index=index+1
        print('\n')


# In[12]:


num=[1,2,3,4,5]
#outer loop
for ele in num:
    #inner
    index=0
    while index<len(num):
        print(num[index],end=' ')
        index=index+1
    print('')


# In[13]:


num=[1,2,3,4,5]
#outer loop
for ele in num:
    #inner
    index=0
    while index<len(num):
        print(num[index],end=' ')
        index=index+1
    print('\n')


# In[17]:


num=[1,2,3,4,5]
#outer loop
for ele in num:
    #inner
    index=0
    while index<len(num):
        print(num[index],end=' ')
        index=index+1
    print('   \n  ')


# In[ ]:




