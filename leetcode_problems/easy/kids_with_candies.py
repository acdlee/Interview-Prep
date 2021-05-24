#O(n) time O(n) space
#O(n) time O(1) space
def kidsWithCandies(candies, extraCandies):
	# result = []

	if candies:
		# M = max(candies)
		# for candy in candies:
		# 	truth_value = (candy + extraCandies) >= M
		# 	result.append(truth_value)
		M = max(candies)
		for i in range(len(candies)):
			truth_value = (candies[i] + extraCandies) >= M
			candies[i] = truth_value


	# return result
	return candies

#we dont have to add extraCandies each time
def optimizedKids(candies, extraCandies):
	M = max(candies) - extraCandies
	return [candy >= M for candy in candies]