class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
        self.components = N

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
        self.components -= 1
        return True
class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        dsu = DSU(N)
        
        for u, v in edges:
            dsu.union(u, v)
        return dsu.components

        