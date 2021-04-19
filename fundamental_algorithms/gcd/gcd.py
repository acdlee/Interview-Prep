#Functionality: Returns the greatest common 
#divisor of a and b in log(min(a,b)) time.
#
#Input: int a, int b
#Output: int
def gcd(a, b):
	"""	
		Euclidean algorithm:
		use the property that:
		gcd(a, b) = gcd(b, a mod b)
	"""
	if not (a and b):	#De Morgan's
		return max(a, b)	#return non-zero parameter
	else:
		return gcd(b, a%b) #apply the aforementioned property

