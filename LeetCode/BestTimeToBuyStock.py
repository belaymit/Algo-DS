def best_time_to_buy_stock(prices):
  max_profit = 0
  
  for i in range(len(prices) - 1):
    for j in range(i + 1, len(prices)):
      profit = prices[j] - prices[i]
      if profit > max_profit:
        max_profit = profit
  return max_profit

# Time complexity: O(n^2)
# Space complexity: O(1)
#Test cases
# print(best_time_to_buy_stock([7,1,5,3,6,4])) #5
# print(best_time_to_buy_stock([7,6,4,3,1])) #0
# print(best_time_to_buy_stock([1,2])) #1


#Optimized solution
def best_time_to_buy_stock2(prices):
  max_profit = 0
  min_price = float('inf')
  
  for price in prices:
    min_price = min(min_price, price)
    profit = price - min_price
    max_profit = max(max_profit, profit)
  return max_profit

# Time complexity: O(n)
# Space complexity: O(1)
#Test cases
print(best_time_to_buy_stock2([7,1,5,3,6,4])) #5
print(best_time_to_buy_stock2([7,6,4,3,1])) #0
