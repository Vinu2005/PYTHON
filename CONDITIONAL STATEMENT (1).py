#!/usr/bin/env python
# coding: utf-8

# In[2]:


age=int(input("Enter your age: "))
if age>=18:
   print("You are eligible for vote! ")
else:
    print("You are not eligible for vote!")


# In[ ]:


##elif


# In[4]:


age=int(input("Enter your age: "))
if age<=12:
   print("You are a kid! ")
elif age==18:
   print("You are 18 and adulthood!")
elif age>=19:
    print("You are above 18!")


# In[ ]:


##Traffic light


# In[10]:


light=input("Enter the light color: ")
if light=='yellow':
    print("Car has to wait!")
elif light=='green':
    print("Car is allowed to go!")
elif light=='red':
    print("Car is allowed to stop!")
else:
    print("Unrecognised signal!")


# In[ ]:


##pass


# In[11]:


age=13
if age<=12:
    pass


# In[ ]:


##grade


# In[14]:


name=input("Enter your name: ")
course=input("Enter student class: ")
section=("Enter student section: ")
marks=int(input("Enter student marks: "))

if marks>=90:
    print("GRADE A= OUTSTANDING!")
elif marks>=80:
    print("GRADE B=EXECELLENT!")
elif marks>=70:
    print("GRADE C=VERY GOOD!")
elif marks>=60:
    print("GRADE D=GOOD!")
elif marks>=45:
    print("GRADE E=SATISFACTORY!")
else:
    print("FAIL!")


# In[ ]:


##Nested condition


# In[15]:


name = input("Enter name:").title()
clas = input("Enter class:")
section = input("Enter section:")
subject = input("Enter the subject name:")
mark = float(input("Mark scored in that subject:"))
 
print("\n----Tracing your", subject, "mark------")
print("Name:", name)
print("Class:", clas)
print("Section:", section)
if mark < 0 or mark > 100:
    print("Error: Mark should be between 0 and 100 only!")
elif mark < 50:
    print(subject, "mark is ", mark)
    print("Failed in ", subject)
elif mark >= 50:
    print(subject, "mark is ", mark)
    print("Congratulations! Pass in ", subject)
    if mark >=50 and mark < 60:
        print("Remark: Good in ", subject)
    elif mark >= 60 and mark < 80:
        print("Remark: Very good in ", subject)
    elif mark >= 80 and mark < 100:
        print("Remark: Outstanding  in ", subject)


# In[ ]:


##Multiple Condition


# In[ ]:


name = input("Enter name:").title()
clas = input("Enter class:")
section = input("Enter section:")
eng = float(input("Enter English mark:"))
hin = float(input("Enter Hindi mark:"))
math = float(input("Enter Math mark:"))
phy = float(input("Enter Physics mark:"))
chem = float(input("Enter Chemistry mark:"))
 
total_mark = eng + hin + math + phy + chem
percentage = total_mark / 5
 
print("\n---------Printing result-------------")
print("Name:", name)
print("Class:", clas)
print("Section:", section)
print("Percentage:", percentage,"%")
if percentage < 0 or percentage > 100:
    print("Error: percentage should be between 0 and 100 only!")
elif percentage < 45:
    print("Failed!")
elif percentage >= 45:
    print("Pass!")
    if percentage >=45 and percentage < 60:
        print("Remark: Just passed!")
    elif percentage >= 60 and percentage < 75:
        print("Remark: Good!")
    elif percentage >= 75 and percentage < 85:
        print("Remark: Very Good!")
    elif percentage >= 85 and percentage < 100:
        print("Remark: Excellent!")

