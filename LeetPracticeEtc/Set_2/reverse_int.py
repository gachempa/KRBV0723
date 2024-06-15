x=-1234599999

if x<0:
    x=x*-1
    y=-1
else:
    y=1

rev_x=0

while x!=0:
    rem=x%10
    rev_x=rev_x*10+rem
    x//=10

rev_x=rev_x*y

if rev_x> 2**31 - 1 or rev_x< -2**31 - 1:
    rev_x=0

print(rev_x)