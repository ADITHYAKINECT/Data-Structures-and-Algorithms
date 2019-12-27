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
        else:
            if self.__search(self.root,key):
                print("\nKey = {} is Present!".format(key))
            else:
                print("\nKey = {} is Absent!".format(key))
        return

    def count_leaves(self):
        print("Number of Leaves in tree: ",self.__count_leaves(self.root))

    def delete(self,key):
        if self.root.data is None:
            print("Tree is empty")
        else:
            self.root.data = self.__delete(self.root,key)
        return    

    def count_all_nodes(self):
        print("Total Number of Nodes in tree {}".format(self.__count_all_nodes(self.root)))    

    # Private Methods
    def __count_all_nodes(self,parent):
        if parent is None or parent.get_value() is None:
            return 0
        elif parent is not None and not parent.has_left_child() and not parent.has_right_child():
            return 1
        else:
            return self.__count_all_nodes(parent.get_left_child()) + self.__count_all_nodes(parent.get_right_child()) + 1 


    def __count_leaves(self,parent):
        if parent.get_value() is None or parent is None:
            return 0
        elif not parent.has_left_child() and not parent.has_right_child():
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

    def __delete(self, parent,key):

        if parent.get_value() == key:
            print("Element Found = {}".format(parent.get_value()))
            # Delete a Leaf Node
            if not parent.has_left_child() and not parent.has_right_child():
                parent.set_value(None)

            # Delete a Node with Left Subtree 
            elif parent.has_left_child() and not parent.has_right_child():
                x = self.__maximum_node_iterative(parent.get_left_child())
                parent.set_value(x)

            # Delte a Node with Right Subtree
            elif parent.has_right_child() and not parent.has_left_child():
                x = self.__minimum_node_recursion(parent.get_right_child())
                parent.set_value(x)

            # Delete a Node with Left and Right Subtree
            elif parent.has_right_child() and parent.has_left_child():
                x = self.__minimum_node_recursion(parent.get_right_child())
                parent.set_value(x)

        # If the key is lesser than current node's value, search in its left subtree  
        elif parent.get_value() > key:
            x = self.__delete(parent.get_left_child(),key)
            parent.left.set_value(x)

        # If the key is greater than current node's value, search in its right subtree
        elif parent.get_value() < key:
            x = self.__delete(parent.get_right_child(),key)
            parent.right.set_value(x)
    
        return parent.get_value()
    
""" Construct a simple Binary Search Tree
                     15
                   /    \
                  7     20
                /  \    / \
               2    9  18 22
              / \  / \
             1   5 8  10
                / \
               4   6                   """
tree_elements = [15,7,9,2,1,5,10,8,20,18,22,4,6]
# tree_elements = [15,20,7,9]           
tree = binary_search_tree()
for element in tree_elements:
    tree.insert(element)
tree.count_leaves()
tree.display()
tree.delete(int(input("\nDelete an Element: ")))
tree.search(int(input("\nEnter the search Element: ")))
tree.count_all_nodes()
tree.display()
