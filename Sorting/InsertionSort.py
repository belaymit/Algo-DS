#It is a sorting algorithm that builds the final sorted array (or list) one item at a time.
#It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
#However, insertion sort provides several advantages:
#Simple implementation: Jon Bentley shows a three-line C version, and a five-line optimized version
#Efficient for (quite) small data sets, much like other quadratic sorting algorithms
#More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort
#Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(nk) when each element in the input is no more than k places away from its sorted position
#Stable; i.e., does not change the relative order of elements with equal keys
#In-place; i.e., only requires a constant amount O(1) of additional memory space
#Online; i.e., can sort a list as it receives it
#When people manually sort cards in a bridge hand, most use a method that is similar to insertion sort.

#Example:
#To sort an array of size n in ascending order:
#1: Iterate from arr[1] to arr[n] over the array.
#2: Compare the current element (key) to its predecessor.
#3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

#Time Complexity: O(n^2) as there are two nested loops.
#Auxiliary Space: O(1)
#The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr

#Test
print(insertion_sort([64, 25, 12, 22, 11])) #[11, 12, 22, 25, 64]