def best_time_to_buy_stock(prices):
  max_profit = 0
  
  for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
      max_profit += prices[i] - prices[i - 1]
  return max_profit

# Time complexity: O(n)
# Space complexity: O(1)
#Test cases
print(best_time_to_buy_stock([7,1,5,3,6,4])) #7
print(best_time_to_buy_stock([7,6,4,3,1])) #0
print(best_time_to_buy_stock([1,2])) #1