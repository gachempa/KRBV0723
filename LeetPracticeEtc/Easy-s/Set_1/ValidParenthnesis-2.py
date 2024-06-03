s="{[]}{}"

open_parens=[]
y=str()

for x in s:
    if x in ("([{"):
        open_parens.append(x)
    else:
        if x==")": y="(" 
        elif x=="]": y="["
        elif x=="}": y="{"
    
        if len(open_parens)>0 and y==open_parens[-1]:
            # print(f"x is {x} and last element in open_params is {open_parens[-1]}")
            open_parens.pop()
        else:
            open_parens.append(x)
            break
            
print(not bool(open_parens))
