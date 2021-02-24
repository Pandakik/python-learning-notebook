# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:22:02 2020

@author: daxiguammm
"""

#What is a web service?
"""
When a developer wants to share the functionality of a function
but not the actual code ub the program,they can place the function on a 
web server.

A programmer with the address of that function on the web server adn
the requrired permissions can call the function

This is called a  web service
从Web service 上访问别人的程序
"""

#What is an API
"""
You can't call a function unless you know the function name and the rqurired
parameters
When you create a service you create an Application Progtamming interface(API)
The API defins the function names and parameters so others know how to call
your function.
"""

#Keys allow me to track which users have permission to use my web sercive
"""
A develper signs up on web site,or buys a license for my software and is provided
a unique key

When the developer calls my web service they provide their unique key and 
I am able to verify the key has been approved for calls to my web service
"""

#There is a standard for sending messages across the web
#Hypertex Transfer Protocol(HTTP) is a standard protocol for sending messages across the web
#GET
'''
Pass values in query string only
Special characters must be 'escaped'
LLimited amount of data
'''
#POST
'''
Pass values in query string and body
No need to escape special characters if passed in body
Can pass ;arge amounts of data,including images,in body
'''





















