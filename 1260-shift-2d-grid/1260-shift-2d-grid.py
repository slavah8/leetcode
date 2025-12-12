class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        if k == 0:
            return grid
        for _ in range(k):
            new_grid = [[0] * cols for _ in range(rows)]
            for r in range(rows):
                for c in range(cols):
                    val = grid[r][c]

                    if r == rows - 1 and c == cols - 1:
                        new_grid[0][0] = val
                        continue

                    if c == cols - 1:
                        new_grid[r + 1][0] = val
                        continue
                    
                    new_grid[r][c + 1] = val

            grid = new_grid

        return new_grid 
                
                