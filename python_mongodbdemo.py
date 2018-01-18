# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pymongo import MongoClient
 
#connect to the MongoDB.
conn = MongoClient('localhost',27017)
 
#Access the testdb database and the customer collection.
db = conn.citidb.customers
 
#create a dictionary to hold customer details.
 
#create dictionary.
cust_rec = {}
 
#set flag variable.
flag = True
 
#loop for data input.
while (flag):
   #ask for input.
   cust_name,cust_addr,cust_id = input("Enter customer name, address and id: ").split(',')
   #place values in dictionary.
   cust_rec = {'name':cust_name,'address':cust_addr,'id':cust_id}
   #insert the record.
   db.insert(cust_rec)
   #Ask from user if he wants to continue to insert more documents?
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
      flag = False
 
#find all documents.
ret = db.find()
 
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
 
#display documents from collection.
for record in ret:
	#print out the document.
	print(record['name'] + ',',record['address'] + ',',record['id'])
 
print()
 
#close the conn to MongoDB
conn.close()