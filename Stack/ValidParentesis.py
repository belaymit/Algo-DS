def isValid(s: str) -> bool:
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    
    stack = []
    
    for char in s:
        if char in matching_pairs:
            top_element = stack.pop() if stack else '#'
            
            if matching_pairs[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack
      

#Test
print(isValid("()")) #True
print(isValid("()[]{}")) #True
print(isValid("(]")) #False