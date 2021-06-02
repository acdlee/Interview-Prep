#setup linked list problems
from node import Node


ll = Node(4)
lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]


curr = ll
while lst:
    curr.next = lst.pop(0)
    curr = curr.next
