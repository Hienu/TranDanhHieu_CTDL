# Code example for discussing cycles in a graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

    def has_cycle(self):
        visited = [False] * self.vertices
        for vertex in range(self.vertices):
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, -1):
                    return True
        return False

    def is_cyclic_util(self, vertex, visited, parent):
        visited[vertex] = True
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, vertex):
                    return True
            elif parent != neighbor:
                return True
        return False

# Check if the weighted undirected graph has a cycle
has_cycle = weighted_graph.has_cycle()
print(f"Does the weighted graph have a cycle? {has_cycle}")
