# Given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2*i (0-indexed)
#  and n == nums.length.

# Return the bitwise XOR of all elements of nums.

 

# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] 
# where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.

#linear t const s
def xor(n, start):
	result = 0

	for i in range(n):
		result ^= start + 2*i

	return result

n = 5
start = 0
print(xor(n, start))