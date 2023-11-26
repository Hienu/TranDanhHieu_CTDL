class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None

# Tiếp tục từ đoạn mã trước
stack_linked = StackLinkedList()

# Kiểm tra ngăn xếp có rỗng hay không
is_empty = stack_linked.is_empty()  # Output: True

# Thêm phần tử vào ngăn xếp
stack_linked.push(5)
stack_linked.push(7)

# Lấy ra phần tử đầu tiên từ ngăn xếp
top_element = stack_linked.pop()  # Output: 7
