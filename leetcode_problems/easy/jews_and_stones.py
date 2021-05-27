#O(J + S) time; O(J) space
def numJewelsInStones(jewels, stones):
	result = 0
	if jewels != '' and stones != '':	#empty strings check 
		h = {}	#counter
		for jewel in jewels:
			if jewel not in h:
				h[jewel] = 0
			h[jewel] += 1

		for stone in stones:
			if stone in h:
				result += 1

	return result