#O(n*m) time, constant space
def maximumWealth(accounts):
	#find the wealth of one customer
	#find the wealth of n customers
	if accounts:	#if accounts isn't empty
		global_wealth = 0

		for account in accounts:	#loop through all the n accounts
			# local_wealth = 0		#keep a running local wealth
			# for m in range(len(account)):
			# 	local_wealth += account[m]


			#check to see if the local wealth is the global wealth
			global_wealth = max(global_wealth, sum(account))
			

		return max_wealth

	return accounts