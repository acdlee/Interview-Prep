#linear space and time 
def sortSentence(s):
	if not s:	return s

	curr = ''

	arr = [0] * len(s)

	for i in range (len(s)):
		c = s[i]
		if c == ' ':
			index = int(curr[-1]) - 1
			arr[index] = curr[:-1]
			curr = ''
		elif i + 1 == len(s):
			index = int(c) - 1
			arr[index] = curr
			curr = ''
		else:
			curr += c

	s = ''
	for ele in arr:
		if ele == 0:
			return s[:-1]
		else:
			s += ele + ' '

#cleaner solution than the one above
def sortSentence(s):
	s_lst = s.split(' ')
	res = [0] * len(s_lst)

	for ele in s_lst:
		index = int(ele[-1]) - 1
		res[index] = ele[:-1]

	return ' '.join(res)


s = "is2 sentence4 This1 a3"
print(sortSentence(s))