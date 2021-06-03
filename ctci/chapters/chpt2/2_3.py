#setup linked list problems
from node import Node


ll = Node(4)
lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]


curr = ll
ptr = None
while lst:
    if len(lst) == 3:
        ptr = curr
    curr.next = lst.pop(0)
    curr = curr.next

#given access to a middle node, 
#remove that node from the list
#constant space and time
def deleteMiddleNode(node):
    if not node: return node

    next_n = node.next
    node.data = next_n.data
    node.next = next_n.next

deleteMiddleNode(ptr)

while ll:
    print(ll.data)
    ll = ll.next