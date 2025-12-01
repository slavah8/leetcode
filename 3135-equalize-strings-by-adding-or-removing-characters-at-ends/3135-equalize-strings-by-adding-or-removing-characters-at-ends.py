class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        
        n = len(initial)
        m = len(target)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        best = 0
        for i in range(1, n + 1):

            for j in range(1, m + 1):
                if initial[i - 1] == target[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > best:
                        best = dp[i][j]
                else:
                    dp[i][j] = 0
        
        # n - best + m - best
        return n + m - (2 * best)