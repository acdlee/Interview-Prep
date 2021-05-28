def oneAway(s1, s2):
	N, M = len(s1), len(s2)
	if abs(N - M) > 1: return False	#trivially not one-away

	h1, h2 = {}, {}
	#count chars in s1 and s2
	countHelper(h1, s1)
	countHelper(h2, s2)

	count = 0
	for k, v in h1.items():	#check counts
		if k not in h2:		#add unique value v
			count += v
		else:				
			count += abs(v - h2[k])	#add the absolute difference of counts


	for k, v in h2.items():	#add uniques of h2
		if k not in h1:
			count += v

	return count <= 2


#helper to count the occurances of
#chars in the string s as key, value
#pairs for h ({char: count})
def countHelper(h, s):
	for c in s:
		if c not in h:
			h[c] = 0
		h[c] += 1

#we now realize that the letters are literally in place.
#this means they are literally one away.
#O(n) time O(1) space
def betterOneAway(s1, s2):
	N, M = len(s1), len(s2)
	if abs(N - M) > 1: return False	#trivially not one-away

	i, j = 0, 0  	#two pointer approach
	found_diff = False
	while i < N and j < M:
		if s1[i] != s2[j]:
			if found_diff: return False	#two different spots => not one-away
			found_diff = True
		
			if N == M:	#if equal size, should only be one diff spot
				i += 1
				j += 1
			else:
				if N > M:	#if diff sizes, increment larger-string pointer
					i += 1
				else:
					j += 1
		else:
			#same letter; increment both pointer
			i += 1
			j += 1

	return True





s1 = 'pale'
s2 = 'ale'

s1 = 'pale'
s2 = 'bale'

s1 = 'mama'
s2 = 'papa'

print(betterOneAway(s1, s2))