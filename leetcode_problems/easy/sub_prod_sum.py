# O(n) time and space
def subtractProductAndSum(n):
	result = 0
	if n:
		product_n = 1
		sum_n = 0
		s = str(n)
		for c in s:
			i = int(c)
			product_n *= i
			sum_n += i

		result = product_n - sum_n

	return result

n = 4421
print(subtractProductAndSum(n))