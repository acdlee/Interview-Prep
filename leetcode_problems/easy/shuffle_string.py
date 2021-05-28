#linear time and space
def restoreString(s, indices):
	N = len(s)
	result = [0] * N
	for i in range(N):
		result[indices[i]] = s[i]

	new_s = ''
	for ele in result:
		new_s += str(ele)

	return new_s

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))