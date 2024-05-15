

# Creating binary tree from given list 
from binarytree import build 

# List of nodes 
nodes =[3, 6, 8, 2, 11, None, 13,4,3,None,2,None,None,3,4,None,None,5] 
  
# Building the binary tree 
binary_tree = build(nodes) 
print('Binary tree from list :\n', binary_tree) 
  
# Getting list of nodes from binarytree 
print('\nList from binary tree :', binary_tree.values) 

print(binary_tree.max_node_value)
print(binary_tree.height)
print(binary_tree.max_leaf_depth)