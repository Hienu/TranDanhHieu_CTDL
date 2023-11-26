class QueueArray:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.data.pop(0)

    def first(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.data[0]
