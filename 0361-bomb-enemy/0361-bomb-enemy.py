class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        row_hits = 0
        col_hits = [0] * cols
        best = 0
        for r in range(rows):
            for c in range(cols):
                
                # recompute row hits
                if c == 0 or grid[r][c - 1] == 'W':
                    row_hits = 0
                    k = c
                    while k < cols and grid[r][k] != 'W':
                        if grid[r][k] == 'E':
                            row_hits += 1
                        k += 1
                
                # recompute col hits
                if r == 0 or grid[r - 1][c] == 'W':
                    col_hits[c] = 0
                    k = r
                    while k < rows and grid[k][c] != 'W':
                        if grid[k][c] == 'E':
                            col_hits[c] += 1
                        k += 1

                if grid[r][c] == '0':
                    best = max(best, row_hits + col_hits[c])
        return best
                

