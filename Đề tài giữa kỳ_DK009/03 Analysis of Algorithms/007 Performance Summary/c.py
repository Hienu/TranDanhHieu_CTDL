# Ví dụ với Big Theta
def example_big_theta_best_worst_case(input_list):
    median_value = sorted(input_list)[len(input_list)//2]  # Θ(N log N)
    return median_value
