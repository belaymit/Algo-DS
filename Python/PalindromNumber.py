# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -2^31 <= x <= 2^31 - 1

def palindromeNumber(x: int) -> bool:
    if x < 0:
        return False
    x_str = str(x)
    return x_str == x_str[::-1]

# Example usage:
print(palindromeNumber(121))  
print(palindromeNumber(-121)) 
print(palindromeNumber(10)) 
