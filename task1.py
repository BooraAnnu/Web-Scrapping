# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:30:37 2021

@author: hp
"""


import requests
import json
r = requests.get("https://my-json-server.typicode.com/typicode/demo/posts").json()
s = requests.get("https://my-json-server.typicode.com/typicode/demo/comments").json()

result = r+s
print("Combined data of both posts/comments are : ", result)