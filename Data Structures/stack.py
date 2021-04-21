#stack.py not built in data structure for specialized requirments 
class stack:
    def __init__(self):
        self.data = []

    def add(self,el):
        self.data.insert(0,el)
    
    def pop(self):
        self.data.pop(0)

    def print_stack(self):
        for i in self.data:
            print('|',i,end='|\n')
        
    def is_empty(self):
        return self.data == []

a = stack()
print(a.is_empty())
a.add('a')
a.add('b')
a.add('c')
a.add('d')
a.add('e')
a.print_stack()
print(a.is_empty())
a.pop()
a.pop()
a.pop()
a.print_stack()
