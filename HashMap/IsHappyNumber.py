def isHappyNumber(num):
    num_map = {}
    
    while num != 1:
        num_map[num] = True
        num = sum([int(i) ** 2 for i in str(num)])
        
        if num in num_map:
            return False
    
    return True
  
#Test
print(isHappyNumber(19)) # True
print(isHappyNumber(2)) # False
print(isHappyNumber(82)) # True