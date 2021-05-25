#(i, j) is a good pair if nums[i]==numsj and i<j
#O(n) space and time
# number of pairs = n*(n-1) //2
def numIdenticalPairs(nums):
	total_pairs, N = 0, len(nums)
	h = {}
	if nums:
		for ele in nums:
			if ele not in h:
				h[ele] = 1
			else:
				h[ele] += 1

	for val in h.values():
		total_pairs += (val*(val-1))//2

	return total_pairs

nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
print(numIdenticalPairs(nums))