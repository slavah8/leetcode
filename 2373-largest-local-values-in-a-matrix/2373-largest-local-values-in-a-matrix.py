class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        
        def get_largest(r0, c0):
            start_r = r0 - 1
            start_c = c0 - 1
            maxx = 0
            for r in range(start_r, start_r + 3):
                for c in range(start_c, start_c + 3):
                    val = grid[r][c]
                    if val > maxx:
                        maxx = val
            
            return maxx
        
        
        rows = len(grid)
        cols = len(grid[0])
        maxLocal = [[0] * (cols - 2) for _ in range(rows - 2)]

        for r in range(rows - 2):
            for c in range(cols - 2):
                r0 = r + 1
                c0 = c + 1
                x = get_largest(r0, c0)
                maxLocal[r][c] = x
        
        return maxLocal




