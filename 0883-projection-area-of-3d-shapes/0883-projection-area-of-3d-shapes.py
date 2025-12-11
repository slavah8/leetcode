class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        top = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    top += 1
        
        # side view xz

        side = 0
        for row in grid:
            maxx = max(row)
            side += maxx
            print(row)
        
        front = 0
        # max at each column
        for c in range(cols):
            maxx = 0
            for r in range(rows):
                x = grid[r][c]
                if x > maxx:
                    maxx = x
            front += maxx
        
        return front + top + side


