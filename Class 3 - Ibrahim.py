#!/usr/bin/env python
# coding: utf-8

# In[1]:


name="Ibrahim"


# In[4]:


if name == "Ibrahim":
  print("Yes, the name is Ibrahim")


# In[5]:


a=10
b=45
c=2

if c==2:
    print(a+b+c)


# In[7]:


if name == "Ibrahim":
  print("Yes, the name is "+name)


# In[9]:


if name == "Salman":
  print("Yes, the name is "+name)
else:
    print("No, the name is not "+name)


# In[17]:


animal="Ant"


# In[19]:


if animal=="Cat":
    print("Yes, this is "+animal)
    
elif animal=="Dog":
    print("Yes, this is "+animal)
    
elif animal=="Elephant":
    print("Yes, this is "+animal)
    
else:
    print("We dont know the animal")


# In[26]:


street="Jinnah"


# In[27]:


if street=="Gulshan":
    print("Yes, this is "+street)
    
elif street=="Johar":
    print("Yes, this is "+street)
    
elif street=="Garden":
    print("Yes, this is "+street)
    
else:
    print("We dont know the street")


# In[38]:


num1=2442
num2=78

op="/"

if op=="+":
    print(num1+num2)
    
elif op=="-":
    print(num1-num2)
    
elif op=="*":
    print(num1*num2)
    
else:
    print(num1/num2)


# In[45]:


age=18
gender="male"

if age>=18 and gender=="male":
    print("You are allowed to ride the bike")
    
else:
    print("You are not allowed")


# In[44]:


age=15
gender="female"

if age>=18 or gender=="male":
    print("You are allowed to ride the bike")
    
else:
    print("You are not allowed")


# In[48]:


age=18
gender="male"

if age>=18:
    if gender == "male":
        print("You are a male, you are allowed to ride a bike")
        
    elif gender == "female":
        print("You are a female, you are not allowed to ride a bike")


# In[51]:


age=input("Enter Age: ")
gender=input("Enter Gender: ")

if int(age)>=18:
    if gender == "male" or gender == "Male":
        print("You are a male, you are allowed to ride a bike")
        
    elif gender == "female" or gender == "Female":
        print("You are a female, you are not allowed to ride a bike")
        
else:
    print("You are under age")


# In[ ]:


age=input("Enter Age: ")
gender=input("Enter Gender: ")

if int(age)>=18:
    if gender == "male" or gender == "Male":
        print("You are a male, you are allowed to ride a bike")
        
    elif gender == "female" or gender == "Female":
        print("You are a female, you are not allowed to ride a bike")
        
else:
    print("You are under age")

