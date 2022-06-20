# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:58:41 2020

@author: user
"""
--ch9--numpy
# number python
import numpy as np

# diffrence between a python list and a numpy array

# create 2 python lists with random numbers
lis1=[4,10,59,14,29]
lis2=[14,90,33,18,40]
lis1+lis2

arr1=np.array([4,10,59,14,29])
arr2=np.array([14,90,33,18,40])
arr1
arr2

type(arr1)
type(lis1)
type(arr2)

# add the 2 arrays - adds elements-wise and returns the individual sum
arr1+arr2

# to get all the functions of numpy
dir(np)

# concatenate arrays into one
np.concatenate([arr1,arr2])

# create multiple random integers
wt = np.random.randint(5,100,30)
len(wt)
print(wt)

# append values to an existing array

wt = np.append(wt,np.random.randint(40,75,12))
len(wt)
print(wt)

# element-wise arithmetic in a single line
wt+1.5
wt-2.5

# numpy does not support python functions
round(arr1/3,2)
np.round(arr1/3,2)

print(np.__version__)

# diffrence between python and numpy code

result = []
%timeit [i**2 for i in range(1,100001)]

num = np.arange(1,10001)
%timeit num**2

# area of circle
radius = np.array([1.2,1.4,2.3,4,5])
np.round(np.pi * radius**2,2)

# sequence of numbers
np.arange(5)
# 0 to 4
# 1-11 with diffrence of 4
np.arange(1,11,4)

# convert a 1-d array into a 2-d array
arr1 = np.arange(1,21)
print(arr1)
arr1.shape

# reshape() converts an array into a new shape by specifying the rows & columns
arr1 = arr1.reshape(4,5)
print(arr1)
arr1.ndim
arr1 = arr1.reshape(10,2)
print(arr1)

# when rows are not known and column are known, then how to reshape
arr2 = np.arange(1,45)

# assume that the number of columns=4
# the row parameter is given as -1 to indicate it is dynamic
arr2 = arr2.reshape(-1,4)
arr2.shape

# simillary we can fix rows and make columns dynamic
arr3=np.arange(1,25)
# fix rows=4
arr3=arr3.reshape(4,-1)
arr3

# all in a single line
np.arange(1,21).reshape(-1,5)

# crate 30 random numpy integers and convert it into a matrix having 5 columns

np.random.randint(100,250,30).reshape(-1,5)

# query on np array
arr4=np.random.randint(1,101,45)

# get all numbers > 70
arr4[arr4>70]
# get all the even numbers
arr4[arr4%2==0]

# transpose  (rows become column, and colum becomes rows)
arr3
arr3.T

# random float numbers in numpy
# i) between 0-1  (used in probability)
np.random.ranf(5)
np.round(np.random.ranf(5),2)

# ii) between any 2 values
np.round(np.random.uniform(10,20,6),3)

# sequence of numbers between 2 float numbers
np.round(np.linspace(1,5,10),3)

# python object can be converted to numpy
list1=[1,4,19,20]
type(list1)

# convert python list to numpy
list1=np.asarray(list1)
type(list1)
# pre-defined array
# create an empty numpy array and initialise with random numbers (int/float)
np.empty([2,3],np.int32)
np.empty([2,3],np.int64)
np.empty([4,5],np.float32)

# create and initialise arrays with 0/1
np.zeros([4,6],np.int32)
np.zeros([4,6],np.float32)

np.ones([3,3],np.int32)
np.ones([3,3],np.float32)

# to get index positions of array matching a condition

# get the index positions of numbers that are >50
np.where(arr4>50)
arr4[2]
arr4[1]

# to get the actual values matching the index position
arr4[np.where(arr4>50)]

# a2)
# get all the numbers from arr4 that are between 40 and 70

ans=arr4[np.where(arr4>=40)and(arr4<=70)]
print(ans)
# ascending sort
np.sort(ans)
# descending sort
np.sort(-ans)
-1*np.sort(-ans)

# create unique values
pop = np.arange(1000)
# take a sample of 25 unique values from a population of 1000 numbers
samp = np.random.choice(pop,25,replace=False)
np.sort(samp)

# accesing the numpy array
dataset=np.random.randint(5,100,40).reshape(-1,5)
print(dataset)
# get row1,all column
dataset[0]
dataset[0,0]
dataset[0,0:4]
dataset[0:3,0:2]
dataset[0,(0,4)]
dataset[4,2]
np.where(dataset==93)
# changing values in array
dataset[0,0]=143
print(dataset)

# axis
# sum of values of the array
dataset
np.sum(dataset)

# axis=1--> row operation
# axis=0 -> column operation

np.sum(dataset,axis=1)

# to get the sum of the first 3 rows
np.sum(dataset,axis=1)[0:3]
np.sum(dataset[0:3],axis=1)
# column-wise sum
np.sum(dataset,axis=0)

# find the max. value of every row and column
np.max(dataset,axis=1)
np.max(dataset,axis=0)

# find the min. value of every row and column

np.min(dataset,axis=1)
np.min(dataset,axis=0)

# avg value
np.mean(dataset)
ap=np.mean(dataset,axis=1)
np.max(ap)

# some other numpy function
# repeating a value
a=np.array([1,2,3])
np.repeat(a,4)

# shuffle the dataset
np.random.shuffle(samp)
samp

# array broadcast
marks=np.random.randint(1,100,15).reshape(-1,5)
marks
weights=np.array([0.15,0.1,0.1,0.05,0.6])

marks*weights

# assignment
# create a price list of a store that has 20 items split into 4 categories
# price range from 1000-9000

price=np.random.randint(1000,9000,20).reshape(-1,4)
price
pre=np.array([1.5,1.5,1.5,1.5,])
price*pre

pre=np.array([0.10,0.10,0.10,0.10])

# create a 3x3 matrix and initialise it will 0
# generate 9 random number between 0-1 (with a 2 decimal precision) and fill the matrix column-wise
mat=np.zeros([3,3],np.float32)
mat
np.round(np.random.uniform(0,1,9),2)


--- 2/12/2020---numpy

# multi dimension
num=np.random.randint(15,200,30).reshape(-1,5)
num

num=np.random.randint(10,300,100).reshape(5,5,4)
print(num)
num.ndim
# mathmatical functions
arr1=np.array([12,4,5,4])
arr2=np.array([1,2,3,2])

np.add(arr1,arr2)
np.subtract(arr2,arr1)
np.multiply(arr1,arr2)
np.divide(arr1,arr2)

dir(np)
# set operations
arr1=np.array([16,5,14,7])
arr2=np.array([5,19,12,7])
arr1
arr2

# intersection
np.intersect1d(arr1,arr2)

# diffrence
# a-b
np.setdiff1d(arr1,arr2)
# b-a
np.setdiff1d(arr2,arr1)

###########################################

import scipy as sp
dir(sp)

from scipy import linalg
dir(linalg)

from scipy import stats
dir(stats)
