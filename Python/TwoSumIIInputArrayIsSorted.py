def  TwoSumIIInputArrayIsSorted(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return []
  
# Test
print(TwoSumIIInputArrayIsSorted([2, 7, 11, 15], 9)) # [1, 2]