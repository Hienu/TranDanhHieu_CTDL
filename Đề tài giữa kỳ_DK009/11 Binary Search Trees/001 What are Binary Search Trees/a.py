class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

# BST is inherently a binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert operation preserving BST properties
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
# Create a sample BST
bst = BST()
keys = [5, 3, 8, 1, 4, 7, 9]
for key in keys:
    bst.root = insert(bst.root, key)

# Create a sample BST
bst = BST()
keys = [5, 3, 8, 1, 4, 7, 9]
for key in keys:
    bst.root = insert(bst.root, key)

def isBST(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if not (min_val <= node.key <= max_val):
        return False

    return (isBST(node.left, min_val, node.key - 1) and
            isBST(node.right, node.key + 1, max_val))

# Binary Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Non-BST Binary Tree
root = Node(5)
root.left = Node(3)
root.right = Node(8)

# Ensure no duplicate keys
def insert_no_duplicates(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root  # Avoid duplicates
        elif root.key < key:
            root.right = insert_no_duplicates(root.right, key)
        else:
            root.left = insert_no_duplicates(root.left, key)
    return root

def insert_and_order(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root  # Avoid duplicates
        elif root.key < key:
            root.right = insert_and_order(root.right, key)
        else:
            root.left = insert_and_order(root.left, key)
    return root

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.key)
        in_order_traversal(node.right)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
