# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:52:11 2020

@author: daxiguammm
"""
#1
#List
#List are collections of items
names = ['Mike','Susan']
print(names)

#You can start with a empty list
scores=[]
scores.append(98)#Add new item to the end
scores.append(99)
scores.append({'first':'Bill','last':'Mike'})
print(scores)
print(scores[1])#Collections are zero-indexed
#List是从0开始的

#2
#Arrays
#Arrays are also collections of items
from array import array
scores2 = array('d')#声明数组类型
scores2.append(97)
scores2.append(98)
print(scores2)
print(scores2[1])

#What's the difference bween List and Array
#Array:Simple types such as numbers 
#Array:Must all be the same type
#List:Store anything
#List:Store any type

#Common operations
names = ['Susan','Mike'] 
print(len(names))#Get the number of items
names.insert(0,'Bill')#Insert before index
print(names)
names.sort()#排序
print(names)

#Retrieving ranges
names = ['Susan','Mike','Bill']
presenters = names[0:2]#Get the first two items
#上面括号中，第一个参数0是指开始的位置
#第二个参数是指需要抓取的个数
#Starting index and number of items to retrieve
print(names)
print(presenters)

#3
#Dictionaries
person = {'first':'Mike'}
person['last'] = 'Harrison'
print(person)
print(person['first'])

#What's the difference btween List and Dictionaries?
#Dictionaries:Key/Value paris
#Dictionaries:Storage order not guaranteed
#List:Zero-based index
#List:Store order guaranteed















