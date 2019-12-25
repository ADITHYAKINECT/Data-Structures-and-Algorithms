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

    def display(self):
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
                print("\nKey = {} is Absent!".format(key))
            return

    def minimum_node_recursion(self):
        min_value = self.__minimum_node_recursion(self.root)
        if  min_value is None:
            print("Tree is Empty")
        else:
            print("\nMinimum Value from Recursion: ",min_value)

    def minimum_node_iterative(self):
        min_value = self.__minimum_node_iterative(self.root)
        if  min_value is None:
            print("Tree is Empty")
        else:
            print("\nMinimum Value from Iterative Method: ",min_value) 
    
    def maximum_node_recursion(self):
        max_value = self.__maximum_node_recursion(self.root)
        if max_value is None:
            print("\nTree is Empty")
        else:
            print("Maximum Value from Recursion: ", max_value)

    def maximum_node_iterative(self):
        max_value = self.__maximum_node_iterative(self.root)
        if  max_value is None:
            print("Tree is Empty")
        else:
            print("\nMaximun Value from Iterative Method: ",max_value) 

    # Private Methods
    def __maximum_node_iterative(self,parent):
        while parent.has_right_child():
            parent = parent.get_right_child()
        return parent.get_value()    

    def __maximum_node_recursion(self,parent):
        if parent.get_value() is None:
            return
        elif parent.has_right_child():
            return self.__maximum_node_recursion(parent.get_right_child())
        else:
            return parent.get_value()    

    def __minimum_node_iterative(self,parent):
        while parent.has_left_child():
            
            parent = parent.get_left_child()
        return parent.get_value()    

    def __minimum_node_recursion(self,parent):
        if parent.get_value() is None:
            return
        elif parent.has_left_child():
            return self.__minimum_node_recursion(parent.get_left_child())
        else:
            return parent.get_value()    

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
            tree.insert(randint(0,2*root_value))
            count = count - 1
        
        tree.minimum_node_iterative()
        tree.maximum_node_iterative()
        tree.search(int(input("\nEnter the search Element: ")))
        tree.display()
except KeyboardInterrupt:
    print("\nTerminating the Program")
