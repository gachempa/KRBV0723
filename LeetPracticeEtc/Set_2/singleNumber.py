nums = [4,1,2,1,2]

single=set()

for n in nums:
    if n in single: single.remove(n)
    else: single.add(n)
single_list=list(single)
print(single_list[0])