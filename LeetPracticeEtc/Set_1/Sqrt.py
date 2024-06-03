import math

x = 0
n=int()
for b in range(x+1):
    print(b*b)
    if b*b<x:
        print("b2 <",b*b)
        continue
    elif b*b==x:
        n=b
        print("b2 =",b*b)
        break
    elif b*b>x:
        n=b-1
        print("b2 >",b*b)
        break

print(n)