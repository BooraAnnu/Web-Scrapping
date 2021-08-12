# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:43:38 2021

@author: hp
"""
import requests

for page in range(1,13):
    #print(page)
    url = "https://reqres.in/api/users?page=page/"
    data = requests.get(url).json()
  
import json
print(data)
print("Total number of users are : ", len(data))
