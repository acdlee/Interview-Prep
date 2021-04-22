def extended_euclidean_algorithm(a, b):
	"""
		Extended Euclidean Algorithm:
		computes the gcd of two inputs, along with the coefficients x, y 
		of Bezout's identity: 
			ax + by = gcd(a, b).
	"""
	(old_r, r) = (a, b)
	(old_s, s) = (1, 0)
	(old_t, t) = (0, 1)

	while r:
		quotient = old_r // r
		(old_r, r) = (r, old_r - quotient * r)
		(old_s, s) = (s, old_s - quotient * s)
		(old_t, t) = (t, old_t - quotient * t)


	print("coefficients: (" + str(old_s) + ", " + str(old_t) + ")" )
	print("gcd: " + str(old_r))


extended_euclidean_algorithm(412, 260)