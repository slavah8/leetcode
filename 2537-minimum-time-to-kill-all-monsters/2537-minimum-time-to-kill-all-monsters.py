class Solution:
    def minimumTime(self, power: List[int]) -> int:
        
        # dp[mask] = minimum days to defeat exactly the set of monsters indicated by mask.
        INF = 10 ** 15
        n = len(power)
        m = (1 << n)
        dp = [INF] * m
        dp[0] = 0

        for mask in range(m):
            t = mask.bit_count() # how many defeated so far
            g = t + 1 # current gain
            base = dp[mask]
            if base == INF:
                continue
            for i in range(n):
                if (mask >> i) & 1: # already killed
                    continue 
                add = math.ceil(power[i] / g)
                nxt = mask | (1 << i)
                if base + add < dp[nxt]:
                    dp[nxt] = base + add
        return dp[m - 1]