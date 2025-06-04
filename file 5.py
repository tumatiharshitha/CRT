class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def enqueue(self, value):
        self.queue.append(value)
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        value = self.queue[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = 0
            self.rear = -1
        return value

    def is_empty(self):
        return self.rear < self.front or self.rear == -1

    def size(self):
        if self.is_empty():
            return 0
        return self.rear - self.front + 1

# Create an object
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  
print(q.dequeue()) 
print(q.size())  
print(q.is_empty())  
print(q.dequeue())  
print(q.is_empty())  
print(q.dequeue())  



