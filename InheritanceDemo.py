'''
Created on 24-Nov-2017

@author: BALASUBRAMANIAM
'''
from day3.ClassDemo import Member
class CorporateMember(Member):
    def __init__(self,privileges):
        #Member.__init__(self)
        self.__privileges=privileges
        
    def getPrivileges(self):
        return self.__privileges
    
corporateMember=CorporateMember("Golf")
print(corporateMember.getPrivileges())