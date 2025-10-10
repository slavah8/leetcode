class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        # Let dp[s] = True iff we can pick some subset of stones that sums to exactly s.
        S = sum(stones)
        target = S // 2
        dp = [False] * (target + 1)

        dp[0] = True

        for w in stones:
            for s in range(target, w - 1, -1):
                dp[s] = dp[s - w] or dp[s]
        
        for s in range(target, -1, -1):
            if dp[s]:
                return S - 2 * s