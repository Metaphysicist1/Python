#queue.py not built in data structure for specialized requirments
class queue:
    #constructor
    def __init__(self):
        self.data = []
    #printing
    def __str__(self):
        for i in self.data:
            print ('{}'.format(i),end=' --> ')
    # add element
    def enqueue(self,el):
        self.data.insert(0,el)
    # delete element
    def dequeue(self):
        self.data.pop()
    # queue's size
    def length(self):
        print(len(self.data))

    
    
    

a = queue()
a.enqueue(3)
a.enqueue(4)
a.enqueue(45)
a.enqueue(123)
a.__str__()
print('\n')
a.dequeue()
a.length()
