# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

"""
def sizeOfLL(self):
	size = 0
	if(self.head):
		current_node = self.head
		while(current_node):
			size = size+1
			current_node = current_node.next
		return size
	else:
		return 0

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
		
# code to locally test data
# make this a linked list with name ListNode
given_list=[[1,4,5],[1,3,4],[2,6]]