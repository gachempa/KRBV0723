# to test recursion concepts

# def factorial(n):

#     return 1 if n==1 else ((n*factorial(n-1)))

# print(factorial(5))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

nums=[-10,-3,0,5,9]
# nums=[1,2]

def createTree(_nums:list,_bTree):

    if len(_nums)==0:
        _bTree.append("")
        return
    elif len(_nums)==1:
        _bTree.append(_nums[0])
        return
    else:
        mid=int((len(_nums)+1)/2)-1
        _bTree.append(_nums[mid])
        leftarray=_nums[0:mid]
        rightarray=_nums[mid+1:]
        TreeNode(nums[mid])
        TreeNode.left=createTree(leftarray,_bTree)
        TreeNode.right=createTree(rightarray,_bTree)
    return _bTree    

bTree=[]
ansBST=createTree(nums,bTree)
print(ansBST)

# mid=int((len(nums)+1)/2)-1
# left=nums[:mid]
# right=nums[mid+1:]
# print(nums[mid])
# print(left)
# print(right)