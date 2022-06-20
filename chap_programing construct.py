 # -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:00:53 2020

@author: user
"""
# ch7: programming constructs


# operators
    # mathematical
    # logical

# statements:
    # if
    # if-else 
    # if-else if-else

# loops
    # for
    # while


# assignment
age = 10

# given an age, print if the person is an adult or not
# conditon for adult = 18+

if age > 18:
    print("is adult")
else:
    print("not an adult")

age=18 
if age >= 18:
    print("is adult")
else:
    print("not an adult")
    
# similarly < and <=
# check if a person is within the age limit to take test.
# age limit = 30

age = 40
if age <= 30:
    print('qualified')
else:
    print('not qualified')

# check equality ==
status = "shipped"    

if status.lower() == "shipped":
    print("product has been shipped")
else:
    print("product not shipped")


# checking for equality with a constant
    
STATUS_SHIPPED = "SHIPPED"    
status = " shipped "

if status.lower().strip() == STATUS_SHIPPED.lower():
    print("product has been shipped")
else:
    print("product not shipped")

# != (not equal to)
colour = "red"
print(colour)
colour = "white"

if colour != 'white':
    print("colour is not white")
else:
    print("colour is white")

    
# Multiple conditions
# AND operator
# OR operator

exp=5; relocate="Y"

if ( (exp>3) & (relocate=="Y") ):
    print("shortlisted for interview")
else:
    print("not shortlisted")
    
# check if a person is qualified to give a test by checking the age
# min age shd be 18 and max age shd be 30

# method 1
age = 10
if ( (age>=18) & (age<=30)):
    print("eligible")
else:
    print("not eligible")    

# method 2
if (18<=age<=30):
    print("eligible")
else:
    print("not eligible")    

# method 3
if age in range(18,30):
    print("eligible")
else:
    print("not eligible")
    
    
# OR operator
'''
T or R -> T
F or T -> T
T or T -> T
F or F -> F
'''

# find if a person is qualified for a job
# requirements: experience atleast 5 years
# OR  educ qual must be PG

exp=14; educ="UG"

if((exp>=5) | (educ=="UG") ):
    print("qualified")
else:
    print("not qualified")
    
# A1
# i) check if the password contains atleast 6 characters
# ii) check if the first character starts with upper case

pwd = "Ab"

if len(pwd)<6:
    print("ERROR")
else:
    print("OK")

# m1
import string as s
if pwd[0] in s.ascii_uppercase:
    print("starts with upper case")
else:
    print("does not start with uppercase")

# m2    
if pwd[0].isupper():
    print("starts with upper case")
else:
    print("does not start with upper case")
    
# Null data
balance = None
print(balance)

if balance is None:
    print('none')

if balance==None:
    print('None')
else:
    print('Not None')
    

## if-elseif-else
area = 903

if area > 3000:
    house = "large"
elif area in range(2000,3000):
    house = "medium"
elif area in range(1000,2000):
    house = "small"
else:
    house = "tiny"

print("area={},house={}".format(area,house))

# to restrict the area between 1-3000

area = 3001

# nested if 
if area in range(1,3001):
    if area > 3000:
        house = "large"
    elif area in range(2000,3000):
        house = "medium"
    elif area in range(1000,2000):
        house = "small"
    else:
        house = "tiny"
    print("area={},house={}".format(area,house))
else:
    print('{} invalid value'.format(area) )
    
    
# if-elif-else for float values
# classify weight as 
    
    # obese       ->  > 81.1
    # very fat    ->   75.1 -> 80
    # fat         ->   70.5 -> 75
    # normal      ->   50.1 -> 70.4
    # underweight ->   < 50.1
    
weight = 58.5

if weight > 81.1:
    mass = "obese"
elif 75.1<=weight<=80:
    mass = "very fat"
elif 70.5<=weight<=75:
    mass = "fat"
elif 50.1<=weight<=70.4:
    mass = "normal"
else:
    mass = "underweight"
    
print(mass)


# loops
# i) for loop

# run a loop 5 times; starting at 0; ending at 4
for i in range(5):
    print(i)

# start = 1; end = 5
for i in range(1,6):
    print(i, end=",")

# start=1; end=50; skip by 6
for i in range(1,51,6):
    print(i, end=" ")

# create a list of 10 random integers
num1 = [10,47,33,109,39,28,68,71,48,93]

# add PI to each value of the list

import math
math.pi

print(num1)
# extract the elemets of the list for processing

# method 1 -> data as it is
for e in num1:
    print(round(e + math.pi,2))

# method 2 -> using the index position
for e in range(0,len(num1)):
    print(round(num1[e]+math.pi,2))
    
# create a list of strings (10 different strings)
# count the total vowels in each string

data=['tiger','apple','computer','elephant','programme']

for e in data:
    total = e.count('a') + e.count('e') + e.count('i') + e.count('o') + e.count('u')
    
    print('word {} has {} vowels'.format(e,total))
    
    
1st iteration -> e = "tiger"

total = 'tiger'.count('a') +'tiger'.count('e') + 'tiger'.count('i') +'tiger'.count('o') + 'tiger'.count('u')
print(total)


# ii) while loop

# print the first 5 numbers
start=1

while(start < 100):
    print(start)

    start+=1

# terminate the loop half way
if (start >= 15):
    break
   






# generate a random number between 1-100
# which is a multiple of 7
import random as r

# method 1
rem=1; iters = 1
while(rem>0):
    num = r.randint(1,100)
    rem = num%7
    iters+=1
    
print("Number = {} generated in iteration {}".format(num,iters-1))



# method 2
found=False; iters=1

while(not found):
    num = r.randint(1,100)
    iters+=1
    if num%7==0:
        found=True

print("Number = {} generated in iteration {}".format(num,iter-1))
    

