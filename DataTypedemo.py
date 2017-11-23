#read room temperature and lights status

roomTemp=input("Enter the temperature")
print("Type of the Data",type(roomTemp))
print("Room Temperature=%s"%(roomTemp))

lightStatus=True
print("Type of the Data",type(lightStatus))
#convert data from one format to another
#101--binary number convert to decimal
#result 5
binaryNumber='101'
print(int(binaryNumber,2))
print(int("0xFF",16))

#complex number
sciData=5+7j
print("Real Data= %d"%(sciData.real))
print("Real Data= %d"%(sciData.imag))

#conversion from string to int
#convType=int(roomTemp,10)
#print(type(convType))
#print("Room Temperature%d"%(convType))

#bit operators
inData=7
outData=10
print("Bit operation=",inData & outData)












