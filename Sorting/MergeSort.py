#Merge Sort
#Merge Sort is a Divide and Conquer algorithm. 
# It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. 
# The merge() function is used for merging two halves. 
# The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
# Its time complexity is O(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
# It requires O(n) auxiliary space.
# It is stable as equal elements are not reordered.
# It is not in-place as it requires additional space.
# It is less efficient compared to the quick sort in the case of arrays.
# It is more efficient compared to the quick sort in the case of linked lists.
# It is used in external sorting.
# It is used in sorting linked lists.
# It is used in inversion count problem.
# It is used in external merge sort.
# It is used in count inversion in an array.

def merge_sort(arr):
  if(len(arr) <=1):
    return arr
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  
  left_sorted = merge_sort(left)
  right_sorted = merge_sort(right)
  
  return merge(left_sorted, right_sorted)

def merge(left, right):
  merged = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
      
  merged.extend(left[i:])
  merged.extend(right[j:])
  
  return merged

#Test
print(merge_sort([64, 34, 25, 12, 22, 11, 90])) #[11, 12, 22, 25, 34, 64, 90]
print(merge_sort([1, 2, 3, 4, 5])) #[1, 2, 3, 4, 5]
print(merge_sort([5, 4, 3, 2, 1])) #[1, 2, 3, 4, 5]