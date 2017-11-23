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
dirPath=dirPath+"/"+fileName+".txt"

if(os.path.exists(dirPath)):
    print("File Exists")
    fileRef=open(dirPath,mode='a')
else:
    print("File Not Found")
    fileRef=open(dirPath,mode='w')
    print("File Created")

import random

for i in range(1,100):
    fileRef.write(str(random.randint(1,1000))+"\n")
fileRef.close()    
print("Contents Written")
    


