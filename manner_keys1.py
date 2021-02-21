# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:26:55 2020

@author: daxiguammm
"""

#Values from outside of your applocation
'''
Connecting to a database
Determining the operating system
Stteings which need to change
Sensitive data
'''

#Reading an environmental variable
import os
os_version = os.getenv('OS')
print(os_version)
#Now this will read any system or user environmental variable tha has been set

#Using dotenv
'''
Don't hard code
Don't check sensitive balues into source control
'''
#.env file
#That .env is for local purposes only This for my local dev
'''
DATABASE = Sample_Connection_String
'''

#app.py
from dotenv import load_dotenv
import os
load_dotenv()
database = os.getenv('DATABASE')
print(database)

#Final notes
'''
Don't haord code sensitive information **EVER**
Use dovtenv for a simple solution
Add .env to .gitignore
Consider full encryption options
Azuer Key Vault
'''









