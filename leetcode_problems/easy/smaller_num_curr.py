#O(n) space
#O(nlgn) time

def smallerNumberThanCurr(nums):
	if not nums:	#empty check
		return nums

	h = {}	#dictionary for counting
	for idx, ele in enumerate(sorted(nums)):
		#the sorted index idx will be the number of elements
		#in nums that are less than ele
		if ele not in h:		#only take the first occurance of ele
			h[ele] = idx

	return [h[num] for num in nums]


#linear time and space
def bucketSolution(nums):
	count = [0] * 102
	for num in nums:
		count[nums + 1] += 1

	for i in range(1, 102):
		count[i] += count[i-1]

	return [count[num] for num in nums]

nums = [6,5,6,8]
print(bucketSolution(nums))


