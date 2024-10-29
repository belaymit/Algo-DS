def summaryRanges(nums):
    ranges = [] 
    start = 0  

    for i in range(1, len(nums) + 1):
        if i == len(nums) or nums[i] != nums[i - 1] + 1:
            if start == i - 1:
                ranges.append(str(nums[start]))
            else:
                ranges.append(f"{nums[start]}->{nums[i - 1]}")
            start = i 

    return ranges

#Test
print(summaryRanges([0,1,2,4,5,7])) #["0->2","4->5","7"]
print(summaryRanges([0,2,3,4,6,8,9])) #["0","2->4","6","8->9"]