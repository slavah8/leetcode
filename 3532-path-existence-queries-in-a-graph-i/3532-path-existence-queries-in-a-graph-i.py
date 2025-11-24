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
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        dsu = DSU(n)

        i = 0
        j = i + 1
        while i < n:
            while j < n and abs(nums[i] - nums[j]) <= maxDiff:
                dsu.union(i, j)
                j += 1
            i += 1
        print(dsu.parent)
        ans = []

        for node1, node2 in queries:
            root_u, root_v = dsu.find(node1), dsu.find(node2)
            if root_u == root_v:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans

