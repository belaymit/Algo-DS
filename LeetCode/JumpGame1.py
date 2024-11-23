#Jump Game
#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.
#For example:
#A = [2,3,1,1,4], return true.
#A = [3,2,1,0,4], return false.

def can_jump(nums):
  finalPos = len(nums) - 1
  for i in range(len(nums) - 1, -1, -1):
    if i + nums[i] >= finalPos:
      finalPos = i
  return finalPos == 0

#Time complexity: O(n)
#Space complexity: O(1)

#Test cases
print(can_jump([2,3,1,1,4])) #True
print(can_jump([3,2,1,0,4])) #False
print(can_jump([1,2])) #True
print(can_jump([0])) #True
print(can_jump([0,1])) #False
print(can_jump([1,0])) #True
print(can_jump([1,0,1])) #False
print(can_jump([1,1,1,1,1])) #True