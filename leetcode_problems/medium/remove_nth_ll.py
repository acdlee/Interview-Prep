class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthFromEnd(head, n):
    #try again
    pass

def printLL(head):
    curr = root
    while curr:
        print(curr.data)
        curr = curr.next


root = Node(-1)
curr = root
for i in range(8):
    curr.next = Node(i)
    curr = curr.next

lst = removeNthFromEnd(root, 1)
printLL(lst)