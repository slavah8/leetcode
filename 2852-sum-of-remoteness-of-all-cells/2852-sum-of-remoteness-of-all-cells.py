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
            return False
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        
        return True

class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        components = 0
        rows = len(grid)
        cols = len(grid[0])
        dsu = DSU(rows * cols)
        component_vals = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_sum = 0
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1:
                    continue

                idx = r * cols + c
                total_sum += grid[r][c]

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                        n_idx = nr * cols + nc
                        dsu.union(idx, n_idx)

        root_val = defaultdict(int)
        root_size = defaultdict(int)    
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1:
                    continue
                idx = r * cols + c
                root = dsu.find(idx)
                root_val[root] += grid[r][c]
                root_size[root] += 1

        for root in root_val:
            s = root_val[root]
            size = root_size[root]
            ans += size * (total_sum - s)
        return ans
        



        
        


        
        

        
                        
        
