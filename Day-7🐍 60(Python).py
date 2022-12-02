#!/usr/bin/env python
# coding: utf-8

# # If Else Statements in Python

# In[4]:


x = 50
y = 100

if x>y:
    print('x is greater than y')
if y>x:
    print('y is greater than x')
    print('data science')
    
else:
    print('Out!')  


# In[7]:


x = 50
y = 100

if x>y:
    print('x is greater than y')
elif y>x:
    print('y is greater than x')
    print('data science')
    if x != y:
        print('Not equal')
    
else:
    print('Out!')


# In[8]:


10 % 3


# In[9]:


num = float(input('Enter any number : '))

if num % 2 == 0:
    if num % 5 ==0:
        print(num,' Divisible bt 5 and 2')
    else:
        print('No 1')
else:
    print('No 2')


# In[10]:


num = float(input('Enter any number : '))

if num % 2 == 0:
    if num % 5 ==0:
        print(num,' Divisible bt 5 and 2')
    else:
        print('No 1')
else:
    print('No 2')


# In[11]:


num = float(input('Enter any number : '))

if num % 2 == 0:
    if num % 5 ==0:
        print(num,' Divisible bt 5 and 2')
    else:
        print('No 1')
else:
    print('No 2')


# In[12]:


from IPython.display import Image
Image('download.png')


# In[13]:


amount = 0

net_units = float(input('Enter your unit value : '))

if net_units <= 100:
    amonut = 0
    
    
elif net_units > 100 and net_units <= 200:
    amount = (net_units - 100) * 5
    

elif net_units>200:
    amount = ((net_units - 200) *10) + 500

print('amount is ',amount)
    


# In[ ]:




