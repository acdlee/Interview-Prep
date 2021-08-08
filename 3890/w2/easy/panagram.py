#O(N + M) time and space
def anagram(s1, s2):
	N, M = len(s1), len(s2)
	if N != M: return False

	#use a dict to store counts
	#increment for chars in s1; decrement for chars in s2
	h = {}

	#count chars for both s1 and s2
	for i in range(N):
		#make entry if the char is not in the dict
		if s1[i] not in h.keys():
			h[s1[i]] = 0

		if s2[i] not in h.keys():
			h[s2[i]] = 0

		#adjust counts
		h[s1[i]] += 1
		h[s2[i]] -= 1

	#check that everything is 0
	for k, v in h.items():
		if v:	return False


	return True


s1 = 'hello'
s2 = 'lloze'
print(anagram(s1, s2))