#O(nlgn) to create a BST time
#O(n) storage since we're making n nodes
class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def insertBST(node, val):
	if not node:
		return Node(val)
	if val < node.val:
		node.left = insertBST(node.left, val)
	elif node.val < val:
		node.right = insertBST(node.right, val)
	else:
		#if we repeat a value, dont add another node
		return node

	return node

def createTree(arr):
	#take the middle value and make it the root
	# bst = insertBST(None, arr[len(arr)//2])
	# for val in arr:
	# 	bst = insertBST(bst, val)

	# return bst


	return linearSol(arr, 0, len(arr) - 1)

def inOrder(node):
	if not node: return
	inOrder(node.left)
	print(node.val)
	inOrder(node.right)

#linear time and space
#we only visit each node once (no extra traversals)
def linearSol(arr, left, right):
	if left > right: return None
	mid = (left + right) // 2
	node = Node(arr[mid])
	node.left = linearSol(arr, left, mid - 1)
	node.right = linearSol(arr, mid + 1, right)
	return node

arr = [3,515,1,23,1,6,10]
arr.sort()
bst = createTree(arr)
inOrder(bst)