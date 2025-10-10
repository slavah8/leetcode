class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        N = len(s)
        # dp[i][j] defined as LPS inside s[i...j]
        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1
        
        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        LPS = dp[0][N - 1]
        return N - LPS <= k
