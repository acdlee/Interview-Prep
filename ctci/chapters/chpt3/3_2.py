class Node:
	def __init__(self, value):
		self.value = value
		self.min = None

class Stack:

	def __init__(self):
		self.lst = []

	def push(self, x):
		#create the new node
		new_node = Node(x)

		#find the min of the previous stack and yourself
		if not self.lst:
			new_node.min = x
		else:
			new_node.min = min(x, self.lst[-1].min)
			
		self.lst.append(new_node)

	def pop(self):
		ele = self.lst.pop()
		return ele.value


	def min_val(self):
		return self.lst[-1].min


s = Stack()
s.push(1)
print(s.min_val())
s.push(-1)
print(s.min_val())
s.pop()
print(s.min_val())