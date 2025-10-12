class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)

        # dp[i][j] defined as min sum to grid [i][j]
        # original problem min (dp[N - 1][i] for i in range(N))

        INF = 10 ** 10

        dp = [[INF] * N for _ in range(N)]
        for i in range(N):
            dp[0][i] = matrix[0][i]


        for i in range(1, N):
            for j in range(N):

                up = dp[i - 1][j]
                left_diag = dp[i - 1][j - 1] if j - 1 >= 0 else INF
                right_diag = dp[i - 1][j + 1] if j + 1 < N else INF
                dp[i][j] = matrix[i][j] + min(up, left_diag, right_diag)
        
        ans = INF
        for i in range(N):
            ans = min(ans, dp[N - 1][i])
        return ans