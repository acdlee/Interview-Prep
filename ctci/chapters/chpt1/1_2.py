#O(n) time and space

def isPermutation(s1, s2):
	N, M = len(s1), len(s2)
	if (N == 0 or M == 0) and M != N: return False
	if (N != M): return False

	h = {} #counter for s1

	for c in s1:	#get the counts of chars in s1
		if c not in h:
			h[c] = 0
		h[c] += 1

	for c in s2: 	#decrement counts of h
		if c not in  h:
			return False
		h[c] -= 1

	#check if all 0's in h
	for value in h.values():
		if value != 0:
			return False

	return True


s1 = 'cat in the hat'
# s2 = 'tah eht  intac'
s2 = 'cat in the hai'
print(isPermutation(s1, s2))