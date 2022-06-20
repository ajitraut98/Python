# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:13:14 2020

@author: ajit
"""

# ch6: sets

# set is a keyword
a=set(['red','yellow','black','blue'])
print(a)
len(a)
type(a)
b=set(['black','red','pink','green','purple'])
print(b)

# common operation on sets 

#1) union (duplicate are excluded)

aub=a.union(b)

print(aub)
type(aub)

# 2) intersection (it shows comman value from 2 table)
a.intersection(b)
aib=a.intersection(b)
print(aib)

#3) minus
# a-b: elements in a not in b
a.difference(b)
# or
a-b

#b-a elements in b not in a
b.difference(a)
#or
b-a

# 4)symmetric diffrences
# elements present in either a or b, but not in both
a.symmetric_difference(b)

# convert list having duplicated values into a unique list
mylist=['table','chair','table','table','fan','cat','cat','fan','car','fan']
mylist.sort()
print(mylist)

set(mylist)


mylist=list(set(mylist))
mylist.sort()
print(mylist)

