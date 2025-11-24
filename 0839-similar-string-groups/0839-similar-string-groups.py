class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
        
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return root_a
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a

        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return root_a

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        n = len(strs[0])
        def similar(a, b):
            k = 0
            diff = 0
            while k < n:
                if a[k] != b[k]:
                    diff += 1
                    if diff > 2:
                        return False
                k += 1
            if diff == 0 or diff == 2:
                return True
            return False
        
        
        m = len(strs)
        dsu = DSU(m)
        for i in range(m):
            for j in range(i + 1, m):
                if similar(strs[i], strs[j]):
                    dsu.union(i, j)
        print(dsu.parent)
        count = 0
        
        roots = set()
        for i in range(m):
            roots.add(dsu.find(i))
        return len(roots)
