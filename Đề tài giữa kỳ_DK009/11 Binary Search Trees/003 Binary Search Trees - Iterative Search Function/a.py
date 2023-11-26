class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tạo một cây BST đơn giản để kiểm thử
#         5
#        / \
#       3   8
#      / \ / \
#     1  4 7  9
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(1), TreeNode(4))
root.right = TreeNode(8, TreeNode(7), TreeNode(9))

# Hàm tìm kiếm trong BST
def iterative_search(t_root, key):
    while t_root:
        if key == t_root.val:
            return True
        elif key < t_root.val:
            t_root = t_root.left
        else:
            t_root = t_root.right
    return False

# Ví dụ về tìm kiếm trong BST
result = iterative_search(root, 6)

# Kiểm tra kết quả
if result:
    print(f"Element 6 found in the BST.")
else:
    print(f"Element 6 not found in the BST.")
