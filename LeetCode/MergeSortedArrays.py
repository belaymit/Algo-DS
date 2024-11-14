#Merge sorted arrays
#Given two sorted arrays, merge them into one sorted array.
#Example:
#Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
#Output: [1, 2, 3, 4, 5, 6]
#Approach:
#1. Initialize an empty array merged.
#2. Initialize two pointers i and j to 0.
#3. Compare the elements at i and j.
#4. Append the smaller element to the merged array.
#5. Increment the pointer of the smaller element.
#6. Repeat steps 3-5 until one of the arrays is exhausted.
#7. Append the remaining elements of the other array to the merged array.
#8. Return the merged array.
#Complexity Analysis:
#The time complexity for this approach is O(n+m), where n and m are the lengths of the two arrays.
#The space complexity is O(n+m) as we are using an extra array to store the merged result.

def merge_sorted_arrays(arr1, arr2):
  merged = []
  i = j = 0
  
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      merged.append(arr1[i])
      i += 1
    else:
      merged.append(arr2[j])
      j += 1
      
  merged.extend(arr1[i:])
  merged.extend(arr2[j:])
  
  return merged

#Test
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6])) #[1, 2, 3, 4, 5, 6]
print(merge_sorted_arrays([1, 3, 5], [2, 4])) #[1, 2, 3, 4, 5]
print(merge_sorted_arrays([1, 3], [2, 4, 6])) #[1, 2, 3, 4, 6]