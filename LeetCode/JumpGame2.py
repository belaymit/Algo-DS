#Jump game 2
#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Your goal is to reach the last index in the minimum number of jumps.
#For example:
#A = [2,3,1,1,4] return 2.
#The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#A = [2,3,0,1,4] return 2.
#The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#A = [1,2] return 1.

def jump_game_2(nums):
  destination = len(nums) - 1
  jumps = 0
  current_jump_end = 0
  coverages = 0
  
  if destination == 0:
    return 0
  
  if len(nums) == 1:
    return 0

  for i in range(len(nums)):
    coverages = max(coverages, i + nums[i])
    
    if i == current_jump_end:
      current_jump_end = coverages
      jumps += 1
      
      if coverages >= destination:
        break
  return jumps

#Time complexity: O(n)
#Space complexity: O(1)

#Test cases
print(jump_game_2([2,3,1,1,4])) #2
print(jump_game_2([2,3,0,1,4])) #2
print(jump_game_2([1,2])) #1
print(jump_game_2([0])) #0
print(jump_game_2([1])) #0