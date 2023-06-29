#-------------------

# 13

a = "!!!Harry!! !!!!!!!!! Harry"
#upppercase-
print(a.upper())

#--------------------------------------------------------------
#lowercase
print(a.lower())

#--------------------------------------------------------------
#strip last space-
print(a.strip()) 

#--------------------------------------------------------------
#repalace harry with john
print(a.replace("Harry","john"))

#--------------------------------------------------------------
#split from space
print(a.split())

#--------------------------------------------------------------
a1 = "harry+john"
#split from +
print(a1.split("+"))

#--------------------------------------------------------------
blogHeading = "introduction tO jS"
#capitalize
print(blogHeading.title())
#--------------------------------------------------------------
str1 = "Welcome to the Console!!!"

#align the string "str1" to the center 50 
#the number of times "Harry" has occurred within

#--------------------------------------------------------------
str1 = "Welcome to the Console !!!"
#check if str1 ends with !!!
print(str1.istitle())

#--------------------------------------------------------------
str1 = "Welcome to the Console !!!"
#check if str1 ends with !!! from 4 to 10
print(str1.endswith("!!!",4,10))

#--------------------------------------------------------------
str1 = "He's name is Dan. He is an honest man."
#use index to find "ishh"
print(str1.index("ishh")) # returns error

#use find to find "ishh"
print(str1.find("ishh")) # returns -1 if flase

#--------------------------------------------------------------
str1 = "WelcomeToTheConsole"
#check if number and alphabet
print(str1.isalnum())

#--------------------------------------------------------------
str1 = "Welcome"
#check if only alphabet
print(str1.isalpha())

#--------------------------------------------------------------
str1 = "hello world"
#check if only lower
print(str1.islower())
#--------------------------------------------------------------
str1 = "We wish you a Merry Christmas\n"
#check if printable
print(str1.isprintable())

#--------------------------------------------------------------
str1 = "         "       #using Spacebar
#check if it has space
print(str1.isspace())
#--------------------------------------------------------------
str1 = "World Health Organization" 
#check if it is Title(1st letters are capital)
print(str1.istitle())

#--------------------------------------------------------------
str2 = "To kill a Mocking bird"
#check if 1st letters are capital
print(str2.istitle())
#--------------------------------------------------------------
str1 = "Python is a Interpreted Language" 
#check if the sentence starts with python
print(str1.startswith("Python"))

#--------------------------------------------------------------
str1 = "Python is a Interpreted Language" 
#change the character casing of the string. Convert Upper case to lower case and lower case to upper case.
print(str1.swapcase())

#--------------------------------------------------------------
str1 = "His name is Dan. Dan is an honest man."
#convert to titleformat
print(str1.title())
#-----------------------------------------------------------------------

#---------------
#---------------

## 17

# We declared a variable N for you.
# Your task is to print all values from 0 to N (inclusive).

N = 11 # Write your answer below


#----------------------------------------------------------------------

# Print all numbers from 42 to 59 (inclusive):

for i in range(42,60):
    print(i)


#------------------------------------------------------------------------------------------
# We declared a variable N for you.
# Your task is to print all values from 0 to N (inclusive).

N = 11 # Write your answer below

for i in range(N+1): # +1 to get upto 11
    print(i)

#--------------------------------------------------------------------------------------------

#-------------------
#------------------

## 23


# Print all items of the list one per line.
lines = ["My candle burns at both ends;", "It will not last the night;", "But ah, my foes, and oh, my friends —", "It gives a lovely light."]

# Write your answer below
for i in lines:
    print(i)

#--------------------------------------------------------------------------------

# Increase by one each value contained in the values list.
# Make the new list
values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 10, 14, 17, 14, 1, 16, 19, 7, 9, 19] # Write your answer below

values = [i+1 for i in values]
print(values)

#---------------------------------------------------------------------------------------

# Define a reversed_values variable whose values are the values in the values list, but in reversed order.
values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 17, 14, 1, 9]

# Write your answer below

reversed_values = []
for i in range(len(values)):
    reversed_values.append(values[len(values) - i - 1])

print(reversed_values)

#------------------------------------------------------------------------------------------------

# What will be the value of values_copy after we execute the following code:
values = [5, 4, 7, 8, 9, 3]

values_copy = []
for v in values:
    values_copy.append(v)

# ANSWER:
[5, 4, 7, 8, 9, 3] #type:ignore

#--------------------------------------------------------------------------------------------------
colors = ["voilet", "indigo", "blue", "green"]
# Change value of an item
colors[2] = "Red"
print(colors)


#----------------------

#----------------------

# 25



tup1 = ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')

#convert to list

list1 = list(tup1)

#-------------------------------------------------------------------------------------------------

## indexing -


# index of "Germany"

print(tup1.index("Germany"))

#-------------------------------------------------------------------------------------

# index of "Germany" in range 2 to 4

print(tup1.index("Germany", 2, 4))

#_-------------------------------------------------------------------------------------

# insert "added:"" in 2 index:

temp = list(tup1)
temp.insert(2, "added") # type: ignore
temp2 = tuple(temp)
print(temp2)

#-------------------------------------------------------------------------------------

# count all 3

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print(Tuple1.count(3))

#-------------------
#-------------------

## 30


# function to calculate factorial:

def factorial(n): # this thing has a limit of 999 though😁
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)

#--------------------------------------------------------------------------------------------------------------

# function to calculate Fibonassi number:
#it works like this: 
# f(0) = 0, f(1) = 1, f(2) = 1+0 = 1, f(3) = 2+1 = 3, f(4) = 3+2 = 5, f(5) = 4+3 = 7 
# f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2)

def fibonassi(n):
    if(n == 1):
        return 1
    elif(n == 0):
        return 0
    else:
        return ((n-1) + (n-2))
    

#--------------------------------------------------------------------------------------------------------------

#----------------------
#----------------------

## 32

# rename to PRACTICE
# Practice Template
# Only use for practice 

# this file won't be uploaded to Git

c = {"Tokyo", "Madrid", "Berlin", "Delhi"}
c2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# union :
c3 = c.union(c2)
print(c3)

# union_update:

c.update(c2) # updating c
print(c)

c2.update(c) # updatimg c2
print(c2)
print(c)

# intersection 
c4 = c.intersection(c2)
print(c4)

#   symmetric difference:
c5 = c.symmetric_difference(c2)
print(c5)

#   difference :

c6 = c.difference(c2)
print('added')
print(c6)


bunty = {"Tokyo", "Madrid", "Berlin", "Delhi"}
rohan = {"Tokyo", "Seoul", "Kabul", "Madrid"}

guddu = bunty.symmetric_difference(rohan)
print(guddu)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)


#-----------------------------------------------------------------------------------------------------------

#--------------------
#--------------------


## 34

    
dic = {'name':'Karan', 'age':19, 'eligible':True}
    
# access single value

print(dic.get('name'))

# access all vales
print(dic.values())

# access all keys:

print(dic.keys())

# access key-value pairs:

print(dic.items())

# Update value:

dic.update({'sdsd': True})

# Clear all items in dictionary:

dic.clear()

# remove an item:

dic.pop('age')
del dic['age']

# remove last item:

dic.popitem()

# clear dictionary:

dic.clear()

# delete ites:

del dic

#------------------
#------------------


