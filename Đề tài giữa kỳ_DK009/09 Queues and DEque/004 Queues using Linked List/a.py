def enqueue(self, element):
    newest = Node(element, None)
    if self.is_empty():
        self.front = newest
    else:
        self.rear.next = newest
    self.rear = newest
    self.size += 1
