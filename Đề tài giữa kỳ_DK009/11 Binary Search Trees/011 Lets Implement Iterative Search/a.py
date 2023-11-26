class BinarySearchTree:
    def __init__(self):
        self.root = None

    def iterative_search(self, key):
        t_root = self.root
        while t_root:
            if key == t_root.element:
                return True
            elif key < t_root.element:
                t_root = t_root.left
            else:
                t_root = t_root.right
        return False

# Tạo cây tìm kiếm nhị phân
b = BinarySearchTree()
b.root = b.recursive_insert(b.root, 50)
b.recursive_insert(b.root, 30)
b.recursive_insert(b.root, 80)
b.recursive_insert(b.root, 10)
b.recursive_insert(b.root, 40)
b.recursive_insert(b.root, 60)
b.recursive_insert(b.root, 90)

# Tìm kiếm và hiển thị kết quả
print(b.iterative_search(60))  # True
print(b.iterative_search(30))  # True
print(b.iterative_search(70))  # False
