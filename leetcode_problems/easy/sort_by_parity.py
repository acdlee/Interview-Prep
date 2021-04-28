# Given an array A of non-negative integers, return an array 
#consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

 

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

# Note:

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

#notes:
#non-neg integers; return array; return all even of A followed by odd ele of A

#O(n) time and space
# def parity_sort(A):
# 	result = []

# 	for ele in A:
# 		if not ele % 2:
# 			#if the element is even add to front
# 			result = [ele] + result
# 		else:
# 			result.append(ele)

# 	return result

#let's go for O(1) space
#O(n) time and O(1) space
# def parity_sort(A):
# 	i, j = 0, len(A) - 1

# 	#use a two pointer system
# 	while i < j:
# 		if A[i] % 2:	#if left side element is odd
# 			#check if we can flip it with jth ele
# 			if not A[j] % 2:	#if right side ele even
# 				#flip the two elements
# 				swap(A, i, j)
# 			else:
# 				#element is odd, so just move j
# 				j -= 1
# 		else:
# 			#j could be even, but i isn't odd
# 			#so increment i
# 			if A[j] % 2:
# 				j -= 1
# 			i += 1

# 	return A

#their solution n time and 1 space
def parity_sort(A):
	i, j = 0, len(A) - 1

	while i < j:
		if A[i] % 2 > A[j] % 2:	#if left side element odd
			#swap
			A[i], A[j] = A[j], A[i]

		if A[i] % 2 == 0: i += 1
		if A[j] % 2 == 1: j -= 1

	return A

def swap(A, i, j):
	temp = A[j]
	A[j] = A[i]
	A[i] = temp

a =  [3,1,2,4]
print(parity_sort(a))



