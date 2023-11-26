class DEQueue:
    def __init__(self):
        self.items = []

    def at_first(self, element):
        self.items.insert(0, element)

    def at_last(self, element):
        self.items.append(element)

    def remove_first(self):
        return self.items.pop(0) if self.items else None

    def remove_last(self):
        return self.items.pop() if self.items else None

    def first(self):
        return self.items[0] if self.items else None

    def last(self):
        return self.items[-1] if self.items else None

    def length(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

# Sử dụng lớp DEQueue
deque = DEQueue()
deque.at_last(5)
deque.at_last(3)
print("First element:", deque.first())
print("Last element:", deque.last())
deque.at_first(7)
deque.at_first(12)
print("Length:", deque.length())
print("Removed element from the front:", deque.remove_first())
print("Removed element from the rear:", deque.remove_last())
print("Length:", deque.length())
