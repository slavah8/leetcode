class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        rows = len(grid)
        cols = len(grid[0])
        # mx[i][j] = maximum product achievable upon reaching cell (i, j)
        mx = [[None] * cols for _ in range(rows)]
        # mn[i][j] = minimum product achievable upon reaching cell (i, j).
        mn = [[None] * cols for _ in range(rows)]


        mx[0][0] = grid[0][0]
        mn[0][0] = grid[0][0]
        # we can only come up or from left

        # for first row
        for j in range(1, cols):
            if mx[0][j - 1] is not None:
                v = grid[0][j] 
                if v >= 0:
                    mx[0][j] = mx[0][j - 1] * v
                    mn[0][j] = mn[0][j - 1] * v
                else:
                    mx[0][j] = mn[0][j - 1] * v
                    mn[0][j] = mx[0][j - 1] * v
        # for first col
        for i in range(1, rows):
            if mx[i - 1][0] is not None:
                v = grid[i][0]
                if v >= 0:
                    mx[i][0] = mx[i - 1][0] * v
                    mn[i][0] = mn[i - 1][0] * v
                else:
                    mx[i][0] = mn[i - 1][0] * v
                    mn[i][0] = mx[i - 1][0] * v

        # rest
        for i in range(1, rows):
            for j in range(1, cols):
                v = grid[i][j]
                cands = []
                if mx[i - 1][j] is not None:
                    cands.append((mx[i - 1][j], mn[i - 1][j]))
                if mx[i][j - 1] is not None:
                    cands.append((mx[i][j - 1], mn[i][j - 1]))
                if not cands:
                    continue
                
                if v >= 0: # positive
                    mx[i][j] = max(x for x, _ in cands) * v
                    mn[i][j] = min(y for _, y in cands) * v
                else: # negative
                    mx[i][j] = min(y for _, y in cands) * v
                    mn[i][j] = max(x for x, _ in cands) * v

        best = mx[rows - 1][cols - 1]
        if best is None or best < 0:
            return - 1
        return best % MOD
                

                
    





