# Create a Node Class

class Node():

    def __init__(self,value = None):
        self.left = None
        self.data = value
        self.right = None

    def set_value(self,value):
        self.data = value

    def get_value(self):
        return self.data

    def set_left_child(self,left_child):
        self.left = Node(left_child)

    def set_right_child(self,right_child):
        self.right = Node(right_child)

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

# Create a Tree class

class Tree():

    def __init__(self,value = None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    # Tree Traversals using recursion

    def inorder(self,x):
        if x is None:
            return
        else:
            self.inorder(x.get_left_child())
            print(x.data)
            self.inorder(x.get_right_child())
        return

    def postorder(self,x):
        if x is None:
            return
        else:
            self.postorder(x.get_right_child())
            self.postorder(x.get_left_child())
            print(x.data)
        return

    def preorder(self,x):
        if x is None:
            return
        else:
            print(x.data)
            self.preorder(x.get_left_child())
            self.preorder(x.get_right_child())
        return

# Construct a tree
tree = Tree("Apple")
tree.get_root().set_left_child("Banana")
tree.get_root().set_right_child("Cherry")
tree.get_root().get_left_child().set_left_child("Dates")

# Check
print("\nInorder Walk:")
tree.inorder(tree.get_root())
print("\nPostorder Walk:")
tree.postorder(tree.get_root())
print("\nPreoder Walk:")
tree.preorder(tree.get_root())
