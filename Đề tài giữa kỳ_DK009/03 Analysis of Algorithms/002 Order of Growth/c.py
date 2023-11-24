import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu cho biểu đồ
input_size = np.arange(1, 10)
time_complexity = input_size ** 2

# Vẽ biểu đồ
plt.plot(input_size, time_complexity, label='O(N^2)')
plt.xlabel('Input Size')
plt.ylabel('Time Complexity')
plt.title('Order of Growth Chart')
plt.legend()
plt.show()
