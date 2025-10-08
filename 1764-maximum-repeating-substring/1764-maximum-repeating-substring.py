class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        s, w = sequence, word
        n = len(s)
        m = len(w)
        dp = [0] * n
        best = 0

        for i in range(n):
            if i >= m - 1 and s[i - m + 1: i + 1] == w:
                dp[i] = 1 + (dp[i - m] if i - m >= 0 else 0)
                if dp[i] > best:
                    best = dp[i]
        return best