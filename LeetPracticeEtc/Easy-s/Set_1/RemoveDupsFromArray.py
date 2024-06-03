nums=[0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums:list[int]):
    nums_set=set(nums)
    list_nums_set=sorted(list(nums_set))
    for x in range (len(nums_set)):
        nums[x]=list_nums_set[x]
    
    return len(nums_set)

print(removeDuplicates(nums))
print(nums)