# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:06:03 2020

@author: daxiguammm
"""

#Many web services return data as JSON
#JSON is a standard data format that can be intimidating at first glance
#Like the results to API

#Using a linting tool to format JSON makes it easier to read

#READ JSON

#Create JSON
import json
#Create a dictionary object
person_dict = {'first':'Christopher','last':'Harrison'}
#Add additional key pairs as needed to dictionary
person_dict['City']='Seattle'

#Convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)

#Nest dicitonaries to create JSOn in the format 
person_dict = {'first':'Christopher','last':'Harrison'}
staff_dict={}
staff_dict['Program Manager']=person_dict
staff_json = json.dumps(staff_dict)
print(staff_json)


#Add lists to the dictionary to create JSON in the format 
person_dict = {'first':'Christopher','last':'Harrison'}
languages_list = ['CSharp','Python','JavaScript']
person_dict = json.dumps(person_dict)
print(person_json)

