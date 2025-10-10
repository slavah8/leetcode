class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        N = len(s1)
        M = len(s2)
        sum1 = sum(map(ord, s1))
        sum2 = sum(map(ord, s2))
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = ord(s1[i - 1]) + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        best = dp[N][M]

        x = sum1 - best
        y = sum2 - best
        return x + y