def reverseAnArray(s):
  n = len(s)
  i, j = 0, n-1
  for i in range(n//2):
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
    
  return s

print(reverseAnArray([1,2,3,4,5])) # [5,4,3,2,1]