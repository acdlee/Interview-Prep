#linear time; constant space
def countMatches(items, ruleKey, ruleValue):
	count = 0
	if items and ruleKey and ruleValue:		#empty check
		#i will be the index for the specific key
		#from each item in items
		i = -1						#give it a default value

		#let's find out what the ruleKey is
		if ruleKey == 'type':
			i = 0
		elif ruleKey == 'color':
			i = 1
		else:
			i = 2

		#loop through items and check if any of
		#the rules are satisfied
		for item in items:
			key = item[i]
			if key == ruleValue:
				count += 1



	return count


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

print(countMatches(items, ruleKey, ruleValue))