// Given two sorted arrays nums1 and nums2 of size m and n respectively,
// return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n)).

// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.

const findMedianSortedArrays = (nums1, nums2) => {
  const data = nums1.concat(nums2);
  data.sort((a, b) => a - b);

  const midPoint = Math.floor(data.length / 2);
  const median = data.length % 2 === 1 ? data[midPoint] : (data[midPoint - 1] + data[midPoint]) / 2;
  return median;
};

const A1 = [1, 3];
const A2 = [2];
findMedianSortedArrays(A1, A2);

const nums1 = [1, 2];
const nums2 = [3, 4];

findMedianSortedArrays(nums1, nums2);