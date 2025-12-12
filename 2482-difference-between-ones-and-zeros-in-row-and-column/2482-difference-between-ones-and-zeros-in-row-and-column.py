class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        rows = len(grid)
        cols = len(grid[0])
        ones_row = [0] * rows
        ones_col = [0] * cols

        zeros_row = [0] * rows
        zeros_col = [0] * cols

        for r in range(rows):
            for c in range(cols):
                x = grid[r][c]

                if x == 1:
                    ones_row[r] += 1
                    ones_col[c] += 1
                else:
                    zeros_row[r] += 1
                    zeros_col[c] += 1
        
        diff = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                diff[r][c] = ones_row[r] + ones_col[c] - zeros_row[r] - zeros_col[c]
        
        return diff
