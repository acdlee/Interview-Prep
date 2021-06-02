#setup linked list problems
from node import Node


ll = Node(4)
lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]


curr = ll
while lst:
    curr.next = lst.pop(0)
    curr = curr.next


#find the kth to last element of a singly linked list
#O(n) time; O(1) space
def iterKthElement(head, k):
    if head:    #None check
        n, curr = 0, head

        while curr:         #calculate the length of the linked list
            n += 1
            curr = curr.next

        #5 7 2 1 4 2 n -> 6; k=2
        #we want to do n-k-1 steps
        steps = n-k

        #reposition curr to the start of the list
        curr = head

        while curr:
            if not steps:   #located the kth element
                return curr.data

            #move pointer if we're still searching and decrement steps
            curr = curr.next
            steps -= 1

    #return -1 in any error case
    return -1

#recursive solution: linear t/s
def kthElement(head, k):
    if not head: return 0       #end of the list check

    index = kthElement(head.next, k) + 1

    if index == k:
        print(head.data)
    
    return index
    






print(kthElement(ll, 4))   #should print 6
