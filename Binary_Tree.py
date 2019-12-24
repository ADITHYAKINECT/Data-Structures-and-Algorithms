from random import randint
from Node import Node

class binary_search_tree(object):

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
    print("Press Control + C to terminate the program")
    while True:
        root_value = int(input("\nEnter the root node value: "))
        tree = binary_search_tree(root_value)
        count = int(input("\nEnter the number of Nodes: "))
        while count:
            tree.insert(randint(-root_value,root_value))
            count = count - 1
        tree.preorder()
        tree.search(int(input("\nEnter the search Element")))
except KeyboardInterrupt:
    print("\nTerminating the Program")