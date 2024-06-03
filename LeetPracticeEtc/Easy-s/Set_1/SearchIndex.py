nums = [1,3,5,6]
target = 4

if target in nums:
    print(nums.index(target))

else:
    nums.append(target)
    a=sorted(nums)
    print(a.index(target))

