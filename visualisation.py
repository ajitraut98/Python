# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:18:55 2021

@author: user
"""

ch= visualisation

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

path="C:/Users/user/pp/superstore.xls"

store=pd.read_excel(path)

store.dtypes

store.Category.unique()

#1) total sales based on Category
np.round(store.groupby('Category').Sales.sum(),2)

#2)Average sales based on Category
np.round(store.groupby('Category').Sales.mean(),2)

#Total sales based on category 
# cross tab
pd.pivot_table(store,'Sales',['Category'],aggfunc=np.sum)

#avergae sales based on category- cross tab
pd.pivot_table(store, 'Sales',['Category'], aggfunc=np.mean)

#group by 2 columns
np.round(pd.pivot_table(store, 'Sales',['Category', 'Sub-Category'],aggfunc=np.mean),2)

store.dtypes()
store['Ship Mode'].unique()

#include index, row and column totals in cross
np.round(pd.pivot_table(store,index=['Category'], columns=['Ship Mode'], values='Sales', aggfunc=np.sum, margins=True, margins_name='Total'),2)

pd.set_option('display.expand_frame_repr', False)

store.dtypes

# what is the average profit based on Segment and Region?




## -------------------
# CHARTS
#---------------------

# i) line charts
# sales vs profits

sales=store.Sales
profit=store.Profit

plt.plot(sales,profit)
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Sales VS Profits')

# ii) scatter plot
plt.scatter(sales,profit)
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('scatter plot-sales-profits')


# iii) count plot
store.Gender.value_counts()
sns.countplot(x='Gender',data=store)
plt.title('Gender-wise order distrubution')


# region wise order

# iv) Bar Chart
# profits vs sales for region
sns.countplot('Region',data=store)
plt.title('Region-wise order')











# v) HISTOGRAM
plt.hist(store.Quantity)
plt.title('Quantity')
plt.xlabel('Quantity')
plt.ylabel('Count')

# vi) DISTRUBUTION PLOT

sns.distplot(store.Quantity,hist=False)
plt.title('Quantity')
plt.xlabel('Quantity')
plt.ylabel('Count')

# vii) BOX PLOT    (use for find outlier and distrubution)
store.boxplot('Discount', vert=False)
plt.title('Boxplot for Discount')


# viii) HEATMAP (to find the correlation among numeric features)

numc=store.select_dtypes(include=['float64','int64']).columns.values
print(numc)

# form the correlation matrix
cor = store[numc].corr()
print(cor)

# take the lower tringlr only for ploting
cor = np.tril(cor,k=0)
print(cor)

# heatmap plot
sns.heatmap(cor,annot=True,xticklabels=numc,yticklabels=numc,vmin=-1, vmax=1,square=False)


