s = "abcabcbb"
# s = "a"
# print(len(s))
s2_count,max_s=0,0
sub_s=set()

for i in range(len(s)):
    while s[s2_count] not in sub_s:
        sub_s.add(s[s2_count])
        max_s=max(max_s,len(sub_s))
        if s2_count<len(s)-1:
            s2_count+=1
        print(sub_s)

    sub_s.remove(s[i])
    # print("----")

print(max_s)