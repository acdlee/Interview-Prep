#O(lgn) time and space
def numberOfSteps(num):	
	return helperSteps(num, 0)


def helperSteps(num, step):
	if not num:		#base case: num == 0 => return step
		return step
	else:
		step += 1	#take a step
		if num % 2:		#parity check
			return helperSteps(num - 1, step)
		else:
			return helperSteps(num/2, step)


#with bit shift:
#O(lgn) time, constant space
def bitShift(num):
	step = 0
	if num:		#num == 0 check
		while num > 0:
			step += 1 + (num & 1)	#take a step; add extra step if odd
			num >>= 1	#bit shift (divide by 2)

	#we take an extra step when going from 1->0,
	#since we account for other odd steps with (num&1)
	return step - 1

val = 4
val = 5 
# print(numberOfSteps(val))
print(bitShift(val) == numberOfSteps(val))