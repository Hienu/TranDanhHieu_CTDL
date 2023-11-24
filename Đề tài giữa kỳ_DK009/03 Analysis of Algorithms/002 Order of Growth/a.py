# Ví dụ đơn giản về các thuật toán và thứ tự tăng ứng với kích thước đầu vào.

algorithms = ["Algorithm_A", "Algorithm_B", "Algorithm_C"]
order_of_growth = ["O(1)", "O(log N)", "O(N^2)"]

# Tạo bảng xếp hạng
ranking_table = {algo: order for algo, order in zip(algorithms, order_of_growth)}

print("Ranking Table:")
for algo, order in ranking_table.items():
    print(f"{algo}: {order}")
