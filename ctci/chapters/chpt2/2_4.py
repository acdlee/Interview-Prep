#setup linked list problems
from node import Node


ll = Node(4)
lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]


curr = ll
while lst:
    curr.next = lst.pop(0)
    curr = curr.next

#linear space and time
def partition(ll, x):
    if not ll:  return False

    lst = []    #hold all data values
    curr = ll

    while curr:
        if curr.data < x:
            #put on left side
            lst = [curr.data] + lst
        else:
            #put on right side
            lst.append(curr.data)

        #move pointer
        curr = curr.next
    curr = ll   #return curr pointer to start of ll
    while curr:
        #assing data, according to lst, sequentially
        curr.data = lst.pop(0)
        #move the pointer
        curr = curr.next

    return True

# def recursivePartition(ll, x):
#     recursivePartitionHelper(ll, x, [])

# def recursivePartitionHelper(ll, x, lst):
#     #let's first add our current
#     #node's data to the lst
#     if ll.data < x:
#         lst = [ll.data] + lst
#     else:
#         lst.append(ll.data)

#     if ll.next:
#         #if there is another node, go to it
#         recursivePartitionHelper(ll.next, x, lst)
#     #backtrack and insert data from lst
#     print(lst)
#     ll.data = lst.pop()

recursivePartition(ll, 4)
curr = ll
while curr:
    print(curr.data)
    curr = curr.next
