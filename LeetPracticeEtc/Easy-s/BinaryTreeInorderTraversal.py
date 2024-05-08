# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()

    def insert(self,val):
        if self.val:
            if val<self.val:
                if self.left is None:
                    self.left=TreeNode(val)
                else:
                    self.left.insert(val)
            elif val>self.val:
                if self.right is None:
                    self.right=TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val=val

root=TreeNode(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(15)
root.PrintTree()