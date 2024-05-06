from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        node_print = self.head
        while node_print is not None:
            print (node_print.val)
            node_print = node_print.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        print(self.head)
        curr_node=self.head
        while curr_node is not None and curr_node.next is not None:
            # print(curr_node.val)
            if curr_node.val==curr_node.next.val:
                curr_node.next=curr_node.next.next
                print(curr_node.val)
            else:
                curr_node=curr_node.next

Llist=LinkedList()
head_arr=[1,1,2,3,3]
for x in reversed(head_arr):
    Llist.insertAtBegin(x)

# Llist.printList()
Llist.deleteDuplicates(Llist.head)