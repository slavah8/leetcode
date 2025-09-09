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
        roota, rootb = self.find(a), self.find(b)
        if roota == rootb:
            return
        
        if self.rank[roota] < self.rank[rootb]:
            roota, rootb = rootb, roota
        self.parent[rootb] = roota

        if self.rank[roota] == self.rank[rootb]:
            self.rank[roota] += 1

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        INF = 10 ** 10
        N = len(source)
        dsu = DSU(N)
        groups = collections.defaultdict(list)
        for u, v in allowedSwaps:
            dsu.union(u, v)
        
        for i in range(N):
            root = dsu.find(i)
            groups[root].append(i)
        
        hamming = 0
            
        for idxs in groups.values():
            count = collections.Counter(source[i] for i in idxs)
            for i in idxs:
                val = target[i]
                if count[val] > 0:
                    count[val] -= 1
                else:
                    hamming += 1

        return hamming
    
            


            
        