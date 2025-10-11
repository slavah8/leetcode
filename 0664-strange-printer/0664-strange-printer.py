class Solution:
    def strangePrinter(self, s: str) -> int:
        
        # dp[i][j] defined as minimum number to print s[i:j]

        INF = 10 ** 20
        N = len(s)
        dp = [[INF] * (N) for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1


        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                best = dp[i][j - 1] + 1 # handle s[j] by itself
                # now check if theres a s[k] == s[j]
                for k in range(i, j):
                    if s[k] == s[j]:
                        best = min(best, dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0))
                dp[i][j] = best
        return dp[0][N - 1] 
