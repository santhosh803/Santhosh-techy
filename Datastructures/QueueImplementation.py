# Queue Implementation Using Deque() from Collections

from collections import deque

class Queue:
    def __init__(self):
        self.container = deque() # Queue

    def enqueue(self, data):
        self.container.appendleft(data)        
    
    def dequeue(self):
        return self.container.pop()
    
    def atFront(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

q = Queue()
q.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
q.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
q.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})
print(q.container)
print(q.dequeue())
print(q.isEmpty())
print(q.size())

print(q.container)
print(q.atFront())
