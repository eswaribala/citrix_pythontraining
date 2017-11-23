message="IBM Bluemix in operation"

version = 1.0

#concatenate operation
print(message+str(version))
#replication
print(5*message)
#slicing
print(message[2])
#range start pos inclusion and end position exclusion
print(message[5:12])
#in operator testing
print('M' in message)

print('X' not in message)

message="hello"
print(message.capitalize())

amount='43534'
print(amount.ljust(20,'*'),amount.rjust(20,'*'),amount.center(20,'*'))
print('$'*5,amount.ljust(20,'*'))

import base64

data=567
message=base64.b64encode(str(data).
                         encode('UTF-8',errors='strict'))
print(message)
#base64 decoding
decodedData=base64.b64decode(message)
print(decodedData)
#actual data
actualData=decodedData.decode(encoding='UTF-8',
                              errors='strict')

print(actualData)





