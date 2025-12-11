class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        new_grid = [[0] * cols for _ in range(rows)]
        max_rows = [0] * rows
        max_cols = [0] * cols
        for r in range(rows):
            for c in range(cols):
                max_rows[r] = max(max_rows[r], grid[r][c])
                max_cols[c] = max(max_cols[c], grid[r][c])
        
        print(max_rows)
        print(max_cols)

        for r in range(rows):
            for c in range(cols):
                new_grid[r][c] = min(max_rows[r], max_cols[c])

        print(new_grid)
        diff = 0
        for r in range(rows):
            for c in range(cols):
                diff += (new_grid[r][c] - grid[r][c])
        
        return diff

