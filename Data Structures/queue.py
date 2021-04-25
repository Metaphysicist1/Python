#queue.py not built in data structure for specialized requirments
class Node:
    def __init__(self,value):
        self.value = value

class Queue:
    #constructor initialization
    def __init__(self):
        self.data = []
    #printing queue
    def __str__(self):
        for i in self.data:
            print ('{}'.format(i),end=' --> ')
    # add element to queue
    def enqueue(self,value):
        self.data.insert(0,Node(value))
    # delete element from queue
    def dequeue(self):
        self.data.pop()
    # queue's size
    def length(self):
        print(len(self.data))
    #setter
    def setter(self,new):
        self.data= new
    #getter
    def getter(self):
        return self.data
    

    
    
    

a = Queue()

a.enqueue(Node(3))
a.enqueue(Node(4))
a.enqueue(Node(45))
a.enqueue(Node(123))
a.__str__()
print('\n')
a.dequeue()
a.length()
