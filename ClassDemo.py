'''
Created on 24-Nov-2017

@author: BALASUBRAMANIAM
'''
class Member:
    Offer=.5
    def __init__(self):
        self.__customerId=0
        self.__customerName=''
      
          
    def getCustomerId(self):
        return self.__customerId
    def setCustomerId(self,id):
        self.__customerId=id
'''
member=Member()
member.setCustomerId(5896798)
print(member.getCustomerId())
print(Member.Offer)
'''        