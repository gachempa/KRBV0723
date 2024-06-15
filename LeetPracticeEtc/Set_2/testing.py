
s="abbcb"

numRows=5

if numRows == 1:
    print(s)

str1=[""]*numRows
i=0
di=1

for x in s:
    str1[i]+=x

    if i==0:
        di=1
    if i==numRows-1:
        di=-1
    
    i+=di

str_res=''.join(str1)
print(str_res)

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