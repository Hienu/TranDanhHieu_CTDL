def binary_iterative(A, N, key):
    L, R = 0, N - 1
    while L <= R:
        M = (L + R) // 2
        if key == A[M]:
            return M
        elif key < A[M]:
            R = M - 1
        else:
            L = M + 1
    return -1
