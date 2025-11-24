class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        dsu = DSU(m * n)
        is_land = [False] * (m * n)
        ans = []
        count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r, c in positions:
            idx = r * n + c
            if is_land[idx]:
                ans.append(count)
                continue
            
            is_land[idx] = True
            count += 1

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n:
                    n_idx = nr * n + nc
                    if is_land[n_idx]:

                        if dsu.union(idx, n_idx):
                            count -= 1
            
            ans.append(count)
        return ans

            

            



