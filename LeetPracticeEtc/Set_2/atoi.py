s = "  -+12"

sign="+"
loop_control=0
sum=int()
x=0
for a in s:
    if a==' ' and loop_control==0:
        continue

    if (a=='+' or a=='-') and loop_control==0:
        loop_control=1
        # print(a)
        if a=='-':
            sign="-"
        continue
        
    try:
        x=int(str(a))
        sum=sum*10+x
        loop_control=1
        print(x)
    except ValueError:
        print("false:",x)
        break

if sign=="-":
    sum=sum*-1

if sum <-2**31:
    sum=-2**31

if sum > 2**31-1:
    sum=2**31-1

print(sum)