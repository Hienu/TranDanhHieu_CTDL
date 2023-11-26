# Ví dụ với Linear Search
def linear_search(arr, key):
    # Trường hợp tốt nhất: Ω(1)
    if arr[0] == key:
        return 0
    
    # Trường hợp xấu nhất: O(N)
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    # Trường hợp trung bình: Θ(N)
    return len(arr) // 2
