# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:06:29 2017

@author: BALASUBRAMANIAM
"""

import os
dirPath=r"f:/yatrabakup/BankingDir"

if(os.path.exists(dirPath)):
    print("Directory Exists")
else:   
   #create sub directory
   subdir=input("Enter Sub Dir Name")
   os.mkdir(dirPath+"/"+subdir, mode=0o777)
   print("Directory created")
   
fileName=input("Enter File Name")
dirPath=dirPath+"/"+fileName+".csv"

if(os.path.exists(dirPath)):
    print("File Exists")
    fileRef=open(dirPath,mode='r')
    #print(type(fileRef)) 
    lineArray=fileRef.readlines()
    for row in lineArray[1:]:
        colArray=row.split(",")
        #for col in colArray:
        print(colArray[2])
        




