#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to iNeuron - Python In Depth")


# In[5]:


for i in range(2000,3201):illkjlj
    if i%7==0 and i%5!=0:
        print(i,end=",")
        


# In[6]:


FirstName = input("Enter Your First Name")
LastName = input("Enter Your Last Name")
print(LastName + " " + FirstName)


# In[7]:


d=12
V=(4/3)*(3.14)*((d/2)**3)
print(V)


# In[21]:


value = input("Input comma separated numbers from Console : ")
list = value.split(",")
print(list)


# In[16]:


for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")    
        
for i in range(4,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")    


# In[20]:


word = input("Enter a word: ")
revword = word[::-1]
print(revword)


# In[24]:


str = 'WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens'
word = "WE, THE PEOPLE OF INDIA, \n\t having solemnly resolved to constitute India into a SOVEREIGN,!\n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t  and to secure to all its citizens"
print(word)


# In[ ]:




