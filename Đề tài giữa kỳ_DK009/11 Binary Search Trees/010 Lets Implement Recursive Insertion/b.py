class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def recursive_insert(self, t_root, e):
        if t_root:
            if e < t_root.element:
                t_root.left = self.recursive_insert(t_root.left, e)
            elif e > t_root.element:
                t_root.right = self.recursive_insert(t_root.right, e)
            return t_root
        else:
            return Node(e)

# Tạo cây tìm kiếm nhị phân
b = BinarySearchTree()
b.root = b.recursive_insert(b.root, 50)
b.recursive_insert(b.root, 30)
b.recursive_insert(b.root, 80)
b.recursive_insert(b.root, 10)
b.recursive_insert(b.root, 40)
b.recursive_insert(b.root, 60)
b.recursive_insert(b.root, 90)

# Hiển thị kết quả bằng phương thức in_order
in_order(b.root)
