def findTheMissingNumber(s):
    n = len(s) + 1
    total = n * (n + 1) // 2
    return total - sum(s)
  
# Test
print(findTheMissingNumber([1, 2, 4, 5, 6, 7, 8])) 