# Example code for computing vertex degree in an undirected graph
class UndirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = 0
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)
        self.adjacency_list[w].append(v)
        self.edges += 1

    def vertex_degree(self, vertex):
        return len(self.adjacency_list[vertex])

# Create an undirected graph
undirected_graph = UndirectedGraph(5)
undirected_graph.add_edge(0, 1)
undirected_graph.add_edge(0, 2)
undirected_graph.add_edge(1, 3)
undirected_graph.add_edge(2, 4)

# Compute the degree of vertex 0
degree_of_vertex_0 = undirected_graph.vertex_degree(0)
print(f"The degree of vertex 0 is: {degree_of_vertex_0}")
