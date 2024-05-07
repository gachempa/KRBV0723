nums1 = [1,2,3,0,0,0]; m = 3
nums2 = [2,5,6]; n = 3

# nums1 = [0]; m = 0
# nums2 = [1]; n = 1

# nums1 = [2,0]; m = 1
# nums2 = [1]; n = 1

n1_idx=m-1 
n2_idx=n-1
for x in range(m+n-1,-1,-1):
    if n1_idx+1 and n2_idx+1:
        if nums2[n2_idx]>=nums1[n1_idx]:
            nums1[x]=nums2[n2_idx]; n2_idx-=1
            print(1,x,nums1[x])
        else:
            nums1[x]=nums1[n1_idx]; n1_idx-=1
            print(2,x,nums1[x])
    elif n2_idx+1:
        nums1[x]=nums2[n2_idx]; n2_idx-=1
        print(3,x,nums1[x])
    elif n1_idx+1:
        nums1[x]=nums1[n1_idx]; n1_idx-=1
        print(4,x,nums1[x])

print(nums1)
