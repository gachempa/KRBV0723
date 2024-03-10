nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# solution 1, easy and simple using intersection of sets
s_nums1=set(nums1)
s_nums2=set(nums2)
result=s_nums1.intersection(s_nums2)

print(result)


# # solution 2
# mp={}
# for num in nums1:
#     mp[num]=mp.get(num,0)+1

# result=[]

# for num in nums2:
#     if num in mp:
#         result.append(num)
#         del mp[num]

# print(result)