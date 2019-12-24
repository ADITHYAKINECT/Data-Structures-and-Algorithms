from random import randint

class Node(object):

    def __init__(self,value=None):
        self.left = None
        self.data = value
        self.right = None

    def set_node_value(self,value=None):
        self.data = value

    def get_node_value(self):
        return self.data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self,node_x):
        self.left = node_x

    def set_right_child(self,node_x):
        self.right = node_x

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

class Tree(object):

    def __init__(self,value = None):
        self.root = Node(value)

    # Public Methods
    def insert(self,key):
        if self.root.data is None:
            print("\nTree is Empty, Adding key = {} as the root".format(key))
            self.root = Node(key)
            return
        else:
            self.__insert(self.root,key)
            return

    def delete(self,key):
        if self.root.data is None:
            print("\nTree is empty")
            return
        else:
            self.__delete(self.root,key)
            return

    def preorder(self):
        if self.root.data is None:
            print("\nTree is Empty")
        else:
            print("Preorder Traversal:")
            self.__preorder(self.root)
        return

    def search(self,key):
        if self.root.data is None:
            print("\nTree is Empty")
            return
        else:
            if self.__search(self.root,key):
                print("\nKey = {} is Present!".format(key))
            else:
                print("\nKey ={} is Absent!".format(key))
            return

    # Private Methods
    def __search(self,parent,key):
        if parent.data is None:
            return False
        elif parent.data == key:
            return True
        else:
            if parent.data > key:
                if parent.left is not None:
                    return self.__search(parent.left,key)
            elif parent.data < key:
                if parent.right is not None:
                    return self.__search(parent.right,key)

    def __insert(self,parent,key):
        if parent.data is None:
            return
        else:
            if parent.data > key:
                if parent.left is None:
                    parent.left = Node(key)
                else:
                    self.__insert(parent.left,key)
            elif parent.data < key:
                if parent.right is None:
                    parent.right = Node(key)
                else:
                    self.__insert(parent.right,key)
        return

    def __preorder(self,parent):
        if parent is None:
            return
        else:
            self.__preorder(parent.left)
            print(parent.data,end=" ")
            self.__preorder(parent.right)
        return

    def __delete(self, parent,key):
        pass


try:
    while True:
        root_value = int(input("\nEnter the root node value: "))
        tree = Tree(root_value)
        count = int(input("\nEnter the number of Nodes: "))
        while count:
            tree.insert(randint(-root_value,root_value))
            count = count - 1
        tree.preorder()
        tree.search(int(input("\nEnter the search Element")))
except KeyboardInterrupt:
    print("\nTerminating the Program")