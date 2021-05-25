#O(n) time and space)
def isUnique(s):
	unique = True
	if s:	#empty or None check
		h ={}	#counter

		for c in s:
			if c not in h:
				h[c] = 0
			h[c] += 1

		#string s is unique only when the length is equal to 
		#the number of keys in the hash (counts are all 1)
		unique = len(h.keys()) == len(s)

	return unique

#O(nlgn) time O(n) space
def betterUnique(s):
	unique = True
	if s:
		sorted_s = s.sort()
		for i in range(1, len(s)):
			if sorted_s[i] == sorted_s[i - 1]:
				return False


	return unique

s = 'is this string unique?'
s = 'abcde fg' 
print(isUnique(s))