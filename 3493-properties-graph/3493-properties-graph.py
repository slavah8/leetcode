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
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        dsu = DSU(n)
        def intersect(a, b):
            count = 0
            nums = a + b
            set_nums = set(nums)
            list_nums = list(set_nums)
            
            for x in list_nums:
                if x in a and x in b:
                    count += 1
            return count
        
        n = len(properties)
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    print(i, j)
                    dsu.union(i, j)
        
        
        roots = set()
        for node in range(n):
            root = dsu.find(node)
            roots.add(root)
        print(roots)
        return len(roots)


        