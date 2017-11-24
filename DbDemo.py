# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:54:28 2017

@author: BALASUBRAMANIAM
"""

import pymysql

def createConnection():
    conn = pymysql.connect(host="localhost",user="root",
                   passwd="vignesh",
                   db="anz_bankdb")
    return conn


def fetchAllRecords():
    conn=createConnection()
    query = "select * from Customer"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def fetchByCustomerId(customerId):
    conn=createConnection()
    cursor=conn.cursor()
    cursor.execute("""select * from Customer where 
    Customer_Id='%d'""" %(customerId))
    return cursor.fetchall()

def insertCustomer():
    conn=createConnection()
    cursor=conn.cursor()
    query ="""insert into  Customer values(1001,'jacob',
    34543,'8056789900')"""
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print("Exception occurred")
        conn.rollback()
        
    
    
insertCustomer()
#rows=fetchByCustomerId(45686)

#rows=fetchAllRecords()
#for row in rows:
    #print(row)

    #for col in row:
        #print(col,end='\n')
        

 




 


