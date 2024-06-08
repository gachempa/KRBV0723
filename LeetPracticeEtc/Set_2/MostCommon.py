from collections import Counter

nums=[2,2,1,1,1,2,2]
print(Counter(nums).most_common(1)[0][0])

#  using dictionary
dic_nums={}

for n in nums:
    if n in dic_nums:
        dic_nums[n]+=1
    else:
        dic_nums[n]=1
print(max(dic_nums,key=dic_nums.get))