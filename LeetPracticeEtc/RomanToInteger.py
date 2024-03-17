s = "MMMCDXC"
# s="I"

dictionary1={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    "IV":4,
    "IX":9,
    "XL":40,
    "XC":90,
    "CD":400,
    "CM":900,
    }
value_integer=0

for x in range(len(s)):
    print("x,val :",x,s[x])
    if x>0 and s[x-1]+s[x] in dictionary1:
        print(s[x-1]+s[x])
        continue
    else:
        if x<len(s)-1 and s[x]+s[x+1] in dictionary1:
                # print(s[x]+s[x+1])
                value_integer=value_integer+dictionary1[s[x]+s[x+1]]
        else:
            value_integer=value_integer+dictionary1[s[x]]

print(value_integer)