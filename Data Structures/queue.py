#queue.py not built in data structure for specialized requirments
class queue:
    def __init__(self):
        self.data = []

    def __str__(self):
        for i in self.data:
            print ('{}'.format(i),end=' --> ')
    
    def enqueue(self,el):
        self.data.insert(0,el)
    
    def dequeue(self):
        self.data.pop()
    
    

a = queue()
a.enqueue(3)
a.enqueue(4)
a.enqueue(45)
a.enqueue(123)
a.__str__()
print('\n')
a.dequeue()
#a.print_queue()
