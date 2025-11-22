class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
    
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        dsu = DSU(n)

        logs = sorted(logs, key = lambda x: x[0])
        print(logs)
        
        for timestamp, x, y in logs:
            dsu.union(x, y)
            if dsu.components == 1:
                return timestamp
        return -1

