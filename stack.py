class Stack():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.items == []:
            return self.items[-1]
        
        
    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
        
my_stack = Stack()
print(my_stack.is_empty())
my_stack.push(1)
my_stack.push('A')
my_stack.push(87)
print(my_stack.get_stack())
my_stack.pop()
print(my_stack.get_stack())
print(my_stack.is_empty())
print(my_stack.peek())
        