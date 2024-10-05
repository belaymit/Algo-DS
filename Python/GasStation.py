def gasStation(gas, cost) -> int:
    totalGas = 0
    totalCost = 0
    startIndex = 0
    currentGas = 0
    
    for i in range(len(gas)):
        totalGas += gas[i]
        totalCost += cost[i]
        currentGas += gas[i] - cost[i]
        
        if currentGas < 0:
            startIndex = i + 1
            currentGas = 0
    
    if totalGas < totalCost:
        return -1
    
    return startIndex
  
print(gasStation([1,2,3,4,5], [3,4,5,1,2])) # 3
print(gasStation([2,3,4], [3,4,3])) # -1