class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        pass
    
    def insert(self, root, key):
        if(root == None):
            return Node(key)
        elif(root.value < key):
            root.right = self.insert(root.right, key)
        elif(root.value > key):
            root.left = self.insert(root.left, key)
    

    def inOrder(self, root):
        l1 = list()
        if(root == None):
            return l1
        l2 = list()
        l2 = self.inOrder(root.left)
        l1.extend(l2)
        l1.append(root.value)
        l2 = self.inOrder(root.right)
        l1.extend(l2)
        return l1
    
    def isSorted(self, l):
        n = len(l)
        if(n == 0):
            return True
        i = n-1
        while i>=1:
            if(l[i] > l[i-1]):
                i = i - 1
            else:
                return False
        
        return True

    def checkBST(self, root):
        print(self.isSorted(self.inOrder(root)))


BST = BinarySearchTree()
v = [4,2,5,1,3]
parent = None
for i in v:
    parent = BST.insert(parent, i)
BST.checkBST(parent)
