import math
# columnNumber=2**31 - 1
columnNumber=10701

quo=int(columnNumber/26)
rem=columnNumber%26

print(quo)
print(rem)

# x log 26 = log (2**31 - 1)

x= math.log10(2**31 - 1) / math.log10(26)
print(x)