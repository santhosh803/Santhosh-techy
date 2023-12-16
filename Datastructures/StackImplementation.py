# Stack Implementation Using Deque() from Collections

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque() # Stack

    def push(self, data):
        self.container.append(data)        
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
print(stack.container)
print(stack.pop())
print(stack.isEmpty())
print(stack.size())
print(stack.peek())
print(stack.container)