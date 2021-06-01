# You own a Goal Parser that can interpret a string command. 
# The command consists of an alphabet of "G", "()" and/or "(al)"
#  in some order. The Goal Parser will interpret "G" as the string
#   "G", "()" as the string "o", and "(al)" as the string 
#   "al". The interpreted strings are then concatenated in
#    the original order.

# Given the string command, return the Goal Parser's 
# interpretation of command.

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al

# The final concatenated result is "Goal".


#linear space and time
def slowInterpret(command):
	h = {'G':'G', '()':'o', '(al)':'al'}
	result, i = '', 0
	while i < len(command):
		c = command[i]
		if c == '(':
			if command[i + 1] == 'a':
				i += 3	#move past the next 3 chars
				c = '(al)'
			else:
				i += 1	#move past the next char
				c = '()'
		result += h[c]
		i += 1
		

	return result

#linear time; constant space
def betterInterpret(command):
	result, i, N = '', 0, len(command)
	while i < N:
		if command[i] == 'G':
			result += 'G'
		elif command[i+1] == 'a':
			i += 3
			result += 'al'
		else:
			i += 1
			result += 'o'

		i += 1

	return result


def interpret(command):
	return command.replace('()', 'o').replace('(al)', 'al')

command = "G()()()()(al)G"
print(interpret(command))

