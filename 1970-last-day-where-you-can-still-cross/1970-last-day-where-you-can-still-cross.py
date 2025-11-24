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
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        TOP = n
        BOT = n + 1
        dsu = DSU(n + 2)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # keep track of which cells are land as we add them in reverse
        land = [False] * n
        # land initialized to false because we process in reverse
        # start with all water cells and keep adding back land cells

        def cell_id(r: int, c: int) -> int:
            # r, c are 0-based here
            return r * col + c


        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i]
            r -= 1
            c -= 1
            
            idx = cell_id(r, c)
            land[idx] = True

            if r == 0: # connected to top
                dsu.union(idx, TOP)
            
            if r == row - 1:
                dsu.union(idx, BOT)

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < row and 0 <= nc < col:
                    n_idx = cell_id(nr, nc)
                    if land[n_idx]:
                        dsu.union(idx, n_idx)
            
            if dsu.find(TOP) == dsu.find(BOT):
                return i

        return 0




