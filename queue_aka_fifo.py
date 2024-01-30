"""
    Program implements the Queue class with two basic operations:
    - put(element), which puts an element at end of the queue;
    - get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)
"""

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, element):
        self.queue.insert(0, element)

    def get(self):
        if len(self.queue) > 0:
            value = self.queue[-1]
            del self.queue[-1]
            return value
        else:
            raise QueueError

queue = Queue()
queue.put(1)
queue.put("dog")
queue.put(False)
try:
    for i in range(4):
        print(queue.get())
except QueueError:
    print("Queue error")
