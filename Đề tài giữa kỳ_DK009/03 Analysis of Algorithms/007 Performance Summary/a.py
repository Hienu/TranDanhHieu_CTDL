# Ví dụ với Big O
def example_big_o(input_list):
    max_value = max(input_list)  # O(N)
    return max_value

# Ví dụ với Big Omega
def example_big_omega(input_list):
    min_value = min(input_list)  # Ω(N)
    return min_value

# Ví dụ với Big Theta
def example_big_theta(input_list):
    average_value = sum(input_list) / len(input_list)  # Θ(N)
    return average_value
