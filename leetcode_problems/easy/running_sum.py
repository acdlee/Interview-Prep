#O(n) time and O(1) space
def runningSum(nums):
    if nums:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

    return nums
