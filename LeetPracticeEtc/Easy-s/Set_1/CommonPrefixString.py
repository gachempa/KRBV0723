strs=["flower","flow","floght"]

if len(strs)==0:
    print("")
else:
    sorted_strs=sorted(strs,key=len)
    # print(sorted_strs[0])
    min_strs=sorted_strs[0]
    # strs=[]

    len_strs=len(strs)
    # print(len_strs)
    # print(strs[0][0])


    commonindex=0

    for y in range(len(min_strs)):
        # print(len(strs[0]))
        to_match=min_strs[y]
        # print([idx for idx in strs if idx[y]==to_match])
        if len([idx for idx in strs if idx[y]==to_match])<len_strs:
            break
        else:
            commonindex+=1

# print(commonindex)

print(min_strs[0:commonindex])
