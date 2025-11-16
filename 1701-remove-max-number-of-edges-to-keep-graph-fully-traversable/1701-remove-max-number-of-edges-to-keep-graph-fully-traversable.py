class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
        self.connected_components = n
    
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
        self.connected_components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        num_edges = len(edges)
        edges = sorted(edges, key = lambda edge: edge[0], reverse = True)
        print(edges)
        dsu1 = DSU(n) # alice
        dsu2 = DSU(n) # bob

        removed = 0

        for t, u, v in edges:
            if t == 3:
                merged_a = dsu1.union(u, v)
                merged_b = dsu2.union(u, v)
                if not merged_a and not merged_b:
                    removed += 1
        
        # alice
        for t, u, v in edges:
            if t == 1:
                merged_a = dsu1.union(u, v)
                if not merged_a:
                    removed += 1
        
        # bob
        for t, u, v in edges:
            if t == 2:
                merged_b = dsu2.union(u, v)
                if not merged_b:
                    removed += 1
        
        if dsu1.connected_components == 1 and dsu2.connected_components == 1:
            return removed
        return -1
        
            
