# Interesting problem from CMSC 456:
# When discussing the attack on the discrete log problem,
# there's the naive attack (O(m)) and a better attack (O(sqrt(m))).

# In the naive attack, there's a problem of trying to find
# an intersection between two lists. Contextually, finding two values
# for i, j where y*g^-i = g^i*sqrt(m).

#This leverages the fact any number can be written as a base
#of another number. Specifically, x = i*sqrt(m) + j
#for i in [0, sqrt(m))
#and j in [0, sqrt(m))
#where m is the order of an cyclic group and y is an element of that group.

#Problem setup:
# find an x s.t. y = g^x, given y and g,
#with the aformentioned conditions met for y and g.
def intersect(g, y, m):
	lst = [0] * sqrt(m)
	h = {}
	target_i, target_j = -1, -1 	#default values for our targets

	#O(sqrtm)
	for i in range(sqrt(m) - 1):
		lst[i] = y*g**(-i)		#calculate the leftside value
		key = g**(i*sqrt(m))	#calulcate the rightside value
		h[key] = i 				#store in hash

	#use the elements of lst as possible keys for h
	for i in range(sqrt(m) - 1):
		local_key = lst[i]
		if local_key in h:		#'in' is O(1) average for hashes
			target_i = i
			target_j = local_key
			break

	#calculate the value of x
	exponent = target_i*sqrt(m) + target_j
	return g**exponent

