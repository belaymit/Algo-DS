class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None 
       
    def insert(self, value):
        if self.value:
            if self.next is None:
                self.next = LinkedList(value)
            else:
                self.next.insert(value)
        else:
            self.value = value
            
    def print_list(self):
        while self: 
            print(self.value)
            self = self.next
    
    def reverse(self):
        prev = None
        current = self
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self = prev
        return self
            
    # Delete a node from a linked list by value
    
    def delete(self, value):
        if self.value == value:
            return self.next
        current = self
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return self
            current = current.next
        return self
    
    # Insert a node at a specific position in a linked list
    def insert_at(self, value, position):
        if position == 0:
            new_node = LinkedList(value)
            new_node.next = self
            return new_node
        current = self
        
        while position > 1 and current.next:
            current = current.next
            position -= 1
            
        new_node = LinkedList(value)
        new_node.next = current.next
        current.next = new_node
        return self

#Test
root = LinkedList(12)
root.insert(6)
root.insert(14)
root.insert(3)
# root.print_list() #12 6 14 3
root = root.reverse()
root.print_list() #3 14 6 12
