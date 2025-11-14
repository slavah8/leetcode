class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        vals = sorted(count.keys())
        n = len(vals)

        gain = [v * count[v] for v in vals]
        
        next_idx = [0] * n
        for i, x in enumerate(vals):
            pass
            j = bisect.bisect_right(vals, x + 2)
            next_idx[i] = j

        # dp[i] = max damage from vals[i..]
        dp = [0] * (n + 1)  # dp[n] = 0
        for i in range(n - 1, -1, -1):
            
            skip = dp[i + 1]
            j = next_idx[i]
            take = gain[i] + (dp[j] if j < n else 0)
            dp[i] = max(skip, take)
        return dp[0]
 