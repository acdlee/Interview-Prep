#O(isSubstring) time; O(S) space
def isRotation(s1, s2):
	if len(s1) != len(s2): return False	#trivially False
	if not s1: return False				#empty string
	
	new_s1 = s1+s1
	return isSubstring(new_s1, s2)
