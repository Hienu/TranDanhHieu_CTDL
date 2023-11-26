# Ví dụ về strongly connected graph
class StronglyConnectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

# Tạo strongly connected graph
strongly_connected_graph = StronglyConnectedGraph(5)
strongly_connected_graph.add_edge(0, 1)
strongly_connected_graph.add_edge(1, 2)
strongly_connected_graph.add_edge(2, 3)
strongly_connected_graph.add_edge(3, 4)
strongly_connected_graph.add_edge(4, 0)
