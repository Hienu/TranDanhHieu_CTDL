class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Sử dụng
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert(root, key)

# Chèn phần tử 35 vào cây
root = insert(root, 35)

def iterative_insert(root, key):
    new_node = Node(key)
    if root is None:
        return new_node

    temp = None
    current = root
    while current:
        temp = current
        if key < current.val:
            current = current.left
        elif key > current.val:
            current = current.right
        else:
            # Node đã tồn tại, không chèn lại
            return root

    if key < temp.val:
        temp.left = new_node
    else:
        temp.right = new_node

    return root

# Sử dụng
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = iterative_insert(root, key)

def iterative_insert(root, key):
    new_node = Node(key)
    if root is None:
        return new_node

    temp = None
    current = root
    while current:
        temp = current
        if key < current.val:
            current = current.left
        elif key > current.val:
            current = current.right
        else:
            # Node đã tồn tại, không chèn lại
            return root

    if key < temp.val:
        temp.left = new_node
    else:
        temp.right = new_node

    return root

# Sử dụng
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = iterative_insert(root, key)
