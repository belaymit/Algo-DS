# Is the simplest sorting algorithm. 
# It works by selecting the smallest (or largest, depending on sorting order) element of the array and placing it at the beginning (or end) of the array. 
# It then repeats the process with the remaining elements until the array is sorted.

def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr

#Test
print(selection_sort([64, 25, 12, 22, 11])) #[11, 12, 22, 25, 64]