def isArray1SubsetOfArray2(arr1, arr2):
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            return False
    return True
  
# Test
# print(isArray1SubsetOfArray2([1, 2, 3], [1, 2, 3, 4, 5])) # True

def checkArray1SubsetOfArray2(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    
    return set1.issubset(set2)
  
# Test
print(checkArray1SubsetOfArray2([1, 2, 3], [1, 2, 3, 4, 5])) # True