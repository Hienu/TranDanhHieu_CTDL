# Ví dụ về sắp xếp ổn định và không ổn định
data = [(5, 'apple'), (3, 'orange'), (5, 'banana')]

# Sắp xếp ổn định
stable_sorted = sorted(data, key=lambda x: x[0])  
print("Sắp xếp ổn định:", stable_sorted)

# Sắp xếp không ổn định
unstable_sorted = sorted(data, key=lambda x: x[0])  
print("Sắp xếp không ổn định:", unstable_sorted)
