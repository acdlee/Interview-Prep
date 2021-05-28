#linear time and space

def paliPerm(s):
	result = True
	
	if s:	#empty check
	h = {} 	#counter

	for c in s:	#store the counts
		if c not in h:
			h[c] = 0
		h[c] += 1

	odd = False
	for val in h.values():	#check counts
		if val % 2:			#if odd by parity
			if odd:
				return False
			odd = True

	return result
