class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Ví dụ về BST
#      5
#     / \
#    3   8
#   /|   |\
#  1 4   6 9
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(9)

# Hàm tìm kiếm trong BST
def search(root, key):
    # Trường hợp cơ bản: nếu cây rỗng hoặc phần tử đang tìm nằm ở gốc
    if root is None or root.val == key:
        return root
    
    # Nếu phần tử cần tìm nhỏ hơn gốc, thực hiện tìm kiếm trong cây con bên trái
    if root.val > key:
        return search(root.left, key)

    # Nếu phần tử cần tìm lớn hơn gốc, thực hiện tìm kiếm trong cây con bên phải
    return search(root.right, key)

# Hàm tìm kiếm có logic
def search_recursive(root, key):
    # Trường hợp cơ bản: nếu cây rỗng hoặc phần tử đang tìm nằm ở gốc
    if root is None or root.val == key:
        return root
    
    # Nếu phần tử cần tìm nhỏ hơn gốc, thực hiện tìm kiếm trong cây con bên trái
    if root.val > key:
        return search_recursive(root.left, key)

    # Nếu phần tử cần tìm lớn hơn gốc, thực hiện tìm kiếm trong cây con bên phải
    return search_recursive(root.right, key)

# Gọi hàm tìm kiếm
result = search(root, 6)

# Kiểm tra kết quả
if result:
    print(f"Element 6 found in the BST.")
else:
    print(f"Element 6 not found in the BST.")
