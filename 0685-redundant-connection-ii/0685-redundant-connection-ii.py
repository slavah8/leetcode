class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]
        self.rank = [0] * (N + 1)
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False # cycle
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True
    

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        N = len(edges)

        parent_of = [0] * (N + 1)

        candA = candB = None

        for i, (u, v) in enumerate(edges):
            if parent_of[v] == 0:
                parent_of[v] = u
            else:
                # 2 parents record the two candidates
                candA = [parent_of[v], v]
                candB = [u, v]

                edges[i][1] = 0 #  # turn [u, v] into [u, 0]
                break
        
        dsu = DSU(N)

        for u, v in edges:
            if v == 0:
                continue # skip invalidated candB
            if not dsu.union(u, v): # found cycle even with invalidated candB so has to be candA
                # if its not the 2 parent case then the current edge forms the cycle
                if candA is None:
                    return [u, v]
                
                # else return candA
                return candA
        
        # if no cycle found with candB invalidated, it means it was the culprit
        return candB

