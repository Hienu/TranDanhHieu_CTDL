# Định nghĩa hàm create_graph()
def create_graph():
    # Thực hiện logic để tạo đồ thị
    # Ví dụ:
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }
    return graph

# Sử dụng hàm create_graph()
graph = create_graph()

# Tiếp tục với các phần khác của mã của bạn

# Code ví dụ: Thuật toán duyệt đồ thị
def graph_traversal(graph, start_vertex):
    # Thực hiện duyệt đồ thị từ đỉnh khởi đầu
    pass

# Code ví dụ: Ứng dụng của duyệt đồ thị
def check_strongly_connected(graph):
    # Kiểm tra xem đồ thị có kết nối mạnh không
    pass

# Code ví dụ: Thuật toán Duyệt Đồ Thị - BFS và DFS
def breadth_first_search(graph, start_vertex):
    # Thuật toán duyệt đồ thị theo chiều rộng
    pass

def depth_first_search(graph, start_vertex):
    # Thuật toán duyệt đồ thị theo chiều sâu
    pass
