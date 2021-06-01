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


def interpret(command):
	h = {'G':'G', '()':'o', '(al)':'al'}
	result = ''
	for i in range(len(command)):
		if command[i] == '(':
			if command[i+1] == 'a':
				#incr past 'al)'
		if c in h:
			result += h[c]

	return result

command = "G()()()()(al)"
print(interpret(command))

