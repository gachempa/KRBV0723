nums=[2,7,11,15]
target=9

# create dictionary with key as the number in list and value as its index in list
target_dict={}

for x in range(len(nums)):
    num2=target-nums[x]
    if num2 in target_dict:
        a=target_dict[num2]
        b=x
        break
    else:
        target_dict[nums[x]]=x

print(a,b)

    

