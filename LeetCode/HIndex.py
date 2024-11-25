#H-index
def hIndex(citations):
    citations.sort(reverse=True)
    
    h = 0 
    for i, citation in enumerate(citations):
        if i + 1 <= citation:
            h = i + 1 
        else:
            break  
    
    return h

#Test cases
print(hIndex([3,0,6,1,5])) #3
print(hIndex([100])) #1
print(hIndex([0])) #0
