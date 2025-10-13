class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        INF = 10 ** 10
        # dp[r][j] defined as min cost to get to rth row and jth col
        # val = grid[r - 1][c]
        # dp[r][j] = dp[r - 1][c] + moveCost[val][c] + val
        dp = [[INF] * cols for _ in range(rows)]

        for j in range(cols):
            dp[0][j] = grid[0][j]

        for r in range(1, rows):
            for j in range(cols):
                dest_val = grid[r][j]
                best = INF
                for c in range(cols):
                    src_val = grid[r - 1][c]
                    best = min(best, dp[r - 1][c] + moveCost[src_val][j])
                dp[r][j] = best + dest_val
        
        return min(dp[rows - 1])
            

                





