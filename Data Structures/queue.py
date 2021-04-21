#queue.py not built in data structure for specialized requirments
class queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self,el):
        self.data.insert(0,el)
    
    def dequeue(self):
        self.data.pop()
    
    def print_queue(self):
        for el in self.data: 
            print(el, end=' --> ')

a = queue()
a.enqueue(3)
a.enqueue(4)
a.enqueue(45)
a.enqueue(123)
a.print_queue()
print('\n')
a.dequeue()
a.print_queue()

