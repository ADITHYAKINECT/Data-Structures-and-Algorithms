class Node(object):

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