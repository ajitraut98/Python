# -*- coding: utf-8 -*-

Created on Tue Nov 24 14:10:48 2020


----chap=5 Dictionary
# create a blank dictionary
channel={}
type(channel)

'''
properties of key
1) unique
2)keys can be numeric/strings/alphanumeric
'''
# add k-v pairs to the dict.

channel[100] = "cricket"
# 100->key, "cricket" -> value
corresponding to the key

channel[101]="domestic cricket"
channel[102]="hindi movies"
channel[103]="hindi serials"
channel[104]="english movies"
channel[105]="english serials"
channel[106]="english news"

print(channel)
type(channel)
# create a dictionary that has following format
# {1:1,2:4,3:9,4:16....}
# do this for the first 20 numbers

numd={}
for i in range(1,21):
     numd[i] = i*i
print(numd)

# access a dictionary
# get the value for a given key
channel[101]
numd[14]

# if a key is specified that is not present, python raises an exception
channel[10]
channel["101"]="cartoon"
print(channel)

channel["101"]="songs"
print(channel)


# accessing the dictionary - other methods
channel.items()
# 1) to extract k, v in a loop
for k,v in channel.items():
    print("key={},value={}".format(k,v))

#2) get only the keys
channel.keys()

# to check if a key exists in a dictionary
# returns true if present/ false if not
125 in channel               
 OR
125 in channel.keys()
101 in channel

# 3) get only the values
channel.values()

# merge dictionaries

full_d=dict(list(channel.items()) + list(numd.items()))
print(full_d)
type(full_d)

# remove values from a dictionary

# specify the key
#k-v paired will be removed from the dictionaries

del numd[1]

1 in numd

# clearing contents
# del remove object permanantely
#clear() clear the data; but structure remains
del numd
print(numd)
numd={}
numd[1]=1; numd[2]=4

numd.clear()
print(numd)
type(numd)

######
# single_key -> multiple values

# create a table with the following attributes:
# ref_num, unique, range(100-999)
# score,  int(1-100)
# rating,  int (1-5)

# generate 50 records
# create 3 lists of values for ref_num,score,rating

import random as r
score=[]; rating=[]

ref_num=r.sample(range(100,999),50)
ref_num
for i in range(50):
      score.append(r.randint(1,100))
      rating.append(r.randint(1,5))

print(score[0:10])
print(rating[0:10])

# ensure the numbers are same in all lists
len(ref_num)
len(score)
len(rating)

# create the dictionary with 1key-multiple vallues
perf_d = {'ref_number':ref_num, 'score':score, 'rating':rating}
print(perf_d)

perf_d.keys()

# to get the data (first 5)
perf_d['score'][0:5]
perf_d['rating'][0:10]

# assignment
# create a dictionary (100 rows) having the following attributes:

# customer_id, int, unique
# name, char,
# gender, char [M,F]
# phone, int, unique

# email [name+domain] ---> create sample domains and pick one domain at random
# eg: if the domain is [yahoo,gmail,rediffmail,mail,mymail], then pick 1 value at random and join with the customer name

# age, int (>18)

# city [same technique as email .. create a list of cities and select 1 at random]


import random as r
import string as s

N=100

custid = r.sample(range(1000,9999),N)
phone = r.sample(range(6000000000,9999999999),N)
gender = ['m']*45 + ['f']*55
print(gender[0:70],end=",") 
r.shuffle(gender)

chars = list(s.ascii_letters)
r.shuffle(chars)

# for the convenience, fix the length of name=5

name=[]; email=[]; city=[]; age=[]

domain=['@gmail.com','@yahoo.co. in','@hotmail.com','@mycompany.in','@imarticus.com','@infy.in','@buisness.org']

l_city=['pune','mumbai','chennai','delhi','banglore','kolkata','ahmedabad','jaipur']

for i in range(N):
      rnd = r.randint(0,46)
      cname=''.join(chars[rnd:rnd+5])
      name.append(cname)

        # email
      rnd = r.randint(0,len(domain)-1)
      email.append(cname+domain[rnd])
     
        # city
      rnd = r.randint(0,len(l_city)-1)
      city.append(l_city[rnd])
     
        # age
      age.append(r.randint(18,100))

# check if there are 100 samples for each feature
len(custid)
len(name)
len(email)
len(city)
len(age)
len(phone)

# verify the data
name[90]
email[90]

# create the dictionary
d_customers={'custid':custid, 'name':name,
             'age':age,'phone':phone,
             'email':email,'city':city}

print(d_customers)

d_customers['custid']
d_customers['email'][0:10]
