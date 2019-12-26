from random import randint
from Node import Node

class binary_search_tree(object):

    def __init__(self,value = None):
        self.root = Node(value)

    # Public Methods
    def insert(self,key):
        if self.root.data is None:
            print("Tree is Empty, Adding key = {} as the root".format(key))
            self.root = Node(key)
            return
        else:
            print("Adding---->{}".format(key))
            self.__insert(self.root,key)
            return

    def display(self):
        if self.root.data is None:
            print("Tree is Empty")
        else:
            print("Preorder Traversal:")
            self.__preorder(self.root)
        return

    def search(self,key):
        if self.root.data is None:
            print("Tree is Empty")
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
            print("Minimum Value from Recursion: ",min_value)

    def minimum_node_iterative(self):
        min_value = self.__minimum_node_iterative(self.root)
        if  min_value is None:
            print("Tree is Empty")
        else:
            print("Minimum Value from Iterative Method: ",min_value) 
    
    def maximum_node_recursion(self):
        max_value = self.__maximum_node_recursion(self.root)
        if max_value is None:
            print("Tree is Empty")
        else:
            print("Maximum Value from Recursion: ", max_value)

    def maximum_node_iterative(self):
        max_value = self.__maximum_node_iterative(self.root)
        if  max_value is None:
            print("Tree is Empty")
        else:
            print("Maximun Value from Iterative Method: ",max_value) 

    def count_leaves(self):
        print("Number of Leaves in tree: ",self.__count_leaves(self.root))

    # Private Methods
    def __count_leaves(self,parent):
        if parent is None:
            return 0
        elif parent.get_value() is not None and not parent.has_left_child() and not parent.has_right_child():
            return 1
        else:
            return self.__count_leaves(parent.get_left_child()) + self.__count_leaves(parent.get_right_child())

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
        if parent is None or parent.data is None:
            return
        else:
            self.__preorder(parent.get_left_child())
            print(parent.data,end=" ")
            self.__preorder(parent.get_right_child())
        return


    def delete(self,key):
        if self.root.data is None:
            print("Tree is empty")
            return
        else:
            self.root.data = self.__delete(self.root,key)
            return

    def __delete(self, parent,key):
        if parent.get_value() == key:
            print("Deleteing Key = {}".format(parent.get_value()))
            if not parent.has_left_child() and not parent.has_right_child():
                parent.set_value(None)
            elif parent.has_left_child() and not parent.has_right_child():
                x = self.__maximum_node_iterative(parent.get_left_child())
                parent.set_value(x)
            elif parent.has_right_child() and parent.has_left_child():
                x = self.__minimum_node_recursion(parent.get_right_child())
                parent.set_value(x)
        elif parent.get_value() > key:
            x = self.__delete(parent.get_left_child(),key)
            parent.left.set_value(x)
        elif parent.get_value() < key:
            x = self.__delete(parent.get_right_child(),key)
            parent.right.set_value(x)
        return parent.get_value()
    

""" Construct a simple Binary Search Tree
                     15
                   /    \
                  7     20
                /  \    / \
               3   9   18  22
              / \
             1   4 
            /
          -10                         """
tree = binary_search_tree()
tree.insert(15)
tree.insert(7)
tree.insert(3)
tree.insert(9)
tree.insert(1)
tree.insert(4)
tree.insert(-10)
tree.insert(20)
tree.insert(18)
tree.insert(22)
tree.display()
tree.minimum_node_iterative()
tree.minimum_node_recursion()
tree.maximum_node_iterative()
tree.maximum_node_recursion()
tree.count_leaves()
tree.delete(int(input("\nDelete an Element: ")))
tree.search(int(input("\nEnter the search Element: ")))
tree.display()