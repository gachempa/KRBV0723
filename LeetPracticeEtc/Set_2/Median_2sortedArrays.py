nums1 = [1,2]
nums2 = [3]

nums3=sorted(nums1+nums2)
# print(nums3)

len_final=len(nums3)
a,b=divmod(len_final,2.0)
# print(a,b)
if b==0:
    m1=nums3[int(a)]
    m2=nums3[int(a)-1]
    med=(m1+m2)/2
else:
    med=nums3[int(a)]

print(med)
