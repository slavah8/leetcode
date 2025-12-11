class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        for r in range(rows):
            for c in range(cols):
                h = grid[r][c]
                if h > 0:
                    area += 2

                    area += 4 * h

                    if r > 0:
                        area -= 2 * min(h, grid[r - 1][c])
                    
                    if c > 0:
                        area -= 2 * min(h, grid[r][c - 1])
        return area
                