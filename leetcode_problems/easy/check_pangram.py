OFFSET = 97

#linear time; O(26) space
def checkIfPangram(sentence):
	if len(sentence) < 26: return False
	arr, zero, = [0]*26, 26
	lowercase_s = sentence.lower()

	for c in lowercase_s:
		if not arr[ord(c) - OFFSET]:
			#if there's a zero in there, decrement
			#the zero count and increase element value
			zero -= 1
			arr[ord(c) - OFFSET] = 1

		if not zero:
			return True

	return False

def checkIfPangram(s):
	return len(set(s)) == 26

s = "thequickbrownfoxjumpsoverthelazydog"
s = 'cat'
s = 'aooaoaoaoaoaoaoaoaoaoaoaooaoaoaoaoaoa'
print(checkIfPangram(s))