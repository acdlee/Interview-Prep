# Given the root of a binary search tree, rearrange the 
# tree in in-order so that the leftmost node in the tree 

# is now the root of the tree, and every node has no left 
# child and only one right child.

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def tree_line(root):
	#navigate to the leftmost node
	if root:
		#if not null

		#visit left subtree
		print(root.val)
		tree_line(root.left)