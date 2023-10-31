#!/usr/bin/env python
# coding: utf-8

# #### Jupyter Shortcuts
# 1) Shift + Enter = Run a cell<br>
# 2) Shift + Tab = Displays function definition<br>

# ### Variable
# 1) A variable is a container which is used to store some value. The value can be of any data type<br>
# 2) Multiple variables can be initialized in the same line by separating them by comma<br>
# 3) Variables can be reinitialized, reassigned, redeclared

# In[2]:


a = 40
print(a)
# a is the variable
# 1) The value of 40 is stored in the variable a
# 2) The value of 40 is assigned in the variable a
# 3) The variable a is initialized with the value of 40


# In[4]:


# Multiple variables can be initialized in the same line by separating them by comma
p,q,r = 10,'Python',True
print(p)
print(q)
print(r)
print(p,q,r)


# In[7]:


# Variables can be reinitialized, reassigned, redeclared
x = 10
print(x)
x = 25
print(x)


# #### Comments
# 1) They are meant for internal documentation.<br>
# 2) They are written by writing a '#' in the begnning<br>
# 3) Comments dont get executed.

# In[8]:


# Variables can be reinitialized, reassigned, redeclared


# #### Rules of Naming a variable
# 
# 1) Start with A-Z, a-z or underscore(_)<br>
# 2) Should not start with number<br>
# 3) Should not contain special characters<br>
# 4) Should not contain python keywords like - if,else, or ,in ,and in,for, while, not, class, def, try, except etc<br>

# In[11]:


wind1234 = "Hello"
print(wind1234)


# In[12]:


284sdv = "Python"
print(284sdv)


# In[14]:


KJsdv_dw%cbk22 = "India"
print(KJsdv_dw%cbk22)


# In[15]:


_vDWvn108 = "Google"
print(_vDWvn108)


# In[ ]:





# #### Dynamic Typing
# The data type of the variable is defined at the run time

# In[19]:


x = "Hello"
print(x)
print(type(x))
x = 45
print(x)
print(type(x))


# #### Data Types
# int,float,str,bool,NoneType,complex

# In[23]:


a1 = 342
print(a1)
print(type(a1))


# In[25]:


a2 = 5.6
print(a2)
print(type(a2))


# #### Strings
# 1) Enclosed in single, double or triple quotes<br>
# 2) Triple quotes are used to write multiline strings
# 
#         "" - Double Quotes
#         '' - Single Quotes
#         """""" - Triple quotes
#         '''''' - Triple quotes

# In[28]:


s1 = 'Welcome'
print(s1)
print(type(s1))
s2 = "Google"
print(type(s2))


# In[31]:


s3 = """Welcome to 
Python"""
print(s3)
print(type(s3))


# In[35]:


s4 = True
print(type(s4))
s5 = 5+7j
print(type(s5))
s6 = None
print(type(s6))


# ### Operators

# #### 1) Arithmetic Operators

# In[38]:


a,b = 5,2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  # int div
print(a**b)  # power operator
print(a%b)   # % remainder


# #### 2) Assignment Operator

# In[43]:


a,b = 5,2
print(a,b)
a  += b   # a = a+b
print(a,b)
a -= b   # a = a-b
print(a,b)
b *= a  # b = b*a
print(a,b)
a /= b   # a = a/b
print(a,b)


# #### 3) Relational or Comparison Operators - returns True or False

# In[48]:


a,b=12,15
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)  # comparison
print(a!=b)  # not equal to


# #### 4) Logical Operators - returns True or False
# 
# and - returns True when both conditions are True, otherwise False 
# 
# or - returns True when either of the conditions is True, otherwise False

# In[54]:


a,b,c = 34,45,39
print(a>b and b>c)
print(a<b and b>c)
print(c<a or b>=a)
print(a>b or b<c)


# #### 5) Membership Operator(in, not in) - returns True or False
# membership operators works with Strings, List and Tuples,Sets

# In[57]:


w = "Welcome to Python learning"
print("Python" in w)
print("ing" in w)
print("where" in w)
print("when" not in w)
print("to" not in w)


# ### print and input (Input and Output)
# \n - newline character

# In[59]:


print('Welcome')   # end= '\n'
print('python')
print('Functions and def \nkeyword in Python')


# In[ ]:





# #### parameters of print - end and sep
# end - values passed in end parameter will be displayed at the end

# In[62]:


a = "Hello"
b = "Image"
c = "Audio"
print(a,b,c,end=" ** ")  # end = " ** "
print(b)     # end = '\n'


# #### sep - It is used to sepearate different values that are passed in the print()

# In[65]:


a = "Hello"
b = "Image"
c = "Audio"
print(a,b,c)
print(a,b,c,sep=" @@ ")


# In[ ]:





# #### input()
# 1) It is used to accpet user input. Accept data at run time.<br>
# 2) Return type of input() is string

# In[71]:


n = input('Enter a number: ')
print(n)
print(type(n))


# In[ ]:





# #### Typecasting
# Changing data from one data type to another data type

# In[74]:


n1 = int(input('Enter number: '))
print(n1)
print(type(n1))


# In[75]:


n1 = int(input('Enter number: '))
print(n1)
print(type(n1))


# ### print formatting methods

# In[79]:


name = "Ankit"
age = 24
city = "Delhi"
print(name,'who lives in',city,'is',age,'yrs old')
print(f'{name} who lives in {city} is {age} yrs old')  # f - string
print('{} who lives in {} is {} yrs old'.format(name,age,city))


# In[79]:


# Varaibles
# data types
# operators
# rules for naming variable
# end and sep
# print formatting
# typecasting and input()


# In[ ]:


# 

