class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

#O(n) time O(1) space
def mid(head):
	#use the fast, slow pointer method
	fast = slow = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	return slow.val

def setup(vals = [10, 12, 1, 4, 20, 8]):
	#if question mark input, return info on how to use the function
	if vals == '?':
		msg = "Given an array of integer values, this function returns"
		msg += "\na linked list of those values."
		print(msg)
		return

	#else process either the default input or the given input
	head = ListNode()
	curr = head

	for val in vals:
		new_node = ListNode(val=val)
		curr.next = new_node
		curr = new_node	

	return head

def checkLLSetup(curr):
	msg = 'Current List: '
	if not curr:
		print(msg + "-Empty-")
	else:
		while curr:
			msg += str(curr.val) + "->"
			curr = curr.next

		print(msg[:-2])

ll = setup([1,2,3,4,5])
checkLLSetup(ll)

print(mid(ll))


