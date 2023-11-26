class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        # Kiểm tra xem các đỉnh v và w có trong danh sách đỉnh không
        if v not in self.adjacency_list or w not in self.adjacency_list:
            raise ValueError("Đỉnh không tồn tại trong đồ thị.")

        # Thêm cạnh vào danh sách kề của đỉnh v
        self.adjacency_list[v].append(w)
        # Thêm cạnh vào danh sách kề của đỉnh w
        self.adjacency_list[w].append(v)

# Tạo đồ thị G và subgraph H
graph_G = Graph(7)
graph_G.add_edge(0, 1)
graph_G.add_edge(1, 2)
graph_G.add_edge(2, 3)
graph_G.add_edge(3, 0)
graph_G.add_edge(0, 4)
graph_G.add_edge(5, 6)

subgraph_H = Graph(4)
subgraph_H.add_edge(0, 1)
subgraph_H.add_edge(1, 3)
subgraph_H.add_edge(2, 3)
subgraph_H.add_edge(3, 0)
