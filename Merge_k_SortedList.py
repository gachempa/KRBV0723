# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
		
# code to locally test data
# make this a linked list with name ListNode
given_list=[[1,4,5],[1,3,4],[2,6]]

class LinkedList:
    def __init__(self) -> None:
		self.head=None
            
	def insert_at_beginning(self,val):
          listNode=ListNode(val,self.head)