# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(1, N + 1)]
        self.rank = [1] * (N + 1)
    
    def find(x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False # cycle
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1

class Solution:
    def numberOfCategories(self, N: int, categoryHandler: Optional['CategoryHandler']) -> int:
        
        dsu = DSU(N)
        print(categoryHandler.haveSameCategory(3, 3))
        categories = 1
        reps = []
    
        for i in range(N):
            matched = False
            for r in reps:
                if categoryHandler.haveSameCategory(i, r):
                    matched = True
                    break
            if not matched:
                reps.append(i)
    
        return len(reps)
                


