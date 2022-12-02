#!/usr/bin/env python
# coding: utf-8

# # All About Data Types in Python

# In[1]:


#Numeric Data 

x = 10 #int
y = 10.5 #float
z = 10+5j #10 is real number and 5j is imaginary


# In[2]:


type(x)


# In[3]:


type(y)


# In[4]:


type(z)


# In[5]:


isinstance(z,complex)


# In[6]:


isinstance(10.5,float)


# In[7]:


isinstance(10.5,int)


# In[8]:


#int to float
n = float(x) # n=float


# In[9]:


n


# In[10]:


type(n)


# In[11]:


n = int(n)
type(n)


# In[12]:


n


# In[13]:


#int to complex
n = complex(n) #10+0j


# In[14]:


n


# In[15]:


type(n)


# In[16]:


n = int(n)


# In[17]:


n = float(n)


# In[18]:


n = complex(input('Enter your complex number :- '))


# In[19]:


n


# In[20]:


n = complex(input('Enter your complex number :- '))


# In[21]:


n


# In[22]:


type(n)


# # Bool

# In[23]:


x = True
y = False


# In[24]:


x


# In[25]:


y


# In[26]:


true


# # Sequence Data

# In[27]:


#List []
l = [1,2,3,4,True,[1,2],'data',(1,2,3,8)]


# In[28]:


l


# In[29]:


l[0]


# In[30]:


l[-1]


# In[31]:


l[-1][-1]


# In[32]:


l[-1][0]


# In[33]:


type(l)


# In[34]:


isinstance(l,list)


# In[35]:


#Tupe ()

t = (1,5,8,9,'Ai')
type(t)


# In[36]:


t[0]


# In[37]:


t[0:4] # colon means to ; 0 to 4-1


# In[38]:


#Range()

x = range(10) #1st case


# In[39]:


x


# In[40]:


for i in x:
    print(i)


# In[41]:


x = range(5,20) #2nd case
for i in x:
    print(i)


# In[42]:


x = range(5,20,3) #3rd case
for i in x:
    print(i)


# In[43]:


x = range(20,5,-3) #4th case
for i in x:
    print(i)


# In[44]:


#array
import array as ar


# In[45]:


a = ar.array([1,2,3,4])
a


# In[46]:


a = ar.array('i',[1,2,3,4])
a


# In[47]:


type(a)


# In[48]:


a = ar.array('f',[1.5,2,3,4])
a


# # string

# In[49]:


x = 'data'
type(x)


# In[50]:


x = "data"
type(x)


# In[51]:


x = '''
I love
Data Science
'''


# In[52]:


x


# In[53]:


type(x)


# # Set
# 

# In[54]:


s = {1,2,3,5}


# In[55]:


type(s)


# # Dictionary

# In[56]:


dic={
    'varsity': 'FAU Germany',
    'Dept': 'Data Science'
}


# In[57]:


dic


# In[58]:


type(dic)


# In[59]:


dic.keys()


# # Data Frame (Pandas)

# In[ ]:


get_ipython().system('pip freeze')


# In[6]:


df = pd.read_csv('HW.csv')


# In[ ]:




