# Mối quan hệ đệ quy: t(n) = t(n-1) + n
def recursive_relation(n):
    if n == 0:
        return 0
    else:
        return recursive_relation(n-1) + n
