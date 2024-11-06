class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node()
    
  def append(self, data):
    new_node = Node(data)
    current = self.head
    while current.next != None:
      current = current.next
    current.next = new_node
    
  def display(self):
    elements = []
    current = self.head
    while current.next != None:
      current = current.next
      elements.append(current.data)
    return elements

  def remove(self, data):
    current = self.head
    while current.next != None:
      previous = current
      current = current.next
      if current.data == data:
        previous.next = current.next
        return True
    return False

#Test

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

print(linked_list.display()) #[1, 2, 3, 4, 5, 6]

linked_list.remove(3)
print(linked_list.display()) #[1, 2, 4, 5, 6]