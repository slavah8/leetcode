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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        dsu = DSU(N)
        groups = defaultdict(list) # groups[root] = list of indices in this component

        for u, v in pairs:
            dsu.union(u, v)
        
        for i in range(N):
            root = dsu.find(i)
            groups[root].append(i)
        
        res = list(s)
        for root, idxs in groups.items():
            idxs.sort()
            chars = sorted(s[i] for i in idxs)
            for i, char in zip(idxs, chars):
                res[i] = char
        return "".join(res)



        