from node import Node

#we can do this without a buffer but we would have to 
#use a double loop to check that some current node isn't
#equal to any other nodes. 

#remove duplicates from an unsorted linked list
#linear space and time
def removeDuplicates(ll):
	
	if ll:		#empty list check
		curr, prev = ll, None
		h = {}			#count for data values we find

		while curr:
			if curr.data not in h:
				#first occurance
				h[curr.data] = 1
				#move prev pointer to curr
				prev = curr
			else:
				#duplicate - remove duplicate by moving prev
				prev.next = curr.next

			#move curr pointer
			curr = curr.next


	return ll


ll = Node(4)
lst = [Node(1), Node(4), Node(6), Node(1), Node(3)]


curr = ll
while lst:
	curr.next = lst.pop(0)
	curr = curr.next

new_ll = removeDuplicates(ll)
curr = new_ll

while curr:
	print(curr.data)
	curr = curr.next