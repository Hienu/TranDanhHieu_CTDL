def binary_search_iterative(arr, key):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return -1

arr = [15, 21, 47, 84, 96]
key_1 = 84
key_2 = 17

result_1 = binary_search_iterative(arr, key_1)
result_2 = binary_search_iterative(arr, key_2)

print("Result:", result_1)  # Output: Result: 3
print("Result:", result_2)  # Output: Result: -1
