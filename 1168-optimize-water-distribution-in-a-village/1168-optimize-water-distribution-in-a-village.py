class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # We’ll have nodes 0..n
        # 0 = virtual node (building a well)
        # 1..n = houses

        
        dsu = DSU(n + 1)
        edges = [] # (cost, u, v)

        for i in range(1, n + 1):
            cost = wells[i - 1]
            edges.append((cost, 0, i))

        for u, v, w in pipes:
            edges.append((w, u, v))
            edges.append((w, v, u))
        
        edges.sort(key = lambda x: x[0])
        min_cost = 0
        for cost, u, v in edges:
            if not dsu.union(u, v):
                continue
            
            min_cost += cost
            if dsu.components == 1:
                return min_cost
        
        
            


        


        
