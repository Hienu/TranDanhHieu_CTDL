# Ví dụ về biconnected components
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

# Tạo đồ thị với biconnected components
biconnected_graph = Graph(5)
biconnected_graph.add_edge(0, 1)
biconnected_graph.add_edge(1, 2)
biconnected_graph.add_edge(2, 3)
biconnected_graph.add_edge(3, 0)
biconnected_graph.add_edge(2, 4)
biconnected_graph.add_edge(4, 0)
