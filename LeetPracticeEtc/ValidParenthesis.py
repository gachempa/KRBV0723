s="(){}[]"

sum_round=0
sum_square=0
sum_curly=0

for x in range(len(s)):
    if sum_curly==-1 or sum_round==-1 or sum_square==-1:
        # print("false")
        # print(x,bracket)
        break
    else:
        bracket=s[x]

        if bracket=="(" or bracket==")":
            if bracket=="(":
                sum_round+=1
            else:
                sum_round-=1
        elif bracket=="[" or bracket=="]":
            if bracket=="[":
                sum_square+=1
            else:
                sum_square-=1
        elif bracket=="{" or bracket=="}":
            if bracket=="{":
                sum_curly+=1
            else:
                sum_curly-=1
    
if sum_curly==0 and sum_round==0 and sum_square==0:
    print(1)
else:    
    print(0)
            
                