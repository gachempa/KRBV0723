# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# code to locally test data
# make this a linked list with name ListNode
# given_list=[[1,4,5],[1,3,4],[2,6]]

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
            # temp.next=self.tail
            temp.next=n
        self.size+=1

    def printlist(self):
        data=""
        current=self.header
        while(current!=None):
            data=data+str(current.data)+" "
            current=current.next
        return data
    
    def removeFirst(self):
        if(self.size==0):
            return None
        data=self.header.data
        if(self.size==1):
            self.header=None
            self.tail=None
        else:
            self.header=self.header.next
        self.size-=1
        return data

mylist_a=LinkedList()
mylist_b=LinkedList()
mylist_c=LinkedList()
mylist_d=LinkedList()

mylist_a.append(1)
mylist_a.append(4)
mylist_a.append(5)

mylist_b.append(1)
mylist_b.append(3)
mylist_b.append(4)

mylist_c.append(2)
mylist_c.append(6)

lists=[]
lists.append(mylist_a)
lists.append(mylist_b)
lists.append(mylist_c)
lists.append(mylist_d)

# print(given_list)

# lists=LinkedList()
# lists.append(999)

# create a dictionaly for input, list sequence: lencgth of sub-list
dictionary_given_list={}

# this list has all the latest min values from the sublists in the given_list
the_min_list=[]
the_min_values_dictionary={}

for x in range(len(lists)):
    a=lists[x].removeFirst()
    dictionary_given_list.update({x:a})
#     the_min_values_dictionary.update({x:given_list[x][0]})
    if a==None:
        pass
    else:
        the_min_list.append(a)
    
# print(dictionary_given_list)
# print(the_min_list)

sorted_list=LinkedList()

# listxyz=[]
# print(len(listxyz))

while(len(the_min_list)>0):
# # below will be wrapped in a looped function
    min_to_append=min(the_min_list)
    sorted_list.append(min_to_append)

    # the index of the min in the min list
    a=the_min_list.index(min_to_append)
    new_min=lists[a].removeFirst()
    # print(new_min)
    dictionary_given_list.update({a:new_min})
    if new_min==None:
        the_min_list.pop(a)
    else:
        the_min_list[a]=new_min

print(dictionary_given_list)
print(the_min_list)
print(sorted_list.printlist())


# # The min is popped and appended to the linked list
# mylist.append(given_list[a].pop(0))
# print(given_list[a])
# print(mylist.printlist())

# # in dictionary, update the count of the list to account for the pop
# dictionary_given_list[a]-=1
# print(dictionary_given_list)

# # the new min from the sublist replaces the popped min
# # if dictionary_given_list[a]==0:

