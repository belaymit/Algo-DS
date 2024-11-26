#Inset delete get random in O(1)
#https://leetcode.com/problems/insert-delete-getrandom-o1/
#Design a data structure that supports all following operations in average O(1) time.
#
#insert(val): Inserts an item val to the set if not already present.
#remove(val): Removes an item val from the set if present.
#getRandom: Returns a random element from current set of elements. 
# Each element must have the same probability of being returned.

class RandomizedSet:
  
      def __init__(self):
          """
          Initialize your data structure here.
          """
          self.data = []
          self.data_dict = {}
          
  
      def insert(self, val: int) -> bool:
          """
          Inserts a value to the set. Returns true if the set did not already contain the specified element.
          """
          if val in self.data_dict:
              return False
          self.data.append(val)
          self.data_dict[val] = len(self.data) - 1
          return True
          
  
      def remove(self, val: int) -> bool:
          """
          Removes a value from the set. Returns true if the set contained the specified element.
          """
          if val not in self.data_dict:
              return False
          last_element, idx = self.data[-1], self.data_dict[val]
          self.data[idx], self.data_dict[last_element] = last_element, idx
          self.data.pop()
          del self.data_dict[val]
          return True
          
  
      def getRandom(self) -> int:
          """
          Get a random element from the set.
          """
          import random
          return random.choice(self.data)
        
#Test cases
obj = RandomizedSet()
print(obj.insert(1)) #True
print(obj.remove(2)) #False
print(obj.insert(2)) #True
print(obj.getRandom()) #1 or 2
print(obj.remove(1)) #True
print(obj.insert(2)) #False
print(obj.getRandom()) #2
