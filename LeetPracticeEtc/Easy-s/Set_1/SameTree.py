# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        print(p.val==q.val)


p = TreeNode([1,"",2])
q = TreeNode([1,"",2])

Solution.isSameTree(p,p,q)