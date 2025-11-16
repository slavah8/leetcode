class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # sort by the limit
        # gradually keep adding edges to the DSU as the limit increases

        edgeList = sorted(edgeList, key = lambda e: e[2])

        indexed = []
        for i, (p, q, limit) in enumerate(queries):
            indexed.append((limit, p, q, i))
        indexed.sort(key = lambda x: x[0])
        dsu = DSU(n)

        m = len(edgeList)
        i = 0 # index in edgeList
        answer = [False] * len(queries)
        for limit, p, q, idx in indexed:

            while i < m and edgeList[i][2] < limit:
                u, v, dis = edgeList[i]
                dsu.union(u, v)
                i += 1
            
            if dsu.find(p) == dsu.find(q):
                answer[idx] = True
            
        return answer



         