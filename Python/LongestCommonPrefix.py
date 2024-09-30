# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


def longestCommonPrefix(strs):
  if not strs:
    return ""
  shortest = min(strs, key=len)
  
  for i, char in enumerate(shortest):
    for string in strs:
      if string[i] != char:
        return shortest[:i]
  return shortest


def isCommonPrefix(strs, length):
    prefix = strs[0][:length]
    
    for string in strs[1:]:
        if not string.startswith(prefix):
            return False
    return True

def findLongestCommonPrefix(strs):
    if not strs:
        return ""
    min_len = len(min(strs, key=len))
    low, high = 0, min_len
    
    while low <= high:
        mid = (low + high) // 2
        if isCommonPrefix(strs, mid):
            low = mid + 1  
        else:
            high = mid - 1  
    
    return strs[0][:high]


print(findLongestCommonPrefix(["flower","flow","floight"])) 