class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    def insert(self, key):
        if self.val:
            if key < self.val:
                if self.left is None:
                    self.left = TreeNode(key)
                else:
                    self.left.insert(key)
            elif key > self.val:
                if self.right is None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
        else:
            self.val = key
            
    def preorder_traversal(self, root):
        if root:
            print(root.val)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
            
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val)
            self.inorder_traversal(root.right)
            
#Test
root = TreeNode(12)
root.insert(6)
root.insert(14)
root.insert(3)

# root.preorder_traversal(root) #12 6 3 14
root.inorder_traversal(root) #3 6 12 14
