class NetworkGraph:
    def __init__(self):
        self.adj = {}

    def add_connection(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append(v)
        self.adj[v].append(u)

    def is_connected(self, start, target):
        if start not in self.adj or target not in self.adj:
            return False

        alrvisited = set()
        return self.dfs(start, target, alrvisited)

    def dfs(self, current, target, alrvisited):
        if current == target:
            return True

        alrvisited.add(current)

        for neighborpc in self.adj[current]:
            if neighborpc not in alrvisited:
                if self.dfs(neighborpc, target, alrvisited):
                    return True

        return False

network = NetworkGraph()

network.add_connection("PC1", "PC2")
network.add_connection("PC2", "PC3")
network.add_connection("PC3", "PC4")

print(network.is_connected("PC1", "PC4"))
print(network.is_connected("PC1", "PC5"))


