#O(n) time/space
def shuffle(nums, n):
	N= 2*n
	even_idx, odd_idx = 1, 0
	result = [0] * (N)
	if nums:	#empty check
		for i in range(N):
			value = nums[i]
			if i < n:
				#odd index
				result[odd_idx] = value
				odd_idx += 2			#keep the odd-indexing
			else:
				#even index
				result[even_idx] = value
				even_idx += 2			#keep the even-indexing

		return result


	return nums

# 2 5 1 3 4 7
# 2 3 1 5 4 7 prev = back_idx, backindx n+1
# 2 3 5, 1, 4, 7
def better_shuffle(nums, n):
	if nums:
		prev = -1	#index for xi placements
		back_idx = n
		for i in range(1, n+2):
			if not i % 2:		#parity check
				#even index => x element
				swap(nums, i, prev)
				prev = back_idx
			else:
				#odd index => y element
				swap(nums, i, back_idx)
				if prev == -1:
					prev = back_idx
				back_idx += 1
	return nums	


def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp
A = [2,5,1,3,4,7]
A = [1,1,2,2]
A = [1,2,3,4,4,3,2,1]
print(better_shuffle(A, 4))

# [1, 4, 2, 5, 3, 6]


# <- [1, 4,2,5 ,3, 6]