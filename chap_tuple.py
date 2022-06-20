
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:43:17 2020
"""

----chap4-TUPLE


lang =('hindi','marathi','tamil','malyalam')
print(lang)
len(lang)
type(lang)

# access value of tuple
lang[0]
lang[0:3]

# tuples are immutable
lang[0]="marathi"

# concatenate tuple
lang = lang +('sanskrit','tulu','kokani')
print(lang)

# delete tuple (u can not delete iten=m in tuple)
del lang[0]

# packing and unpacking tuple
rec = ('cki11939','anand a','542452452','anand@co.in','wk1000')

# unpacking
custid,custname,phone,email,plan=rec
print(custid)
print(email)

# check for existance
'punjabi' in lang

# get the index of an element
lang.index('malyalam')

# how to make changes to a tuple
#method1--convert tuple--> list
lang = list(lang)
print(lang)
type(lang)

# change 'hindi', to 'Hindi'
lang[0]='Hindi'
print(lang)

lang[0].lower()

# convert list-->tuple

lang = tuple(lang)
print(lang)
type(lang)

# nested tuple
# companyname,est,loc,founder,emp
comp_db = (
    ('mycompany',2020,'pune','crs',20),
    ('sbi',1985,'bombay','mr a',125000),
    ('mrf',1970,'madras','memon',4000)
    )
print(comp_db)

# get only the company names from the tuple


for e in comp_db:
    print('company = ', e[0])

# to merge nested tuples
c1= (
    ('microsoft',1985,'california','bill',2500),
    ('yahoo',1996,'bay area','c-d',2000),
    ('tablue',2005,'chicago','xyz',1250)
    )
# merge with old one
comp_db=comp_db+c1
print(comp_db)

# zipping in tuple
stock=('ril','sbi','infy','wipro','tcs')
avgpr=(2100,350,1100,340,2700)
avgtr=(3000,700,2000,500,3500)

tuple(zip(stock,avgpr,avgtr))

# tuple of numbers
num = tuple(range(1,11))
print(num)
'''
# create a tuple of grocery items (about 10 diffrent items)

#columns
itemname/qty/price/totalprice
i) totalprice = qty*price (to be calc. programiticaly)
ii) calc.total bill amount
iii) identify the costliest and cheapest item (based on total price)

'''
groc = (
        ('rice',5,50,0),
       ('bread',1,40,0),
       ('sugar',10,47,0),
       ('salt',2,20,0),
       ('pulses',5,101,0),
       ('potato',3,40,0),
       ('eggs',1,70,0),
       ('cereal',1,245,0),
       ('tomato',3,24,0),
       ('juie',3,99,0)
       )
type(groc)
groc = list(groc)

total = 0

items=[]; price=[]


for i in range(len(groc)):
    groc[i] = list(groc[i])
    groc[i][3] = groc[i][1]* groc[i][2]
    total+= groc[i][3]
    groc[i]=tuple(groc[i])
    items.append(groc[i][0])
    price.append(groc[i][3])
    
# updated tuple with item-wise total
groc

# bill total
print(total)

total = total + amount
total+=amount

# max price
items[price.index(max(price))]


# min price
items[price.index(min(price))]

