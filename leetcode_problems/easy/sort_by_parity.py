#O(n) space and time
def parity(nums):
    result = []
    for ele in nums:
        if ele % 2 == 0:
            result = [ele] + result
        else:
            result.append(ele)

    return ele


#O(n) time O(1) space
def parity(nums):
    i, j = 0, len(nums) - 1

    while i < j:
        if nums[i] % 2:
            #if the current i is odd
            while i < j and nums[j]%2:
                #find an even element from the back
                j -= 1
            swap(nums, i, j) #swap the elements

            #move the pointers
            j -= 1
        i += 1

    return nums

#helper for swapping
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
