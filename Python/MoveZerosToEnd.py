# Given an array `nums`, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# input = [0, 1, 0, 3, 12]
# output = [1, 3, 12, 0, 0]

def moveZerosToEnd(nums):
    n = len(nums)
    if n == 0:
        return nums
    
    left, right = 0, 0
    
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    
    return nums

d = [0, 1, 0, 3, 12]
print(moveZerosToEnd(d))