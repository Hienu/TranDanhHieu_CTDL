# Example code for discussing indegree and outdegree in a directed graph
class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = 0
        self.indegree = {v: 0 for v in range(vertices)}
        self.outdegree = {v: 0 for v in range(vertices)}

    def add_edge(self, v, w):
        self.outdegree[v] += 1
        self.indegree[w] += 1
        self.edges += 1

    def vertex_indegree_outdegree(self, vertex):
        return self.indegree[vertex], self.outdegree[vertex]

# Create a directed graph
directed_graph = DirectedGraph(4)
directed_graph.add_edge(0, 1)
directed_graph.add_edge(0, 3)
directed_graph.add_edge(1, 2)
directed_graph.add_edge(2, 3)

# Discuss indegree and outdegree for vertex 0
indegree_of_0, outdegree_of_0 = directed_graph.vertex_indegree_outdegree(0)
print(f"The indegree of vertex 0 is: {indegree_of_0}")
print(f"The outdegree of vertex 0 is: {outdegree_of_0}")
