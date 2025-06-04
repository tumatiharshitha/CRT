class Graph:
    def __init__(self):
        self.graph = {}  
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        print("Adjacency List")
        for i in self.graph:
            print(f"{i} --> {self.graph[i]}")

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.display()

def create_adjacency_matrix(vertices, edges):
    matrix = [[0] * vertices for _ in range(vertices)]

    for (u, v) in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  

    return matrix

def print_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))


V = 7


edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (3, 6),
    (4, 5),
    (5, 6)
]

adj_matrix = create_adjacency_matrix(V, edges)
print_matrix(adj_matrix)
