#setup linked list problems
from node import Node


ll = Node(4)
lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]


curr = ll
i = 3
ptr = None
while lst:
    curr.next = lst.pop(0)
    curr = curr.next
    i -= 1
    if not i:
        ptr = curr

#create a loop
curr.next = ptr

#O(n) time; O(n) space
def loopDetection(head):
    if not head: return head #empty check

    # p1, p2 = head, head.next
    p1 = head
    h = {}  #keep track of visisted nodes

    while p1:   #cycle through all the nodes
        if p1 in h:     #if we find a collision => "looper"
            return p1
        h[p1] = 0       #store the new node in h
        p1 = p1.next    #move pointer

    #if we come across None in the prior while loop
    #=> not a cycle.
    return None

#linear space const time
def loopDetection(head):
    if not head: return head

    p1, p2 = head, head

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next

        if p1 == p2:
            break

    p1 = head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1

print(loopDetection(ll).data)