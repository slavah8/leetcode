class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True
    
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # KRUSKAL'S ALGORITHM

        total = 0
        dsu = DSU(n)
        connections = sorted(connections, key = lambda edge: edge[2])
        print(connections)
        edges = 0
        for u, v, cost in connections:
            if dsu.union(u, v):
                total += cost
                edges += 1
                if edges == n - 1:
                    return total

        return -1
        
        
