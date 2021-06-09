#linear time and space
def arrayStringsAreEqual(word1, word2):
	s1, s2 = '', ''
	for ele in word1: s1 += ele
	for ele in word2: s2 += ele

	return s1 == s2


word1 = ["ab", "c"]
word2 = ["a", "bc"]

print(arrayStringsAreEqual(word1, word2))