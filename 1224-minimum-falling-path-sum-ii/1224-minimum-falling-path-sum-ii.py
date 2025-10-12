class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        INF = 10 ** 10
        # min non zero shift falling path up to ith row and j column
        # relate dp[i][j] = min (dp[i - 1][j] for all j != j)
        dp = [[INF] * N for _ in range(N)]

        for i in range(N):
            dp[0][i] = grid[0][i]
        
        for i in range(1, N):
            for j in range(N):
                best = INF
                for k in range(N):
                    if k != j:
                        best = min(best, dp[i - 1][k])
                dp[i][j] = best + grid[i][j]
        minn = INF
        
        for i in range(N):
            minn = min(minn, dp[N - 1][i])         
        return minn 
