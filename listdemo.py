dataSet=[6,'message',78.9,True]

#print(dataSet)
dataSet.append(0xFF)

#print(dataSet)

#for loop
for data in dataSet:
    if(type(data)==str):
        print(data,end="\t\t")
    else:
        print(data,end="\t")


#dynamic list
customerIdList=[]
import random
for _ in range(1,10):
    customerIdList.append(random.randint(1,10000))
print("\nBefore Sorting....",customerIdList)
#sorting
customerIdList.sort();
print("\nAfter Sorting....",customerIdList)
#reverse the list
customerIdList.sort(reverse=True)
print("\nAfter Reverse Sorting....",customerIdList)

#nested list

customerData=[2342,['Arun','Chennai,9952031456'],
              43543,['Anitha','Bangalore',39569357]]

for _ in customerData:

    if type(_)==int:
        print("\n",_)
    else:
        for innerData in _:
            print(innerData,end="\t")


#zip
employeeNames=["Suja","Ani","Sam"]
projects=["HSBC","HDFC","SBI"]
location=["Pune","Chennai","Gurgaon"]
outerList=[]
for (name,proj,loc) in zip(employeeNames,projects,location):
     innerList=[]
     innerList.append (name)
     innerList.append(proj)
     innerList.append(loc)
     outerList.append(innerList)

#join operator
for _ in outerList:
   print('-->'.join(_))






