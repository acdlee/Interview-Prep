class SubrectangleQueries:

	def __init__(self, rectangle):
		self.rectangle = rectangle
		self.N = len(rectangle)		#number of rows
		self.M = len(rectangle[0])	#number of cols

	# rectangle := [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]

	#O(n'*m') time, where n' = row2 - row1 and m' = col2-col1
	#O(1) space
	def updateSubrectangle(self, row1, col1, row2, col2, newValue):
		#upper left coord is (row1,col1) and bottom right (row2, col2)
		if not (self.checkOOB(row1, col1) or self.checkOOB(row2, col2)): #DeMorgan's boundary check
			for row in range(row1, row2 + 1):
				for col in range(col1, col2 + 1):
					self.rectangle[row][col] = newValue

		#returns None in either case
		return None

	#constant time and space
	def getValue(self, row, col):
		if not self.checkOOB(row, col):	#boundary check
			return self.rectangle[row][col]

		#return -1 on index OOB case
		return -1

	#checks that the input row/col is in bounds.
	#
	#Returns True if row or col is OOB; False otherwise. 
	def checkOOB(self, row, col):
		if row < self.N and col < self.M and row >= 0 and col >= 0:
			return False

		return True

rect = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
rect.updateSubrectangle(0,0, 3,2, 5)
print(rect.getValue(0,2))