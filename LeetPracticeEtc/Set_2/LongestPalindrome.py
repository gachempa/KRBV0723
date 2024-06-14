s="bbcc"

res = ''
        
for i in range(len(s)*2-1):
    print("i is",i)
    
    l, r = i // 2, (i + 1) // 2
    print("l is",l)
    print("r is",r,"\n")    
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        print("l is",l)
        print("s[l] is",s[l])
        print("r is",r,"\n")
        
    res = res if len(res) > len(s[l+1:r]) else s[l+1:r]
    print(res)
# print(res)