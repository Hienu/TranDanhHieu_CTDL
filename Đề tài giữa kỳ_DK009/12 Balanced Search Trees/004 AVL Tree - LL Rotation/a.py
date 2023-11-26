class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Quá trình xoay và cân bằng
def rotate_and_balance(node_a, node_b, node_c):
    # Quá trình xoay
    node_b.left = node_c
    node_a.right = node_b

    # Cập nhật chỉ số cân bằng

# Ví dụ về cây tìm kiếm nhị phân
root = Node(30)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(15)
root.left.right = Node(25)
root.right.right = Node(60)

# Chèn phần tử mới và cân bằng cây
new_element = Node(10)
# Cập nhật cây và chỉ số cân bằng sau khi chèn phần tử mới

# Hiển thị cây tìm kiếm nhị phân cân bằng (AVL)
