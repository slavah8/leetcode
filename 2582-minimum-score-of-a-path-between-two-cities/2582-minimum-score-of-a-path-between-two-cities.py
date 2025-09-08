class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]
        self.rank = [0] * (N + 1)

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
    def minScore(self, N: int, roads: List[List[int]]) -> int:
        # find min edge in the connected component that contains node 1 and node n

        dsu = DSU(N)
        for (u, v, cost) in roads:
            dsu.union(u, v)

        print(dsu.parent)

        node1 = dsu.find(1)
        INF = 10 ** 10
        minn = INF
        
        for (u, v, cost) in roads:
            if dsu.find(u) == node1:
                minn = min(minn, cost)
        
        return minn



        