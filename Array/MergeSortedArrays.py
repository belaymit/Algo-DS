def mergeSortedArrays(arr1, arr2):
    arr1_index = 0
    arr2_index = 0
    merged = []
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        if arr1[arr1_index] < arr2[arr2_index]:
            merged.append(arr1[arr1_index])
            arr1_index += 1
        else:
            merged.append(arr2[arr2_index])
            arr2_index += 1
            
    # If there are still elements in arr1 or arr2 or left over
    while arr1_index < len(arr1):
        merged.append(arr1[arr1_index])
        arr1_index += 1
        
    while arr2_index < len(arr2):
        merged.append(arr2[arr2_index])
        arr2_index += 1
        
    return merged
  
# Test
print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30])) # [0, 3, 4, 4, 6, 30, 31]