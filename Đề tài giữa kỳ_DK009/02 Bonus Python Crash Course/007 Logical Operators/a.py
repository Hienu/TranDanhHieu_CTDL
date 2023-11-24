zero_value = 0
empty_string = ""
non_zero_value = 42
non_empty_string = "Hello"

# Số 0 và chuỗi rỗng được coi là False
print(bool(zero_value))  # Output: False
print(bool(empty_string))  # Output: False

# Các giá trị khác đều là True
print(bool(non_zero_value))  # Output: True
print(bool(non_empty_string))  # Output: True
