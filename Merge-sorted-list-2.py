# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# code to locally test data
# make this a linked list with name ListNode
given_list=[[1,4,5],[1,3,4],[2,6]]

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.header=None
        self.tail=None
        self.size=0

    def append(self,data):
        n=Node(data)
        if(self.size==0):
            self.header=n
            self.tail=n
        else:
            temp=self.tail
            self.tail=n
            temp.next=self.tail
        self.size+=1

    def printlist(self):
        data=""
        current=self.header
        while(current!=None):
            data=data+str(current.data)+" "
            current=current.next
        return data
    
mylist=LinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

print(mylist.printlist())

# create a dictionaly for input, list sequence: lencgth of sub-list
dictionary_given_list={}

for x in range(len(given_list)):
    dictionary_given_list.update({x:len(given_list[x])})

print(dictionary_given_list)

