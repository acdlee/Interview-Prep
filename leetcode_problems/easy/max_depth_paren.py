

def maxDepth(s):
	if s == '': return 0				#True case
	if len(s) == 1 and (s != ')' or s != '('): return 0	#True cases
	if not s: return False	#None check

	stack = []
	m_depth = 0
	count = 0

	for c in s:
		if c == '(':
			count += 1
			m_depth = max(m_depth, count)
		if c == ')':
			count -= 1
			

	return m_depth


s = "(1+(2*3)+((8)/4))+1"
s = "(1)+((2))+(((3)))"
s = "8*((1*(5+6))*(8/6))"
# s = "1+(2*3)/(2-1)"
# s = "1"
print(maxDepth(s))