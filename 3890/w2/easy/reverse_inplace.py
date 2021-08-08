#O(n) time; O(1) space
def reverseInPlace(arr):
	#None and empty check
	if arr:
		#two pointer method
		i, j = 0, len(arr) - 1


		# 1 2 3 4
		# 1 2 3 4 5
		while i < j:
			#swap the elements and move pointers
			swap(arr, i, j)
			i += 1
			j -= 1

def swap(arr, i, j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp




x = [1,4,6,2,-1]
# print(reverseInPlace(x))
reverseInPlace(x)
print(x)