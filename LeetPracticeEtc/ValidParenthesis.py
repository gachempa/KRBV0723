s="{[}]"

sum_round=0
sum_square=0
sum_curly=0

if len(s)<2:
    sum_round=-1
else:

# to keep track of parenthesis opened create a list
# use 1 for round, 2 for square and 3 for curly - brackets opened
    opened_parenthesis=[]
    n_opens=0 # to track count of opened parenthesis for indexing

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
                    opened_parenthesis.append(1)
                    n_opens+=1
                elif n_opens>0 and opened_parenthesis[n_opens-1]==1:
                    opened_parenthesis.pop()
                    n_opens-=1
                    sum_round-=1
                else:sum_round=-1
            elif bracket=="[" or bracket=="]":
                if bracket=="[":
                    sum_square+=1
                    opened_parenthesis.append(2)
                    n_opens+=1
                elif n_opens>0 and opened_parenthesis[n_opens-1]==2:
                    opened_parenthesis.pop()
                    n_opens-=1
                    sum_square-=1
                else:
                    sum_square-=1
            elif bracket=="{" or bracket=="}":
                if bracket=="{":
                    sum_curly+=1
                    opened_parenthesis.append(3)
                    n_opens+=1
                elif n_opens>0 and opened_parenthesis[n_opens-1]==3:
                    opened_parenthesis.pop()
                    n_opens-=1
                    sum_curly-=1
                else:
                    sum_curly-=1
    
if sum_curly==0 and sum_round==0 and sum_square==0:
    print(1)
else:    
    print(0)
            
                