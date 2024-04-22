#!/usr/bin/env python
# coding: utf-8

# # this is a comment

# In[5]:


'''
test
'''


# In[6]:


"""Test
test"""


# In[16]:


variable = 25
variable_2 = 3.14


# In[9]:


variable


# In[10]:


variable + variable


# In[24]:


var_cal = (variable + variable) * variable / variable * variable_2


# In[25]:


var_cal


# In[19]:


type(var_cal)


# In[20]:


type(variable)


# In[30]:


fruits = ["Apple", "Banana", "Strawberry"]
print(fruits)
type(fruits)


# In[31]:


fruits[0]


# In[32]:


round(var_cal)


# In[33]:


a = 33
b = 200
if(b > a):
    print("b is greater than a")


# In[34]:


for x in fruits:
    print(x)


# In[39]:


a = 1
b = 10
while(a < b):
    print(a)
    a = a + 1


# In[41]:


def addition(a, b):
    c = a + b
    return c

def divide(a, b):
    if(b > 0):
        c = a / b
        return c
    else:
        print("cannot divide trough zero")


# In[46]:


a = 1
b = 0

print(addition(a, b))
print(divide(a,b))


# In[64]:


ghost_intake = ["Gernot Nikolaus", "David Hansen", "Rohit Khati", "Asad Ullah", "Reid Taremwara"]

print("This is the ghost intake:\n")

print("Semester 01") 
for x in ghost_intake:
    print(x)
    
print("\nSemester 02")
ghost_intake.remove("Reid Taremwara")
for x in ghost_intake:
    print(x)
    
print("\nSemester 03")
ghost_intake.remove("Asad Ullah")
for x in ghost_intake:
    print(x)
    
print("\nSemester 04")
ghost_intake.clear()
print("No one left here")


# In[73]:


import random
veggies = ["Carrot", "Cucumber", "Tomato", "Potato", "Eisberg"]

rdn_num = random.randint(0, len(veggies))
print(veggies[rdn_num])


# In[74]:


count = 10
counter = 0
while(counter < count):
    rdn_num = random.randint(0, len(veggies))
    print(veggies[rdn_num])
    counter = counter + 1


# In[115]:


import random

print("HELLO!! WELCOME TO OUR LITTLE GAME")
print("I think about a number and you have to guess it")

mistakes = 3
len = 5
guess = 0

#get random number
rdn_num = random.randint(1, len)
print(rdn_num)


print("while")
if(guess != rdn_num):
    print("What is your guess?")
    guess = input("guess")
    check(guess)
else:
    print("You are out!")
    
def check(input):
    if(input == rdn_num):
        print("You are right!")
    else:
        mistakes = mistakes - 1
        print("You have " + mistakes + " tries left!")
    


# In[ ]:




