class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class QueuesLinked:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

def __len__(self):
    return self.size

def is_empty(self):
    return self.size == 0

def enqueue(self, element):
    newest = Node(element)
    if self.is_empty():
        self.front = newest
    else:
        self.rear.next = newest
    self.rear = newest
    self.size += 1

def dequeue(self):
    if self.is_empty():
        print("Queue is empty")
        return
    e = self.front.element
    self.front = self.front.next
    self.size -= 1
    if self.is_empty():
        self.rear = None
    return e

def first(self):
    if self.is_empty():
        print("Queue is empty")
        return
    return self.front.element

def display(self):
    p = self.front
    while p:
        print(p.element, end=' ')
        p = p.next
    print()

queue = QueuesLinked()
queue.enqueue(5)
queue.enqueue(3)
queue.display()
print("Length:", len(queue))
queue.enqueue(7)
queue.enqueue(12)
queue.display()
print("Length:", len(queue))
queue.dequeue()
queue.display()
print("Length:", len(queue))
print("Front element:", queue.first())
