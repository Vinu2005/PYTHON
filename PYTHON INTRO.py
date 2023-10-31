#!/usr/bin/env python
# coding: utf-8

# #### IDE(Integrated Develeopment Enviroment)
# 
# Recommended IDEs for Python
# 
# <pre>
# 1) Jupyter
# 2) Google Colab
# 3) VS Code
# 4) PyCharm
# 5) Sublime
# 6) Spyder
# </pre>
# 

# ### Features of Python
# <pre>
# 1) Open Source. It has a Large community.
# 2) It is a high level language.
# 3) It is object oriented.
# 4) It is dynamically typed.
# 5) It is interpreted language.
# 6) It provides lot of different libraries to support different applications.
# 7) Portable
# 8) Supports GUI (Graphical User Interface)
# 9) Simple syntax. Easy to grasp and understand.
# 10) Case sensitive
# </pre>
# etc

# ### Applications of Python
# <pre>
# 1) Data Science/Data Analysis.
# 2) Machine Learning
# 3) AI(Artificial Intelligence) Deep Learning
# 4) CV(Computer Vision)
# 5) NLP(Natural Language Processing)
# 6) Web Development - Frameworks - Django, Flask, Streamlit etc
# 7) Web Scraping
# 8) Automation - Selenium
# 9) To build GUI based applications
# 10) Used in Cloud data engineering
# 11) Craete API and fetch Data from API
# 12) RPA (Robotic Process Automation)
# 13) Cyber Security and networking
# 14) Scientific Computing
# etc
# </pre>

# ### Domains or Industries
# <pre>
# 1) Healthcare
# 2) Banking
# 3) Telecom
# 4) Transportataion
# 5) Ecommerce
# 6) OTT platforms
# 7) Finance
# 8) Marketing
# </pre>

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Jupyter Shortcuts
# <pre>
# 1) To execute the code written in a cell
# a) Press Shift + Enter OR
# b) Press Run from Tool Bar
# 2) To add a new cell below the current cell: B or + (from Tool bar)
# 3) To add a new cell above the current cell: A
# 4) To delete a cell - Double D    
# 5) To undo an operation - Z    
# 6) Find and replace - F
# 7) To see all Shortcuts - H
# </pre>

# In[4]:


x = 14
print(x)


# #### Variables
# 1) Storage units. Entity that stores data. Data can be of any data type.

# In[7]:


s = 45
print(s)

# 1) s is assigned with the value of 20.
# 2) s is initialized with the value of 20.
# 3) the value of 20 is stored in the varaible s.


# #### Rules for Naming a Variable
# <pre>
# 1) Start with A-Z,a-z or (_)underscore.
# 2) It should not contain special characters, space charcaters etc.
# 3) It should not start with number.
# 4) Python keywords should be avoided. (keywords - if,else,elif,for,while,and,or etc)
# </pre>

# In[9]:


dsvcs34543 = "hello"
print(dsvcs34543)


# In[11]:


_ASd34 = 30
print(_ASd34)


# In[10]:


cwdv23*3241&45xsdc = "Kite"
print(cwdv23*3241&45xsdc)


# In[14]:


a1,a2,a3 = "Hello",10,20
print(a1)
print(a2)
print(a3)
print(a1,a2,a3)


# In[15]:


# variable can reinitialized, redeclared and reassigned
x = 15
print(x)
x = "Welcome"
print(x)


# #### Data Type
# Int, float, bool, None, str, complex

# In[15]:


a1 = 0
print(a1)
print(type(a1))


# In[16]:


a2 = 5.78
print(a2)
print(type(a2))


# In[20]:


a3 = True   # False
print(a3) 
print(type(a3))


# In[21]:


a4 = None
print(a4)
print(type(a4))


# In[22]:


a5 = 7+3j
print(a5)
print(type(a5)) # p + qj


# In[24]:


# Str - '', "", """""", ''''''
a6 = "Hello"
a7 = 'welcome'
print(type(a6))
print(type(a7))


# In[27]:


a8 = """Welcome to Python 
learning."""
print(a8)
print(type(a8))


# ### Operators

# ### 1) Arithmetic Operator

# In[32]:


a,b = 5,2
print(a+b)
print(a-b)
print(a*b)
print(a/b)    # returns float
print(a//b)   # int division  
print(a**b)   # power operation
print(b**a)
print(a%b)    # remainder


# ### 2) Assignment Operator

# In[40]:


a,b = 5,2
print(a,b)
a += b  # a = a+b
print(a,b) # (7,2)
a -= b  # a = a-b
print(a,b) # (5,2)
b *= a  # b = b*a
print(a,b) #(5,10)
a /= b   # a = a/b
print(a,b)


# #### 3) Relational or Comparison Operator
# They return True or False

# In[43]:


a,b = 10,7
print(a>b,a>=b)
print(a<b,a<=b)
print(a==b)  # Equality condition
print(a!=b)  # not equal to


# ### 4) Logical Opertators
# and - Returns T when both conditions are T, otherwise F.<br>
# or - Returns T when any one of the condition is T, otherwise F.

# In[46]:


a,b,c = 7,14,10
print(a>b and a<c)
print(b>a and a<=c)
print(a>c or b<a)
print(a>c or b>a)


# ### 5) Membership Operator
# in , not in

# In[51]:


s = "Welcome to Python and data Science"
print('data' in s)
print('Java' in s)
print('Science' not in s)
print('Where' not in s)


# #### Input 
# 1) Accept input from user.<br>
# 2) Returns a string

# In[55]:


n = input('Enter a num: ')
print(n)
print(type(n))


# #### Tyepcasting - Changing from one data type to another

# In[56]:


d = int(input('Enter a num: '))
print(d)
print(type(d))


# In[57]:


d = int(input('Enter a num: '))
print(d)
print(type(d))


# In[61]:


d = int(input('Enter a num: '))
print(d)
print(type(d))


# #### end and sep parameters for print function
# 
# end - The value written in end is displayed at the end<br>
# sep - The value written in sep is used to separate the arguments in the print()

# In[1]:


# \n - newline character
print('Hello \nWorld')


# In[4]:


a,b,c = "Hi",20,'Python'
print(a,b,c) # default value of sep=' ', end='\n'
print('Welcome to Python')


# In[9]:


print(a,b,c,sep=" ** ")
print(a,b,c,end=" 123 ")
print('Hello')


# ### Print formatting

# In[18]:


name = "Ritwik"
age = 24
role = "Data Analyst"
print(name,',who is',age,'yrs old wants to be a',role)  # comma sepearted method
print(f'{name}, who is {age} yrs old wants to be a {role}')  # f-formatting
print('{}, who is {} yrs old wants to be a {}'.format(name,age,role))  # using format function
print("{}, who is {} yrs old wants to be a {}".format(name,age,role))


# In[ ]:




