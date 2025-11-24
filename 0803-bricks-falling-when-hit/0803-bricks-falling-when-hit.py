class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
        self.size = [0] * n
    
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
        self.size[root_a] += self.size[root_b]

        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        
        return True

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        

        stable = 0
        roof = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dsu = DSU(rows * cols + 1)
        original = [row[:] for row in grid]

        def cell_id(r, c):
            return r * cols + c + 1

        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                
                idx = r * cols + c + 1
                dsu.size[idx] = 1
                if r == 0: # connected to the top of the grid
                    dsu.union(roof, idx)
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    idx = cell_id(r, c)
                    for dr, dc in directions:
                        nr, nc = dr + r, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            n_idx = nr * cols + nc + 1
                            dsu.union(idx, n_idx)        
        

        def roof_size():
            return dsu.size[dsu.find(roof)]

        res = [0] * len(hits)
        for i in range(len(hits) - 1, -1, -1):
            r,c = hits[i]
            if original[r][c] == 0:
                res[i] = 0
                continue
            
            before = roof_size()
            print(before)
            # add the brick back
            grid[r][c] = 1
            idx = cell_id(r, c)
            dsu.size[idx] += 1
            if r == 0:
                dsu.union(roof, idx)

            
            for dr, dc in directions:
                nr, nc = dr + r, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    n_idx = cell_id(nr, nc)
                    dsu.union(n_idx, idx)
            after = roof_size()
            fallen = after - before - 1
            res[i] = max(0, fallen)
        return res

            






                
