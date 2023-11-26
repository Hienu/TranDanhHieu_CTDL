class Graph:
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

simple_graph = Graph(4)
simple_graph.add_edge(0, 1)
simple_graph.add_edge(0, 3)
simple_graph.add_edge(1, 2)

degree_of_vertex_0 = simple_graph.vertex_degree(0)
print(f"The degree of vertex 0 is: {degree_of_vertex_0}")
