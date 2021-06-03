
#setup linked list problems
from node import Node


ll = Node(4)
# lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]
lst = [Node(1), Node(4)]

curr = ll
while lst:
    curr.next = lst.pop(0)
    curr = curr.next

#linear time and space
def palindrome(ll):
    if not ll: return True  #empty case defaults True

    deque, curr = [], ll

    #use a deque data structure to record data
    while curr:
        deque.append(curr.data)
        curr = curr.next

    #pop both sides of the deque and check that
    #they are equal
    while deque:
        if len(deque) == 1:
            return True
        else:
            front, back = deque.pop(0), deque.pop()
            if front != back:
                return False

    return True


print(palindrome(ll))