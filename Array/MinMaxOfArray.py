def findMinMax(s):
    if len(s) == 0:
        return None
    
    if len(s) == 1:
        return s[0], s[0]

    if s[0] > s[1]:
        minEle, maxEle = s[1], s[0]
    else:
        minEle, maxEle = s[0], s[1]

    for i in range(2, len(s)):
        if s[i] > maxEle:
            maxEle = s[i]
        if s[i] < minEle:
            minEle = s[i]

    return minEle, maxEle

print(findMinMax([2, 6, 9, 3, 5, 8, 1]))


# With the above approach, we are comparing the elements in pairs. So, the total number of comparisons will be 1 + 2(n-2) in the worst case. Therefore, the time complexity of this approach is O(n).
# The space complexity of this approach is O(1) as we are using only a constant amount of extra space.
# The above approach is the optimal approach to solve this problem. We can solve this problem in O(n) time complexity and O(1) space complexity.
# Now let's implement with less number of comparisons.

def findMinMax(s):
    if len(s) == 0:
        return None
    
    if len(s) == 1:
        return s[0], s[0]
    
    if len(s) % 2 == 0:
        if s[0] > s[1]:
            minEle, maxEle = s[1], s[0]
        else:
            minEle, maxEle = s[0], s[1]
        start = 2
    else:
        minEle, maxEle = s[0], s[0]
        start = 1
    
    for i in range(start, len(s), 2):
        if s[i] > s[i+1]:
            maxEle = max(maxEle, s[i])
            minEle = min(minEle, s[i+1])
        else:
            maxEle = max(maxEle, s[i+1])
            minEle = min(minEle, s[i])

    return minEle, maxEle

# Test
print(findMinMax([2, 6, 9, 3, 5, 8, 1]))
