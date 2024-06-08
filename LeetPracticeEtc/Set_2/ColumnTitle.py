import math
columnNumber=2**31 - 1
# columnNumber=10701
# columnNumber=701
s=""

while columnNumber:
    columnNumber,rem=divmod(columnNumber-1,26)
    s+=chr(65+rem)
    print(chr(65+rem))
    print(columnNumber)
print(s[::-1])

# x log 26 = log (2**31 - 1)

# x= math.log10(2**31 - 1) / math.log10(26)
# print(x)