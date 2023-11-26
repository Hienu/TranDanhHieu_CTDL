# Code example for discussing paths and cycles in a graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

# Create a weighted undirected graph
weighted_graph = Graph(5)
weighted_graph.add_edge(0, 1)
weighted_graph.add_edge(1, 2)
weighted_graph.add_edge(2, 3)
weighted_graph.add_edge(3, 0)
weighted_graph.add_edge(0, 4)

# Create a directed graph
directed_graph = Graph(4)
directed_graph.add_edge(0, 1)
directed_graph.add_edge(1, 2)
directed_graph.add_edge(2, 3)
directed_graph.add_edge(3, 0)

# Code example for discussing paths in a graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        for neighbor in self.adjacency_list[start]:
            if neighbor not in path:
                new_path = self.find_path(neighbor, end, path)
                if new_path:
                    return new_path
        return None

# Find a path from vertex 0 to vertex 3 in the weighted undirected graph
path_in_weighted_graph = weighted_graph.find_path(0, 3)
print(f"Path in weighted graph: {path_in_weighted_graph}")
