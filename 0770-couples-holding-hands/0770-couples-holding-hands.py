class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a # always make root_a the larger tree 

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:

        # couples in the same connected component are intertangled and need changing
        # couples in different components dont affect each other

        N = len(row) // 2
        dsu = DSU(N)

        for i in range(N):
            a, b = row[2 * i], row[2 * i + 1]
            dsu.union(a // 2, b // 2)
        
        comp_size = {}
        for couple_id in range(N):
            root = dsu.find(couple_id)
            comp_size[root] = comp_size.get(root, 0) + 1

        swaps = 0
        for size in comp_size.values():
            swaps += size - 1
        
        return swaps


        