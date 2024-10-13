def isSubsequence(s, t):
    if not s:
        return True
      
    i = 0
    
    for c in t:
        if c == s[i]:
            i += 1
            if i == len(s):
                return True
    return False
  
# Test
print(isSubsequence("abc", "ahbgdc")) # True

def isSubsequence2(s, t):
  pointer_s, pointer_2 = 0, 0
  
  while pointer_s < len(s) and pointer_2 < len(t):
    if s[pointer_s] == t[pointer_2]:
      pointer_s += 1
    pointer_2 += 1
  return pointer_s == len(s)

# Test
print(isSubsequence2("abc", "ahbgdc")) # True