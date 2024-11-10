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
            

#Test
root = LinkedList(12)
root.insert(6)
root.insert(14)
root.insert(3)
# root.print_list() #12 6 14 3
root = root.reverse()
root.print_list() #3 14 6 12
