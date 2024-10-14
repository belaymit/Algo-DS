def threeSum(nums):
    if not nums or len(nums) < 3:
        return []
      
    nums.sort()
    result = set()
    
    for i in range(len(nums) - 2):
      left, right = i + 1, len(nums) - 1
      while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
          result.add((nums[i], nums[left], nums[right]))
          left += 1
          right -= 1
        elif total < 0:
          left += 1
        else:
          right -= 1

    return [list(triplet) for triplet in result]
  
#Test
print(threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]