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
    print(window )

    if s[right] in t_counter and window[s[right]]==t_counter[s[right]]:
        have+=1

print("tcounter:",t_counter)
print(window)
print("have:",have)
print("need",need)