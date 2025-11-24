class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
        self.comp_sum = [0] * n

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
        self.comp_sum[root_a] += self.comp_sum[root_b]
        

        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return root_a
        
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        dsu = DSU(n)
        active = [False] * n
        ans = [0] * n       

        max_sum = 0

        for i in range(n - 1, -1, -1):
            ans[i] = max_sum
            idx = removeQueries[i]
            active[idx] = True

            dsu.comp_sum[idx] = nums[idx]
            root = idx
            if idx + 1 < n and active[idx + 1]:
                root = dsu.union(idx, idx + 1)
            if idx - 1 >= 0 and active[idx - 1]:
                root = dsu.union(idx, idx - 1)
            
            max_sum = max(max_sum, dsu.comp_sum[root])
        return ans


