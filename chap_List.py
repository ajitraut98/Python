# -*- coding: utf-8 -*-
"""

created on thu nov 12/11/2020

"""
# python started
# ch1: variables/data types

# define the initialisation 
radius = 1

# print the value assigned to the variables
print("the value of radius=",radius)

# print the data type of the 
totalsales = 0
print('sales done at 9 am =',totalsales)
# transaction amount

# total sales should reflect the transaction amount details
totalsales + current transaction
totalsales = 0
trans_amt = 155.75
totalsales = totalsales + trans_amt

# a1)
# print the updated totalsales value
print("totalsales =", totalsales)

#a2)
trans_amt = 1093+5100
totalsales = totalsales + trans_amt
print("totalsales =", totalsales)

# find the data types of total sales
type(totalsales)

# radius of the circle
PI = 3.14
radius = 1
area = PI * r * r
print("area of circle with radius 1=", area)

PI = 3.14
r = 5.26
area = PI * r * r
print("area of circle with radius 5.26=",area)


PI = 3.14
r = 7.7
area =round( PI * r * r,2)
print("area of circle with radius 7.7=",area)

# substraction (-)
# a product has a discount of 20 rs calc. the net price

price = 356
disc = 20

print('price before discount=',price)
print('price after discount=',price-disc)

# division (/)
price = 1560
disc = 5 # discount is in %

discprice = price- (disc/100)*price
print(discprice)

# print multiple values as output
print("actual price = {}, discounted price = {}" .format(price,discprice))


# calc. 3 successive discount of price 15000
price = 15000
disc = 2 # discount is in %
discprice = price- (disc/100)*price

price = 14700
disc = 5 # discount is in %
discprice = price- (disc/100)*price

price = 13965
disc = 10 # discount is in %
discprice = price- (disc/100)*price

# other math operators
# power
5*5*5*5
pow(5,4)

#square root
pow(25,1/2)

# i want integer part only
#type conversion
int(pow(25,1/2))

#cube root
pow(125,1/3)

#absolute
abs(-985)
abs(545)

abs(-5)+(-10)

---friday lec2 date-13/11/2020

## import liabraries in python

#libraries for math
import math
# to get all the function of the math libraries
dir(math)

#usage of function
#<libraryname>.<function_name>(input)

# factorial of 6
math.factorial(3)

number = 150
#natural log
math.log(number)
# truncate the ans 2 digit
lognumber = round(math.log(number),2)
print(lognumber)

# calc the log base 2 of the number 150. restrict to decimal 3
# store result in a variable
# method 1 -> log2
dir(math)
number = 150
math.log2(number)
lognumber = round(math.log2(number),3)
print(lognumber)

# method 2 -> log(number, base)
lognumber =round(math.log(number,2),3)
print(lognumber)

# calc the log base 10 of num 150

lognumber = round(math.log(number,10),3)
print(lognumber)

# cieling () : returns the next highest value of the integer portion of a float
number = 18.453
math.ceil(number)
    
    
    
# floor() : it return the integer part of the float number only
number = 51.4947
math.floor(51.4947)

# solve the following:
x^3 + y^4 - 3xy -> x=3; y = -2
x = 3
y = -2
pow(x,3) + pow(y,4) - (3*x*y)

# 2) 2a-3b+6ab-5a^2b^2 --a=6, b=8
a=6
b=8
(2*a)-(3*b)+(6*a*b) - 5*(pow(a,2))*pow(b,2)


# 3 sides of triangle
a=17
b=21
c=10

s=(a+b+c)/3
print(s)
s=16
round(pow(s*(s-a)*(s-b)*(s-c),1/2))

# constant values
math.e
math.pi
# sequence of numbers

# in python, number starts from 0
typecast the output of range() into a list datatype to view the results
print(list(range(10)))
# i want range between 1-10
print(list(range(1,11)))
# i want range between 20-50
print(list(range(20,51)))

# create a sequence of numbers with a diffrence other than 
# diffrence from 1-50, diff=4
list(range(1,51,4))

# print the 1st 20 numbers divisible by 6
print(list(range(6,6*20+1,6)))

#generate sequence in the reverse direction (descending order)
list(range(50,1,-5))

# random numbers
'r' -> alias name for the library function
import random as r
dir(r)

# generate 1 random number between 1-10
#method 1
r.randint(1,10)

#method 2
r.choice(range(1,20,))

# store the result
rnum = r.randint(1,10)
print('random number =',rnum)
type(rnum)

# generate 1 random float number
round(r.uniform(10,50),3)

----tuesday 17/11/2020


# how to generate multiple random
r.randint(10,50)
r.uniform(10,50)

# use the loops  (to generate random multiple)
# loops -> repeated iteration

# i want to generate 5 random integer 
# i will run a loop 5 times
for i in range(5):
    print(r.randint(10,50))

# to get the output in horizontal form
for i in range(5):
    print(r.randint(10,50),end=",")



# simillary you can generate more than 1 random float values

#a1
#
# generate 10 float values between  90 and 110; with a decimal precision of 2

for i in range(10):
  print(round(r.uniform(90,100),2),end=",")

# random numbers with a specific interval
for i in range(10):
   print(r.randrange(5,50,6))

for i in range (15):
    print(r.randrange(10,100,4))


------ ch2 strings--

str1 = 'c' #single char
str2 = "ajit" #multiple char

print("str1=",str1)
print("str2=",str2)

#get the total number of character(length)
len(str1)
len(str2)

# create charachter vector
str3="india is my country"
len(str3)

# access individual characters
# get the 1st element
str3[0]

# substring
# get the first 5 elements
str3[0:5]

# get the last letter of the vector
str3[len(str3)-1]
str3[-1]
# get the last 'n' elements
# eg: get the last 5 character 
last5 = str3[-5:]
print('the last 5 characters are',last5)

# join the 1st 10 and the last 10 characters
str3[0:10]+str3[-10:] 

# dynamic string building
msg = "there are 365 days in a year"
print(msg)
type(msg)
 
mth=88; sc=84; lang=72
total = mth+sc+lang
av = round(total/3,1)

print("maths score = {}, science score = {}, language score = {}, total = {}, average ={}"
      .format(mth,sc,lang,total,av) )

# generate random values for maths,science and language (marks should be integers between 1-100)
for 10 students.:
# the output should be
'''
student=1, then followed by the same output as above

eg:
student 1 maths=67 sc=90 lang=67 total=224 avg=73
student 2 maths= sc= lang=, total=, avg=
student 3 maths= sc= lang=, total=, avg=
student 4 maths= sc= lang=, total=, avg=
'''


for i in range (10):
    mth=r.randint(1,100)
    sc=r.randint(1,100)
    lang=r.randint(1,100)
    total=mth+sc+lang
    av = round(total/3,1)

    print("student {},maths score = {}, science score = {},language score = {},total = {},average = {}" 
          .format(i+1,mth,sc,lang,total,av))
    
# repeat values
"m " * 5
"f " * 4
"hello " * 10

str3
# from "str3", starting from the 1st position, get every 3rd chatacter
str3[::3]

# if no number is specified before the :,
python automatically takes the starting position=0 and ending position=last

# find words within a string

str4="python is a programming language.python is also a snake.python is easy to learn and use,python is a dangerous reptile,python is used a lot in data science."

word_to_find = "python"

# count the number of occurance (how many times occured)
str4.count(word_to_find)

str4.count("python")

# since the python is case sensitive, the count is 0

# find if a given string exists in a sentences
#returns true if found; else returns false

word_to_find in str4
"apple" in str4

# find the 1st occurance of a given word
# returns the index position
str4.find(word_to_find)
# str4.find("")

# returns the last occurance of a given word__returns the index position
str4.rfind(word_to_find)
str4

# check if the sentence start with a pattern
#returns true if it matches;else return false

str4.startswith(word_to_find)
str4.startswith("language")

# check if sentence ends with pattern
#returns true if it matches;else return false

str4.endswith("later")
str4.endswith("science")

# find and replace
# replace "python" with "cobra"
str4.replace("python","cobra")

# to save the result of the find and replace,assign the result back to the variable
str4.replace("python","cobra")
print(str4)

# some common string operations
word = "program"

# convert to uppercase 
word=word.upper()
print(word)

# convert to lowercase
word.lower()

# change only the first character to uppercase
word.capitalize()

# remove spaces
word = "   python program    "
# return 21 that include spaces
len(word)

# remove spaces from left side of the word
word.lstrip()
len(word.lstrip())

#remove spaces from right side of the word
word.rstrip()
len(word.rstrip())

#remove spaces from right and left side of the word
word.strip()
len(word.strip())


--- 18/11/2020

sent1="  this is a sentence  \t\t\t that has \n\n\n some white spaces  need to remove  "
print(sent1)
sent1.strip()


#to format this string
# i) split the sentence into words on the default delimiter 'whitespace'

sent1.split()
words = sent1.split()
print(words)
# ii) join words to make a sentence
' '.join(words)

# combine this into a single line
' '.join(sent1.split())

str2="16328$color tv$yes$14643"
print(str2)
str2.split("$")

# library for strings
import string
dir(string)
string.ascii_uppercase
string.ascii_lowercase
string.punctuation

# concatenete the strings
string.ascii_uppercase + string.ascii_lowercase
string.digits

# set the directory path to read file(s)
path="f:\new\term1\data.csv"
print(path)

# fixes
# method1
path="f:/new/term1/data.csv"
print(path)
# method2
path="f:\\new\\term1\\data.csv"
print(path)

# to get current working directory
import os
os.getcwd()



------- chap3_list

colors=['green','yellow','red','orange']
print(colors)
type(colors)

# count the elements
len(colors)

# accessing the elements
colors[0]
colors[0:3]

# lists are mutable - value can be changed
colors[0] = "crimson"
print(colors)
# change the value of 'red' to 'blood red'
colors[-2] = "blood red"
print(colors)

# slicing a list(subset)
c1 = colors[0:3]
print(c1)
type(c1)

# get all the colors in the even position
colors[1::2]

# create a list
list1 = ['a','b','c']
print(list1)

# make a copy
l_copy1 = list1
print(l_copy1)
# make a changes to the copy
l_copy1[0] = 'apple'
print(l_copy1)
print(list1)

#contents in both lists will change
#this is a called "shallow copy"

# copy2
l_copy2 = list1.copy()
print(l_copy2)
print(list1)

# make a changes to the copy
l_copy2[1] = 'biscuit'
l_copy2[2] = 'cat'
print(l_copy2)
print(list1)

# add elements to a list 
#1) always at the end
colors.append('brown')
print(colors)
colors = colors + ['silver']
print(colors)

#2) at any position
colors.insert(1,"violet")
print(colors)

# add the color "gold" in the place of "silver"
ndx = colors.index('silver')
colors.insert(ndx,"gold")
print(colors)
ndx

# add a color

colors.insert(colors.index("blood red"),"black")
print(colors)

# remove elements from the list
del colors[colors.index("brown")]
print(colors)

# method 2 remove
colors.remove("blood red")
print(colors)


# sort a list  (sort order is ascending order)
colors.sort()
print(colors)

# descending sort
colors.sort(reverse=True)
print(colors)

# list is iterable
print(colors)

# when object is iterable, the values can be fetched in 2 ways
i) get the value directly
    for c in colors:
        print("color is",c)

# print the name and length of each color from the color list
print(colors)
len(colors)

for c in colors:
    print("color is {}, length is {}".format(c,len(c)))


---19/11/2020

--- get the value based on index
for i in range(len(colors)):
    print('color is', colors[i])


# heterogeneous list
#packing
rec=[10903,'ajit','m',75.2,175,'True']
print(rec)
type(rec)

# unpacking
# getting the individual values stored in variable
sid,name,gender,wt,ht,status = rec
print(sid)
print(name)
print(gender)
print(wt)
print(ht)
print(status)

# zipping
country=['india','usa','uk']
capital=['new delhi','wdc','london']
currency=['rupees','dollar','pound']

list(zip(country,capital,currency))

# will give a error if value not found;else return the index position

#numeric list
num = list(range(1,21))
print(num)
type(num)
# get the first 3 numbers
num[0:3]

# empty list
r_num = []

# create 50 random integers (1,100) and fill them in the r_num list
import random as r
for i in range(50):
    r_num.append(r.randint(1,100))

print(r_num)

# max. value
max(r_num)

# min.value
min(r_num)

# sum total of values
sum(r_num)

# find the avg. of list
sum(r_num)/len(r_num)

# nested list --- every element is a list
nested= [
    list(range(1,50,3)),
    list(range(5,50,6)),
    list(range(7,50,4))
    ]
len(nested)
# get the individual element
nested[0]
nested[1]
nested[2]
nested[0][0:5]

# get top 3 values
n = nested[2][-3:]
n.sort(reverse=True)
opoi87

# shuffle the data
el = nested[0]
el
r.shuffle(el)
print(el)

# create a nested list  to store the tables of 2-10 in the following foramt

2,4,6,8,10.......20
3,6,9.............30
4,8..............40
...
..
10,20.............100


tables=[]
for i in range(2,11):
      tables.append(list(range(i,(i*10)+1, i)))

print(tables)

# list concatenation
colors
country
newlist = colors+country

num1=[1,2,3,4]
num2=[5,6,7,8]
num1+num2



















