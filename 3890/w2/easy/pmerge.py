# Question:
# Given two sorted integer arrays A and B, merge B into A as one 
# sorted array. You may assume that A has enough space (size that
#  is greater or equal to m + n) to 
# hold additional elements from B. assume A is of length n and B is of length m.

# Example:
# arr1 = [1,3,5,7], arr2 = [2,4,6,8] --> [1,2,3,4,5,6,7,8]


def merge(A, B):
	'''
		Solution in O(N + M) time and space
		using the two pointer technique.
	'''

	#empty/trivial checks
	if not A: return B
	if not B: return A

	result = []	#result arr
	i = j = 0	#pointers
	N, M = len(A), len(B)

	#step through both arrays and insert into
	#result array using the two pointer method
	while (i < N and j < M):
		if A[i] < B[j]:
			result.append(A[i])
			i += 1
		else:
			result.append(B[j])
			j += 1

	#add remaining elements in either (not both) A or B
	while (i < N):
		result.append(A[i])
		i += 1

	while (j < M):
		result.append(B[j])
		j += 1


	return result

arr1 = [1,3,5,7]
arr2 = [2,4,6,8]

print(merge(arr1, arr2))



