class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        pairs = 0
        for row in grid:
            
            for c in range(cols):
                cur_col = []
                for r in range(rows):
                    cur_col.append(grid[r][c])
            
                if cur_col == row:
                    pairs += 1
        
        return pairs
