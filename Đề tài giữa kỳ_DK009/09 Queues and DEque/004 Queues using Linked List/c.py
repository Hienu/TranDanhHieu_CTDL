def first(self):
    if self.is_empty():
        print("Queue is empty")
        return
    return self.front.element
