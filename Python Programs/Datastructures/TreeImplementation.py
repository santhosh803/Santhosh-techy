class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)


    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def preorder_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.inorder_traversal()

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        if self.right:
            elements += self.right.inorder_traversal()

        elements.append(self.data)
        
        return elements
    
    def search(self, data):
        if data == self.data:
            return True
    
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
            

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def deleteRight(self, val):
        if val < self.data:
            if self.left:
                self.left.deleteRight(val)
        elif val > self.data:
            if self.right:
                self.right.deleteRight(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.deleteRight(min_value)


        return self
    
    def deleteLeft(self, val):
        if val < self.data:
            if self.left:
                self.left.deleteLeft(val)
        elif val > self.data:
            if self.right:
                self.right.deleteLeft(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.deleteLeft(max_value)


        return self

    
def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])


    return root

elements = [17, 4, 1, 20, 9, 23, 18, 13, 19, 34, 18, 4]
b_tree = build_tree(elements)
print(b_tree.inorder_traversal())
# print(b_tree.preorder_traversal())
# print(b_tree.postorder_traversal())

# print(b_tree.search(19))
# rootNode = b_tree.deleteRight(20)
rootNode = b_tree.deleteLeft(20)
print(rootNode.data)
print(b_tree.inorder_traversal())



