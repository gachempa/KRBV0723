

# Creating binary tree from given list 
from binarytree import build 

# List of nodes 
nodes =[3, 6, 8, 2, 11, None, 13,4,3,None,2,None,None,3,4,None,None,5] 
  
# Building the binary tree 
binary_tree = build(nodes) 
print('\nBinary tree from list:\n', binary_tree) 
  
# Getting list of nodes from binarytree 
print('\nList from binary tree:\n',binary_tree.values) 

print('\nMax node value:',binary_tree.max_node_value)
print('Tree height:   ',binary_tree.height)
print('Max leaf depth:',binary_tree.max_leaf_depth,'\n')

def mytest(balanceTree):
    if balanceTree.height==0: return True
    print(balanceTree.values[0])
    print(balanceTree.values[1])

mytest(binary_tree)


