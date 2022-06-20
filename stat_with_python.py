# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:06:53 2020

@author: user
"""

# statistic with python

import numpy as np
import scipy.stats as spstats
import matplotlib.pyplot as plt
import seaborn as sns

# central tendency

# create a dataset of 100 numbers (10-200)

data = np.random.randint(10,200,100)
len(data)

# mean
np.mean(data)

#median
np.median(data)

#wighted mean
#problem
# create a matrix of size 5x5 containing data between 1-100 that indicates a score

# weights for the columns are:
    '''
  leadership quality
  decision making,
  technical skills
  interpersonal skills
  managerial skills
    '''
# create scores for 5 employees
# calc the weighted mean of each employee using the given weights for the scores
# calc. the weightage average of each employee    
    
data=np.random.randint(1,100,25).reshape(5,5)
data
# weights
weights =
weights=np.array([0.35,0.2,0.1,0.1,0.2])

# weightage average
np.sum(data*weights,axis=1)    

# geometric mean    
data=np.round(np.random.uniform(100,120,5),2)
data    

np.array([])
    
    
############################################################################################
    
    
  # -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:07:45 2020

@author: user
"""
# statistic with python

import numpy as np
import scipy.stats as spstats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# central tendency

# create a dataset of 100 numbers (10-200)

data = np.random.randint(10,200,100)
len(data)

# mean
np.mean(data)

#median
np.median(data)

#wighted mean
#problem
# create a matrix of size 5x5 containing data between 1-100 that indicates a score

# weights for the columns are:
    '''
  leadership quality
  decision making,
  technical skills
  interpersonal skills
  managerial skills
    '''
# create scores for 5 employees
# calc the weighted mean of each employee using the given weights for the scores
# calc. the weightage average of each employee    
    
data=np.random.randint(1,100,25).reshape(5,5)
data
# weights
weights =
weights=np.array([0.35,0.2,0.1,0.1,0.2])

# weightage average
np.sum(data*weights,axis=1)    

# geometric mean    
data=np.round(np.random.uniform(100,120,5),2)
data    

ans=1
for x in data:
    ans = ans*x
print(ans)

import sympy
sympy.integer_nthroot(int(ans),len(data))

# mode

# find the mode of given dataset 
data=np.random.randint(1,6,50)
data
u_data = np.unique(data)
u_data
for i in u_data:
    ctr = list(data).count(i)
    print("number {}occur {} times".format(i,ctr))

### spread
data = np.random.randint(14,100,50)
print(data)

# range
np.max(data)-np.min(data)


# quartiles/deciles
np.percentile(data,25)
# get all the quartiles
# 25%--->value
# 50%--->value
# 75%--->value

perc = np.arange(25,76,25)
perc
np.percentile(data,perc)

# iqr
quartiles = np.percentile(data,perc)
quartiles[2] - quartiles[0]

# get all the deciles
perc = np.arange(10,101,10)
perc
deciles = np.percentile(data,perc)

# variance and standard deviation
np.var(data)
np.std(data)

# measure of association
# covariance and corelation     (diff. bet.covariance,corelation)

X=np.round(np.random.uniform(10,70,6),1)
Y=np.round(np.random.uniform(1,5,6),1)

len(X)
len(Y)

# what is the relation between X and Y


# covariance --> measure of direction
np.cov(X,Y)

# correlation --> measure of strength
np.corrcoef(X,Y)

########################################################
# INFERENTIAL STATISTIC

# hypothesis testing

# given z-score, what is the area
spstats.norm.cdf(1.96)

# given the area what is the z-score
spstats.norm.ppf(0.95)


# 1-sample t-test  (t-test done when sample size less than 30)

# problem statement: the average weight is 30kg

weights=np.round(np.random.uniform(16,60,11),2)
weights

# h0: mean is 30
# h1: mean is not 30
tail=2
tt= spstats.ttest_1samp(weights,30)
print(tt)

# Calculated
tcalc = tt[0]; tcalc
pval = tt[1]; pval

# Critical
alpha=0.05
dof = len(weights)-1
dof

# if its a 2-tail test, then split the alpha
if tail==2:
    alpha/=2
alpha

# find the t-critical
tcritical = abs(spstats.t.ppf(alpha,dof))
tcritical

# interpretation
# 1) check tcalculated and tcritical
if tcalc > tcritical:
    print("reject h0")
else:
    print("fail to reject h0")

# OR

# ii) check pvalue and alpha
if pval < alpha:
    print("reject h0")
else:
    print("fail to reject h0")

########################################################

# Z-TEST  (sample size is greter than 30)

# the average IQ of 100 people in the class is more than 95. test this sample at 95% CI

# claim: mean > 95
# opposite: mean<=95
# h0: mean = 95
# h1: mean > 95
tail = 1


iqscores = np.random.randint(90,180,100)
iqscores

z_test= spstats.ttest_1samp(iqscores,95)
print(z_test)

zcalc = z_test[0]; zcalc
pval = z_test[1]; pval

# if its a 2-tail test, then split the alpha
if tail==2:
    alpha/=2
alpha

# find the z-critical
zcritical = spstats.norm.ppf(1-alpha)
zcritical


# interpretation
# 1) check zcalculated and zcritical
if zcalc > zcritical:
    print("reject h0")
else:
    print("fail to reject h0")

#################################################################3################

# assignment
# write python functions to do the 2-sample hypothesis testing for means and proportions

# use the same data 


#2  2  sample test for variance are same

n1=249;n2=79;x1=20.14458;x2=30.48101;s1=6.41470;s2=6.10771
def variance(n1,n2,x1,x2,s1,s2,alpha=0.05,tail=2):
    n = (n1-1)*np.square(s1) + (n2-1)*np.square(s2)
    d = (n1+n2-2)
    sp = np.sqrt(n/d)
    tnumerator = x1-x2
    tdenominator = sp*np.sqrt((1/n1)+(1/n2))
    tstat = abs(tnumerator/tdenominator)
    if tail ==2:
        alpha/= 2
        zcritical = spstats.norm.ppf(1-alpha)
    if total > zcritical:
        print("Reject H0")
    else :
        print("Fail to reject H0") 
        print("2sample mean")
    return(tstat)
total = variance(249,79,20.14458,30.48101,6.41470,6.10771)
print("tstat={}".format(total))


i) assignment
#write function to do the 2sample hypothesis testing for means and proportion
#use the same data that was used in a class exercise.
'''2 sampe test for mean 
                proportion
                
'''                
#2 sample test for mean variance are different

'''
H0:population mean are same
H1:population mean are not same'''

def sample(n1,n2,x1,x2,std1,std2):
    n=x1-x2
    d=np.square(std1)/75 + np.square(std2)/50
    tt =  n/np.sqrt(d)
    tail=2
    alpha = 0.05
    if tail ==2:
        alpha/= 2
        zcritical = spstats.norm.ppf(1-alpha)
    if total > zcritical:
        print("Reject H0")
    else :
        print("Fail to reject H0") 
        print("2sample mean")
    return(abs(tt))
total = sample(75,50,28,33,14.1,9.5)
print("tt={}".format(total))



#2  2  sample test for variance are same


#3Testing equality of 2 population proportions


'''
H0:population mean are same
H1:population mean are not same'''

n1=800;n2=1000;x1=200;x2=350
def proportion(n1,n2,x1,x2):
    P1=x1/n1
    P2=x2/n2
    P = (x1+x2)/(n1+n2)
    Q = 1-P
    d=P*Q*(1/n1)+(1/n2)
    tt =  P1-P2 / np.sqrt(d)
    tail=2
    alpha = 0.05
    if tail ==2:
        alpha/= 2
        zcritical = spstats.norm.ppf(1-alpha)
    if total > zcritical:
        print("Reject H0")
    else :
        print("Fail to reject H0") 
    print("2sample mean for proportion")
    return(abs(tt))
total = proportion(800,1000,200,350)
print("tt={}".format(total))



# ANOVA testing

# create a dataset to store the petrol prices of 10 days of 5 indian cities
# claim: prices are similer

# H0: mu1=mu2=mu3=mu4=mu5
# H1: mu1<>mu2....

# create a list to store the petrol prices

delhi = np.round(np.random.uniform(69,99,10),1)
mumbai = np.round(np.random.uniform(70,96,10),1)
pune = np.round(np.random.uniform(68,92,10),1)
kolkata = np.round(np.random.uniform(67,88,10),1)
chennai = np.round(np.random.uniform(70,93,10),1)

# ANOVA test
ftest = spstats.f_oneway(delhi,mumbai,pune,kolkata,chennai)

fcalc = ftest[0]
pvalue = ftest[1]

print('fcalculated={},pvalue={}'.format(f_critical,pvalue))

pcritical= 0.05

# checking p-values
if pcalc < pcritical:
    print("reject h0")
else:
    print("fail to reject h0")


# find out the fcritical

dof_n = 4 # (number of group - 1)
dof_d = 45 # (from each sample, substract 1)

# alpha = 0.05

fcritical=spstats.f.ppf(1-0.05, dfn=dof_n,dfd=dof_d)

print(fcritical)

# checking the fscore
if fcalc > fcritical:
    print("reject h0")
else:
    print("fail to reject h0")


#######################################################################

# CHI-SQARE TEST

# maleria cases in 2 cities

city=['mumbai']*500 + ['delhi']*400
cases=['yes']*12 + ['no']*488 + ['yes']*7 + ['no']*393

data=pd.DataFrame({'city':city,'maleria':cases})
data

# cross tab of the data
ct = pd.crosstab(data.city,data.maleria)

# chisquare test

chisq = spstats.chi2_contingency(ct)
chisq

# OUPUT
# I) P-value
pcalc = chisq[0]
pcalc
pcrit = 0.05

# 2) chi square
chisq_calc = chisq[1]; chisq_calc

# 3) DOF
# 4) expected value matrix

if (pcalc < pcrit):
    print('reject h0')
    print('cases are dependent')
else:
    print('failed to reject h0')
    print('cases are independent')



















  
    
    





























