#O(n) space and time complexity
def finalprices(prices):
	if prices: #if prices isn't empty
		stack = []

		for idx, price in enumerate(prices):
			while stack and price <= stack[-1][1]:	#while the stack isnt empty and price is lower
				i, p = stack.pop()
				prices[i] -= price

			stack.append((idx, price))

	return prices