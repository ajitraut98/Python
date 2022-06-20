# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:13:38 2020

@author: user
"""

# ch8: functions

# functions
# named parameters
# mandatory and optional parameters
# return 1 or more values from a function
# order of parameters
# lambda functions

# qty, price, tax, discount
# calculate the net price

# parameters are mandatory

# tax and disc are %
# qty and price are numbers
def calcTotalPrice(qty,rate,tax,disc):
    
    totalprice = qty*rate
    
    # apply discount
    totalprice=totalprice-(disc/100)*totalprice
    
    # apply tax to the new amount
    totalprice = totalprice + (tax/100)*totalprice
    
    return(totalprice)

# run the function
tp = calcTotalPrice(5.5,140,12,5)
print("Net price = ", tp)

# add 5 to the net price as additional charge
tp + 5


# if a function does not have a return statement
def calcTotalPrice(qty,rate,tax,disc):
    
    totalprice = qty*rate
    
    # apply discount
    totalprice=totalprice-(disc/100)*totalprice
    
    # apply tax to the new amount
    totalprice = totalprice + (tax/100)*totalprice

# run the function
tp = calcTotalPrice(5.5,140,12,5)
print(tp)
# the return value is None
tp + 5
print("Net price = ", tp)


# return multiple values from a function
def calcTotalPrice(qty,rate,tax,disc):
    
    totalprice = qty*rate
    
    # apply discount
    totalprice=totalprice-(disc/100)*totalprice
    
    # apply tax to the new amount
    totalprice = totalprice + (tax/100)*totalprice
    
    # return the gross price and net price
    return(qty*rate, totalprice)


gp,np = calcTotalPrice(5.5,140,12,5)
print("gross price={}, net price={}".format(gp,np))


# A1) write a function that has 2 numbers as input

# Do
# addition, 
# subtract (shd return +ve number), # multiply, 
# divide (bigger number / smaller number)

# return the results of all the 4

# A2)
# make a circular reference of a list
# i.e. if total elements in a list is 5 and user enters the number 11, then function should return the 1st element ;

# if total elements is 23, and user enters 5, then it should return the 3rd element

# and so on....

list1=['a','b','c','d','e']
elem = 16
list1[elem%len(list1)]

# named parameters

# prefix the parameter name before the value and call the function with these parameters in any sequence

gp,np = calcTotalPrice(tax=12,disc=5,qty=5.5,rate=140)
print("gross price={}, net price={}".format(gp,np))


# making paramters optional
# specify '= 'after the paramters to make it optional

# all mandatory parameters have to be specified first; then the optional parameters

# here, paramters qty/rate are mandatory
# tax and disc are optional

def calcTotalPrice(qty,rate,tax=10,disc=5):
    
    totalprice = qty*rate
    
    # apply discount
    totalprice=totalprice-(disc/100)*totalprice
    
    # apply tax to the new amount
    totalprice=totalprice + (tax/100)*totalprice
    
    # return the gross price and net price
    return(qty*rate, totalprice)

# function call
gp,np = calcTotalPrice(10,200)
print("gross={},net={}".format(gp,np))


# write a function to calcualte the HCF of 2 positive integers


def addnum(num1,num2):
    return(num1+num2)

addnum(5,10)


# lambda functions
ans = lambda a,b : a+b
ans(10,20)

# add the r,g,b values
ans = lambda r,g,b : r+g+b
color = ans(245,145,200)
color

# multiplty numbers
ans = lambda x,y : x*y
ans(5,30)

# find the greatest of the 2 numbers
ans = lambda x,y : x if x>y else y
ans(109,131)

# find the smaller number from 2 numbers
ans = lambda x,y : x if x<y else y
ans(144,203)

# iterations with lambda
list1 = [3,5,7,2,10,14]

list(map(lambda x:pow(x,2),list1))

# A) using lambda, calculate the area of a circle where list1 values represent individual radius

list(map(lambda x: round(3.14*x*x,1),list1))

# create 2 lists that represents length and breadth of a rectange (counts are same)
# to calculate the area of rectangle

# create random data for length/breadth
leng=[]; br=[]

import random as r
for i in range(10):
    leng.append(r.randint(10,25))
    br.append(round(r.uniform(1,5),2))
leng
br
list(map(lambda l,b:l*b,leng,br))


# filter with lambda
age=[]

for i in range(100):
    age.append(r.randint(21,60))

age

# get all the ages > 50
g50 = list(filter(lambda x:x>50,age))
len(g50)


list(map(lambda x:x>50,age))
