nums=[0,1,2,2,3,0,4,2]
val=2

def removeElement(nums, val):
    while val in nums:
        nums.remove(val)

removeElement(nums,val)
print(nums)