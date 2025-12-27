class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        

        n = len(s)
        # dp[i][c] defined as LIS up to index i and ends with char c
        dp = [[0] * 26 for _ in range(n + 1)]

        for i in range(1, n + 1):
            x = ord(s[i - 1]) - ord('a')

            prev = dp[i - 1]
            curr = dp[i]

            curr[:] = prev[:]

            lo = max(0, x - k)
            hi = min(25, x + k)

            best_prev = 0
            for p in range(lo, hi + 1):
                if prev[p] > best_prev:
                    best_prev = prev[p]

            curr[x] = max(curr[x], best_prev + 1)
        
        return max(dp[n])
