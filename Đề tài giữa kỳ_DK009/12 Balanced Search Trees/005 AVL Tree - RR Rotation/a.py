# Đoạn mã ví dụ
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Tạo cây nhị phân
root = Node("A")
root.right = Node("B")
root.left = Node("L")
root.right.right = Node("C")
root.right.left = Node("b L")

# Đoạn mã ví dụ
def RR_rotation(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    return new_root
