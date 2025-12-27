class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        
        # dp[i] = minimum number of substrings to partition s[0..i-1] (first i chars).
        n = len(s)
        INF = 10 ** 15
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            base = 1
            val = 0
            for j in range(i - 1, -1, -1):
                digit = ord(s[j]) - ord('0')
                val = digit * base + val
                
                if val > k:
                    break
                dp[i] = min(dp[i], dp[j] + 1)
                base *= 10

        return -1 if dp[n] >= INF else dp[n]
