class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        OFFSET = 10001
        dsu = DSU(OFFSET * 2)

        for r, c in stones:
            dsu.union(r, c + OFFSET)
        
        seen = set()
        for r, c in stones:
            seen.add(dsu.find(r))
            seen.add(dsu.find(c + OFFSET))
        
        components = len(seen)
        return len(stones) - components
        

