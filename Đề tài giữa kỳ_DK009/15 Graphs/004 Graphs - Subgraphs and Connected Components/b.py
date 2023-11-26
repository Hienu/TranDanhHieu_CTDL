# Ví dụ về connected components và articulation points
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

# Tạo đồ thị connected và đồ thị với connected components
connected_graph = Graph(5)
connected_graph.add_edge(0, 1)
connected_graph.add_edge(1, 2)
connected_graph.add_edge(2, 3)
connected_graph.add_edge(3, 0)
connected_graph.add_edge(1, 3)

disconnected_graph = Graph(6)
disconnected_graph.add_edge(0, 1)
disconnected_graph.add_edge(1, 2)
disconnected_graph.add_edge(3, 4)
disconnected_graph.add_edge(4, 5)
