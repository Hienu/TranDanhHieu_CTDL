def binary_recursive(a, key, l, r):
    if l > r:
        return -1  # hoặc thông báo không tìm thấy
    
    m = (l + r) // 2
    
    if key == a[m]:
        return m
    elif key < a[m]:
        return binary_recursive(a, key, l, m - 1)
    else:
        return binary_recursive(a, key, m + 1, r)
