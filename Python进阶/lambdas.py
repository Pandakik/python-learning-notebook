# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:56:59 2020

@author: daxiguammm
"""

#Let's sort some objects
presenters = [
    {'name':'Susan','age':50},
    {'name':'Christopher','age':47}        
]


#presenters.sort()   #直接用sort函数会出错
#print(presenters)

#Notes about sort
'''
sort can automatically handle primitive types and strings
If we need to do anything complex whether to sort by age or name

the key parameter allows you pass in a function to call for each lisst element
before it compares items for sorting
'''

#Let's sort by name
def sorter(item):
    return item['name']

presenters = [
    {'name':'Susan','age':50},
    {'name':'Christopher','age':47}        
]

presenters.sort(key=sorter)#按名字排序
print(presenters)


#Lam用于排序时不用调用函数
#Let's do the same thing inline

presenters = [
    {'name':'Susan','age':50},
    {'name':'Christopher','age':47}        
]

presenters.sort(key=lambda item: item['age'])
print(presenters)


#How lambdas work
'''
def sorter(item):
    return item['name']
    
lambda item: item['name']    
'''

#Let's sort by name length(short to long)
presenters = [
    {'name':'Susan','age':50},
    {'name':'Christopher','age':47}        
]
presenters.sort(key = lambda item: len(item['name']))
print('---length---')
print(presenters)







