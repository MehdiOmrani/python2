#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1

firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print (lastname + firstname)


# In[10]:


a = 5
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


# In[7]:


#Question 3

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[8]:


#Question 4
nl=[]
for x in range(2000, 3000):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


# In[ ]:


#Question 5
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))


# In[ ]:


#Question 6
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))


# In[ ]:


#Question 7

# input sale amount
amt = int(input("Enter Sale Amount: "))

# checking conditions and calculating discount
if(amt>0): 
    if amt<=500:
       disc = amt*0.05
    elif amt=200-500:
        disc=amt*0.12
    else amt>200:
        disc=0.02 * amt
   

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
else:
    print("Invalid Amount")

