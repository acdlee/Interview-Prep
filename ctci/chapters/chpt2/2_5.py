#setup linked list problems
from node import Node


l1 = Node(4)
l2 = Node(8)
lst = [Node(1), Node(4)]
lst2 = [Node(6), Node(1)]


curr = l1
while lst:
    curr.next = lst.pop(0)
    curr = curr.next

curr = l2
while lst2:
    curr.next = lst2.pop(0)
    curr = curr.next

#O(m+n) time and space
def sumLL(l1, l2):
    if not l1 or not l2: return False   #empty check

    #use the helper function to generate the string representation
    #of our two numbers
    s1, s2 = getNumberHelper(l1), getNumberHelper(l2)

    print(s1)
    print(s2)

    #get our summed number
    value_s = str(int(s1) + int(s2))

    print(value_s)

    #note that value_s needs to be changed to a linked
    #list and reversed

    #instantiate our return_ll as the tail None
    return_ll = None

    for c in value_s:   #loop through each character (each int)
        #create a node and link it the the rest of the list
        new_node = Node(int(c))
        new_node.next = return_ll
        return_ll = new_node

    return return_ll



def getNumberHelper(ll):
    s, curr = '', ll

    while curr:
        s = str(curr.data) + s
        curr = curr.next

    return s


new_ll = sumLL(l1, l2)

while new_ll:
    print(new_ll.data)
    new_ll = new_ll.next
