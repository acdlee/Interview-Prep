#O(n) time and space
def decode(encoded, first):
	result = [first]

	if encoded: #empty check
		#we know that encoded[i] = arr[i] xor arr[i + 1]
		#note that encoded[i]xor arr[i] = arr[i+1]
		for i in range(len(encoded)):
			result.append(result[i]^encoded[i])


	return result



encoded, first = [1,2,3], 1
print(decode(encoded, first))

