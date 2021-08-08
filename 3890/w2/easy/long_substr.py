#O(N) time and space
def longestSubString(s1):
	if not s1:	return 0

	k = 0	#longest substring length

	#"sliding window" technique
	start, window, window_dict = 0, 0, {}
	curr_count = 0

	while window < len(s1):
		#check if the char is repeated
		if s1[window] in window_dict.keys():		#if repeated
			#move the start of our window past the first occurance of
			#the repeat char
			start = window + 1
			#adjust the current run count
			curr_count = window - window_dict[s1[window]]
		else:					 					#if not repeated
			#store the char and its indicie
			window_dict[s1[window]] = window
			curr_count += 1
			#update k
			k = max(k, curr_count)

		#move the window
		window += 1

	#return length of longest substring
	return k





s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(longestSubString(s1))
print(longestSubString(s2))
print(longestSubString(s3))
