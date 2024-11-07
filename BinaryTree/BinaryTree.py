class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
    

class BinaryTree:
  def __init__(self, value):
    self.root = Node(value)
    
  
  def insert_left(self, current_node, value):
    if current_node.left is None:
      current_node.left = Node(value)
    else:
      new_node = Node(value)  
      new_node.left = current_node.left
      current_node.left = new_node
      
  def traverse(self, root):
    if root:
      print(root.value)
      self.traverse(root.left)
      self.traverse(root.right)
      
      
#Test
tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_left(tree.root.left, 3)
tree.insert_left(tree.root.left.left, 4)

tree.traverse(tree.root) #1 2 3 4

