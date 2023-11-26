# Ví dụ về thao tác cơ bản trên ngăn xếp
stack = []
stack.append(1)  # push
top_element = stack.pop()  # pop
is_empty = len(stack) == 0  # isEmpty

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

class LinkedStack:
    # ... (như trên)
    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if not self.top:
            return None
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def top(self):
        return self.top.data if self.top else None

stack = LinkedStack()
stack.push(5)
stack.push(3)

print(len(stack))        # Output: 2
stack.display()          # Output: 3 -> 5

popped_element = stack.pop()
print(popped_element)    # Output: 3

print(stack.isEmpty())   # Output: False
stack.display()          # Output: 5

top_element = stack.top()
print(top_element)       # Output: 5
