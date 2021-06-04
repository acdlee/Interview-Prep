#setup linked list problems
from node import Node


l1 = Node(4)
lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]

l2 = Node(1)
l2.next = Node(5)

curr = l1
c2 = l2.next

i = 3
while lst:
    curr.next = lst.pop(0)
    curr = curr.next
    if not i:
        c2.next = curr

    i -= 1

#O(n+m) time and constant space
def intersection(l1, l2):
    if not l1 or not l2: return None   #empty check

    #get the size and tails of both lists
    size1, tail1 = getSizeTail(l1)
    size2, tail2 = getSizeTail(l2)

    #if tails are not equal => no intersection
    if tail1 != tail2:  return None

    #check if we need to cut off any beginning nodes
    if size1 != size2:
        temp = 0
        if size1 < size2:
            #l2 bigger => trim l2
            l2 = move(l2, size2 - size1)
        else:
            #l1 bigger => trim l1
            l1 = move(l1, size1-size2)

    #set pointers
    c1, c2 = l1, l2


    #since equal size and there is an intersection, 
    #mirror interations
    while c1 != c2:
        c1 = c1.next
        c2 = c2.next

    return c1

def move(ll, temp):
    while temp:
        temp -= 1 
        ll = ll.next

    return ll
    
def getSizeTail(ll):
    size = 0
    curr = ll
    while curr.next:
        size += 1
        curr = curr.next

    return size + 1, curr



node = intersection(l1, l2)

print(node.data) 