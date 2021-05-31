#linear time and space
def decompressRLElist(nums):
	result = []

	if nums:	#empty check
		for i in range(0, len(nums), 2):
			freq, val = nums[i], nums[i+1]	#by problem description
			result += [val]*freq


	return result





nums = [1,2,3,4]
print(decompressRLElist(nums))