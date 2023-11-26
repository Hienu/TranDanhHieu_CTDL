def dequeue(self):
    if self.is_empty():
        print("Queue is empty")
        return
    element = self.front.element
    self.front = self.front.next
    self.size -= 1
    if self.is_empty():
        self.rear = None
    return element
