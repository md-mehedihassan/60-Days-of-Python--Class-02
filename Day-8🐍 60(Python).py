#!/usr/bin/env python
# coding: utf-8

# # 01. Take values of length and breadth of a rectangle from user and check if it is square or not.

# In[2]:


#Input the length from user
length = float(input('Enter the length : '))

#Input the breadth from user
breadth = float(input('Enter the breadth : '))

#square is a rectangle whose length and breadth are equal and commonly called as sides which are of equal length.

if breadth == length :
    print('Yes, It is Square')
    
else:
    print('It is not Square')


# In[3]:


#Input the length from user
length = float(input('Enter the length : '))

#Input the breadth from user
breadth = float(input('Enter the breadth : '))

#square is a rectangle whose length and breadth are equal and commonly called as sides which are of equal length.

if breadth == length :
    print('Yes, It is Square')
    
else:
    print('It is not Square')


# # Assignment 02 : Solved
# 02. Take three int values from user and print greatest among them.

# In[4]:


# take three integer numbers from user input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
    largest = num1
    
elif (num2 > num1) and (num2 > num3):
    largest = num2
    
else:
    largest = num3

print("The largest number is",largest)


# In[5]:


# take three integer numbers from user input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
    largest = num1
    
elif (num2 > num1) and (num2 > num3):
    largest = num2
    
else:
    largest = num3

print("The largest number is",largest)


# In[6]:


# take three integer numbers from user input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
    largest = num1
    
elif (num2 > num1) and (num2 > num3):
    largest = num2
    
else:
    largest = num3

print("The largest number is",largest)


# # Assignment 03 : Solved
# 03. A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# In[7]:


held = int(input('Number of classes held : '))
attended = int(input('Number of classes attended : '))

attended_ratio = (attended/held) * 100


# In[8]:


attended_ratio


# In[9]:


if attended_ratio >= 75:
    print('You are allowed')
else:
    print('You are not allowed')


# In[10]:


if attended_ratio >= 65:
    print('You are allowed')
else:
    print('You are not allowed')


# In[11]:


if attended_ratio >= 95:
    print('You are allowed')
else:
    print('You are not allowed')


# # OR

# In[12]:


held = int(input('Number of classes held : '))
attended = int(input('Number of classes attended : '))

attended_ratio = (attended/held) * 100

if attended_ratio >= 75:
    print('You are allowed')
else:
    print('You are not allowed')


# In[13]:


held = int(input('Number of classes held : '))
attended = int(input('Number of classes attended : '))

attended_ratio = (attended/held) * 100

if attended_ratio >= 75:
    print('You are allowed')
else:
    print('You are not allowed')


# In[14]:


held = int(input('Number of classes held : '))
attended = int(input('Number of classes attended : '))

attended_ratio = (attended/held) * 100

if attended_ratio >= 95:
    print('You are allowed')
else:
    print('You are not allowed')


# # Assignment 04 : Solved

# In[15]:


'''
A school has following rules for grading system:-
Below 25 – F, 25 to 44 – E, 45 to 49 – D, 50 to 59 – C, 60 to 79 – B, 80 to 89 - A, Above 90 - A+

QUESTION:- Now, Ask user to enter marks and print the corresponding grade.

'''


# In[16]:


marks = float(input('Enter your marks : '))

if marks < 25:
    print('You are Genius Like me :)')

elif marks>=25 and marks<=44:
    print('E Grade, Pass korco mama! You also tene tune Genius!')

elif marks>=45 and marks<=49:
    print('D Grade')
    
elif marks>=50 and marks<=59:
    print('C Grade')
    
elif marks>=60 and marks<=79:
    print('B Grade')
    
elif marks>=80 and marks<=89:
    print('A Grade')
    
else:
    print('You are a loser!!!')


# In[17]:


marks = float(input('Enter your marks : '))

if marks < 25:
    print('You are Genius Like me :)')

elif marks>=25 and marks<=44:
    print('E Grade, Pass korco mama! You also tene tune Genius!')

elif marks>=45 and marks<=49:
    print('D Grade')
    
elif marks>=50 and marks<=59:
    print('C Grade')
    
elif marks>=60 and marks<=79:
    print('B Grade')
    
elif marks>=80 and marks<=89:
    print('A Grade')
    
else:
    print('You are a loser!!!')


# In[18]:


marks = float(input('Enter your marks : '))

if marks < 25:
    print('You are Genius Like me :)')

elif marks>=25 and marks<=44:
    print('E Grade, Pass korco mama! You also tene tune Genius!')

elif marks>=45 and marks<=49:
    print('D Grade')
    
elif marks>=50 and marks<=59:
    print('C Grade')
    
elif marks>=60 and marks<=79:
    print('B Grade')
    
elif marks>=80 and marks<=89:
    print('A Grade')
    
else:
    print('You are a loser!!!')


# In[19]:


marks = float(input('Enter your marks : '))

if marks < 25:
    print('You are Genius Like me :)')

elif marks>=25 and marks<=44:
    print('E Grade, Pass korco mama! You also tene tune Genius!')

elif marks>=45 and marks<=49:
    print('D Grade')
    
elif marks>=50 and marks<=59:
    print('C Grade')
    
elif marks>=60 and marks<=79:
    print('B Grade')
    
elif marks>=80 and marks<=89:
    print('A Grade')
    
else:
    print('You are a loser!!!')


# In[20]:


marks = float(input('Enter your marks : '))

if marks < 25:
    print('You are Genius Like me :)')

elif marks>=25 and marks<=44:
    print('E Grade, Pass korco mama! You also tene tune Genius!')

elif marks>=45 and marks<=49:
    print('D Grade')
    
elif marks>=50 and marks<=59:
    print('C Grade')
    
elif marks>=60 and marks<=79:
    print('B Grade')
    
elif marks>=80 and marks<=89:
    print('A Grade')
    
else:
    print('You are a loser!!!')

