class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        M = len(matrix)
        N = len(matrix[0])

        # dp[i][j] = side length of largest square ending at (i,j)
        dp = [[0] * N for _ in range(M)]
        best = 0
        for i in range(M):
            for j in range(N):

                if matrix[i][j] == '1':
                    if i == '0' or j == '0':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                best = max(best, dp[i][j])
        return best * best
