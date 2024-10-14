def minimumSizeSubArray(nums, target):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
      current_sum += nums[right]

      while current_sum >= target:
        min_length = min(min_length, right-left +1)
        current_sum -= nums[left]
        left +=1

    return 0 if min_length == float('inf') else min_length
  
# Test cases
print(minimumSizeSubArray([2,3,1,2,4,3], 7)) # 2