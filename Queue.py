class Queue:

    def __init__(self,size):
        self.size = size
        self.list = [None for i in range(size)]
        self.front = self.rear = -1
    
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self,element):
        if self.is_full():
            print("Queue is Full, cannot perform Enqueue on {}".format(element))
        else:
            if self.is_empty():
                self.rear += 1
                self.front += 1
                self.list[self.rear] = element
            else:
                self.rear +=1
                self.list[self.rear] = element
        return

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty, cannot perform Dequeue operation") 
        else:
            if self.front < self.rear:
                self.front +=1
            elif self.front == self.rear:
                self.front = self.rear = -1
        return
        
    def posterior(self):
        if self.is_empty():
            return None
        else:
            return self.list[self.rear]

    def frontier(self):
        if self.is_empty():
            return None
        else:
            return self.list[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        else:
            print("Queue is:")
            position = self.front
            while position <= self.rear:
                print(self.list[position],end=" ")
                position += 1
            print("\n")
        
