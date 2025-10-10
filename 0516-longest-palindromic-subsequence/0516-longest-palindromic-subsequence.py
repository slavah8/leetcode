class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # define dp[i][j] as the length of the LPS inside s[i..j]

        N = len(s)
        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1

        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][N - 1]