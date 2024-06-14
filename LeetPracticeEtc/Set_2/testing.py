
s="abbcb"
max_pdrome=""
for i in range(len(s)*2):
    r=i//2
    l=(i-1)//2
    # print(i,r,l)

    while l>=0 and r<len(s) and s[l]==s[r]:
        # print(s[-1])
        l-=1
        r+=1
    pdrome=s[l+1:r]
    max_pdrome=max_pdrome if len(max_pdrome)>len(pdrome) else pdrome

print(max_pdrome)

# for x in range(1):
#     print(x)

# nums1 = [1,2]
# nums2 = [3]

# nums3=sorted(nums1+nums2)
# print(nums3)
# nums4=nums1+nums2
# nums4.sort()
# print(nums4)
# print(nums4[1])