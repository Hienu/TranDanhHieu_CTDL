# Ví dụ đơn giản về cấu trúc nút trong AVL Tree
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Chiều cao của cây con

# Ví dụ về tính toán balance factor
def balance_factor(node):
    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0
    return left_height - right_height

# Kiểm tra xem một cây có phải là AVL Tree không
def is_avl_tree(root):
    if root is None:
        return True
    bf = balance_factor(root)
    if abs(bf) > 1:
        return False
    return is_avl_tree(root.left) and is_avl_tree(root.right)
