# Balanced strings are those that have an equal quantity of 
# 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount 
# of balanced strings.

# Return the maximum amount of split balanced strings.

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
# each substring contains same number of 'L' and 'R'.

#linear time; constant space
def balancedStringSplit(s):
	result = count = 0
	
	for c in s:
		count += 1 if c == 'R' else -1

		if not count:
			result += 1

	return result


s = "RLRRLLRLRL"
# s = "RLLLLRRRLR"
print(balancedStringSplit(s))