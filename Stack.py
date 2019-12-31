class Stack:
    
    def __init__(self,size):
        self.size = size
        self.list = [None for i in range(size)]
        self.top = -1

    def is_empty(self):
        return self.top == -1 
    
    def is_full(self):
        return self.top == self.size - 1

    def push(self,element):
        if self.is_full():
            print("Stack is Overflowing!, cannot push {} into the stack".format(element))
        else:
            self.top += 1
            self.list[self.top] = element 

    def pop(self):
        if self.is_empty():
            print("Stack is Empty, cannot perfrom pop operation")
        else:
            posterior = self.list[self.top]
            self.top -= 1  
            return posterior
    
    def display(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Stack is: ")
            position = self.top
            while position:
                print(self.list[position],end=" ")
                position -= 1
            print("\n")
