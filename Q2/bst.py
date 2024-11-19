class TreeNode:

    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)


    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)

    def find(self,value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True

    

tree = TreeNode(50)

tree.insert(5)
tree.insert(2)
tree.insert(23)
tree.insert(12)
tree.insert(45)
tree.insert(10)
tree.insert(55)
tree.insert(22)
tree.insert(67)
tree.insert(1)
tree.insert(33)

print(tree.inorder())
print(tree.preorder())
print(tree.postorder())