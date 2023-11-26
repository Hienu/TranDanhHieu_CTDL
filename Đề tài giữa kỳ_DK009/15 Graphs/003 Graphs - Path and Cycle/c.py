# Code example for discussing Directed Acyclic Graph (DAG)
class DirectedAcyclicGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

# Create a directed acyclic graph
dag = DirectedAcyclicGraph(5)
dag.add_edge(0, 1)
dag.add_edge(1, 2)
dag.add_edge(2, 3)
dag.add_edge(3, 4)
