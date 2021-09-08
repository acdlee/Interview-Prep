class TreeNode():
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.right = right
		self.left = left


def merge(root1, root2):
	#treat root1 as the current tree
	#use root2 to add to the tree
	if not root1 and not root2:
		return None
	ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
	ans.left = merge(root)