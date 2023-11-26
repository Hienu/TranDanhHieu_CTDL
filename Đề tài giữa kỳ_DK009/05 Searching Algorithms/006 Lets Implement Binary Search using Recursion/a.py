def binary_search_recursive(a, key, l, r):
    if l > r:
        return -1  # hoặc thông báo không tìm thấy
    mid = (l + r) // 2
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search_recursive(a, key, l, mid - 1)
    else:
        return binary_search_recursive(a, key, mid + 1, r)

a = [15, 21, 47, 84, 96]
found = binary_search_recursive(a, 84, 0, len(a) - 1)
print("Result:", found)
