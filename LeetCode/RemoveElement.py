#Remove and element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. 
# For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
#Approach:
#1. Initialize a pointer i to 0.
#2. Iterate through the array.
#3. If the element at i is equal to the target value, replace it with the last element of the array.

def remove_element(nums, val):
  i = 0
  for j in range(len(nums)):
    if nums[j] != val:
      nums[i] = nums[j]
      i += 1
  return i

#Test
print(remove_element([3,2,2,3], 3)) #2
print(remove_element([0,1,2,2,3,0,4,2], 2)) #5
print(remove_element([1], 1)) #0
print(remove_element([1], 2)) #1
print(remove_element([1, 1], 1)) #0
print(remove_element([1, 1], 2)) #2
print(remove_element([1, 2], 1)) #1
print(remove_element([1, 2], 2)) #1