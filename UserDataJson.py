# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 14:05:06 2017

@author: BALASUBRAMANIAM
"""
import requests

response= requests.get("http://jsonplaceholder.typicode.com/users")
print(response)

for user in response.json():
    print(user['name'],'\t',user['email'],'\t',user['address']['city'])
    
'''
finData=requests.get("https://www.quandl.com/api/v3/datasets/OPEC/ORB.json",verify=False)
print(finData)

print(finData.json()['dataset'])

directionsData=requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=Bangalore&destination=Pune",verify=False)
print(directionsData.json()['routes'][0]['bounds'])

'''




