class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        rows = len(grid)
        cols = len(grid[0])

        
        ans = [-1] * cols
        for c in range(cols):
            max_width = 0
            for r in range(rows):
                num = str(grid[r][c])
                max_width = max(max_width, len(num))
            ans[c] = max_width
        return ans
            