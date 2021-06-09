#linear time and space
class OrderedStream:

	def __init__(self, n):
		self.n = n
		self.ptr = 0	#chunk pointer
		self.stream = [0] * n

	def insert(self, idKey, value): 
		self.stream[idKey - 1] = value
		result = []
		i = self.ptr

		while i < self.n and self.stream[i]:
			result.append(self.stream[i])
			i += 1

		if 0 in result:
			return []

		self.ptr = i
		return result


os = OrderedStream(5)
print(os.insert(2, 'cat'))
print(os.insert(1, 'dog'))
print(os.insert(4, 'ctt'))
print(os.insert(3, 'ddg'))