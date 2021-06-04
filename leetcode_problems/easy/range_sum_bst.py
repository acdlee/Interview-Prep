class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
        self.left = left
		self.right = right

#linear in the number of nodes for time and space (n stack calls)
def rangeSumBST(root, low, high):
        if not root: return 0
        if root.val < low: return rangeSumBST(root.right, low, high)
        if root.val > high: return rangeSumBST(root.left, low, high)
        return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
