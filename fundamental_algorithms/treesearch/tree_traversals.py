class TreeNode():
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def insertNode(root, val):
	if not root: return TreeNode(val)
	if root.val == val:
		return root
	elif val < root.val:
		root.left = insertNode(root.left, val)
	else:
		root.right = insertNode(root.right, val)

	return root

def setupBinarySearchTree(vals=[2,5,1,6,12,9]):
	if not vals: return None
	BST = None
	for val in vals:
		BST = insertNode(BST, val)

	return BST

def runTraversals(BST):
	print("Preorder: ")
	preorderTraversal(BST)
	print("Inorder: ")
	inorderTraversal(BST)
	print("Postorder: ")
	postOrderTraversal(BST)


def inorderTraversal(node):
	if not node: return
	inorderTraversal(node.left)
	print(node.val)
	inorderTraversal(node.right)

def preorderTraversal(node):
	if not node: return
	print(node.val)
	preorderTraversal(node.left)
	preorderTraversal(node.right)

def postOrderTraversal(node):
	if not node: return None
	postOrderTraversal(node.left)
	postOrderTraversal(node.right)
	print(node.val)

def searchBST(node, val=12):
	if not node: 
		print("Node not found!")
		return
	if node.val == val:
		print("Found node!")
	elif node.val < val:
		searchBST(node.right, val)
	else:
		searchBST(node.left, val)

BST = setupBinarySearchTree()
runTraversals(BST)
searchBST(BST, 13)



