# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Max Halpern

class Stack:    

    def __init__(self):
        self.data = []
        
    
    def is_empty(self):
        return self.data == []

    
    def pop(self):
        if self.is_empty():
            raise IndexError("Index Error! Stack is empty.")
        else:
            last = self.data[-1]
            self.data.pop()
            return last

    def peek(self):
        if self.is_empty():
            raise IndexError("Index Error! Stack is empty.")
        else:
            value = self.data[-1]
            return value

    def push(self,item):
        self.data.append(item)