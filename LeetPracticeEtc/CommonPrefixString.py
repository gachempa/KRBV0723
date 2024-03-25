strs=["flower","flow","flight"]
# strs=[]

len_strs=len(strs)
print(len_strs)
print(strs[0][0])

if len(strs)==0:
    print("")
else:
    commonindex=0

    for y in range(len(strs[0])):
        print(len(strs[0]))
        to_match=strs[0][y]
        print([idx for idx in strs if idx[y]==to_match])
