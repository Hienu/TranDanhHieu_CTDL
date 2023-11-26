def recursive_insert(root, e):
    if root is None:
        return Node(e)
    else:
        if e < root.val:
            root.left = recursive_insert(root.left, e)
        else:
            root.right = recursive_insert(root.right, e)
    return root

def recursive_insert(root, e):
    if root is None:
        return Node(e)
    else:
        if e < root.val:
            root.left = recursive_insert(root.left, e)
        else:
            root.right = recursive_insert(root.right, e)
    return root

root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = recursive_insert(root, key)
