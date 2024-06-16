# not my program, just testing

s = "ADOBECODEBANC"
t = "ABC"

t_counter, window={},{}

for x in t:
    t_counter[x]=1+t_counter.get(x,0)

have, need=0,len(t_counter)
ans,ans_size=[-1,-1],float("infinity")
left=0

for right in range(len(s)):
    window[s[right]]=1+window.get(s[right],0)
    # print(window )

    if s[right] in t_counter and window[s[right]]==t_counter[s[right]]:
        have+=1

    while have==need:
        if(right-left+1)<ans_size:
            ans=[left,right]
            ans_size=(right-left+1)
        window[s[left]]-=1
        if s[left] in t_counter and window[s[left]]<t_counter[s[left]]:
            have-=1
        left+=1
print( s[ans[0]:ans[1]+1] if ans_size != float("infinity") else "")

print("tcounter:",t_counter)
print(window)
print("have:",have)
print("need",need)